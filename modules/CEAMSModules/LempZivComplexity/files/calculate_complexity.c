/*******************************************************************/
/*                                                                 */
/*  calculate_complexity.c                                              */
/*                                                                 */
/*  Lempel-Ziv complexity kernel used by Snooz LempZivComplexity.  */
/*                                                                 */
/*  PROVENANCE                                                     */
/*  -----------                                                    */
/*  Core LZ parser and multi_uni packing are based on the C/MEX    */
/*  implementation by:                                             */
/*    - Tofik Amara (July 2002)                                    */
/*    - Steeve Zozor (January 2003)                                */
/*  Algorithm: Kaspar & Schuster, Phys. Rev. A 36(2):842-848, 1987 */
/*  Multidimensional / joint LZC theory:                           */
/*    Zozor, Ravier & Buttelli, Physica A 345:285-302, 2005        */
/*  EEG pipeline usage (binarization + FT-surrogate normalization  */
/*  done in Python, not here):                                     */
/*    Toker et al., PNAS 2022 (fJLZC / joint & concat LZC)         */
/*  Concatenation mode (Schartner et al., PLoS One 2015) is        */
/*  prepared in Python; this file then sees a 1D binary string.    */
/*                                                                 */
/*  WHY THIS FILE EXISTS IN C                                      */
/*  -------------------------                                      */
/*  The Kaspar-Schuster scan is roughly O(nt^2). Pure Python is    */
/*  far too slow for sleep / hd-EEG windows; ctypes calls this     */
/*  shared library instead.                                        */
/*                                                                 */
/*  API (exported for Python ctypes)                               */
/*  --------------------------------                               */
/*  multi_uni(...)                                                 */
/*      Pack binary channels into one scalar series (Zozor).       */
/*  complexity(...)                                                */
/*      Single-group / 1D LZC. Used for concat (nc==1 after        */
/*      Python flatten) or joint when nc <= MAX_CH_PER_GROUP.      */
/*  complexity_joint(...)                                          */
/*      Joint LZC for any channel count. Automatically splits      */
/*      channels into groups of at most MAX_CH_PER_GROUP, packs    */
/*      each group, and requires ALL groups to match for a         */
/*      "vector match" (equivalent to full Zozor joint equality).  */
/*                                                                 */
/*  WHY AUTOMATIC GROUPING?                                        */
/*  -----------------------                                        */
/*  Packing binary channels into one IEEE-754 double is only       */
/*  unique for about 53 bits (2^53). Using groups of <= 50 keeps   */
/*  packing exact. Older code hard-coded 2 groups (hd) or 5        */
/*  groups (hd2). Here:                                            */
/*      n_groups = ceil(nc / MAX_CH_PER_GROUP)                     */
/*  All-groups-must-match == full Zozor vector equality.           */
/*  NOTE: for large nc, joint LZC often saturates (c ≈ nt) so      */
/*  data/surrogate ratios approach 1 — a property of joint LZC,    */
/*  not a failure of grouping. */
/*                                                                 */
/*  MEMORY LAYOUT                                                  */
/*  --------------                                                 */
/*  signal is row-major (C contiguous), matching NumPy (nc, nt):   */
/*      signal[ch * nt + t]                                        */
/*                                                                 */
/*  Build (same commands as lzc_complexity/.github/workflows):     */
/*    Windows x86_64:                                              */
/*      gcc -O2 -shared -o calculate_complexity_64.dll \           */
/*          calculate_complexity.c                                 */
/*    Linux x86_64:                                                */
/*      gcc -O2 -fPIC -shared -o calculate_complexity_64.so \      */
/*          calculate_complexity.c                                 */
/*    macOS Intel x86_64:                                          */
/*      clang -O2 -dynamiclib -o calculate_complexity_x86_64.dylib */
/*          calculate_complexity.c                                 */
/*    macOS Apple Silicon arm64:                                   */
/*      clang -O2 -dynamiclib -o calculate_complexity_arm64.dylib  */
/*          calculate_complexity.c                                 */
/*                                                                 */
/*******************************************************************/

#include <math.h>
#include <stdlib.h>

/* Max binary channels packed into one double.
 * Must stay below ~53 so each group maps uniquely into a double
 * (mantissa of IEEE-754). 50 leaves a safety margin. */
#define MAX_CH_PER_GROUP 50

/********************************************************************/
/* multi_uni                                                        */
/*                                                                  */
/* Zozor "joint discretization": at each time t, encode the binary  */
/* channel vector as one scalar:                                    */
/*   sig[t] = sum_{ch=0}^{nc-1} signal[ch,t] * al^ch                */
/* With al=2 this is the usual bit packing (ch0 = LSB).             */
/*                                                                  */
/* Inputs:                                                          */
/*   nc, nt  - channels, time points                                */
/*   signal  - binary matrix, row-major [ch * nt + t]               */
/*   al      - alphabet size (2 for binary EEG after thresholding)  */
/* Output:                                                          */
/*   sig     - length nt; caller-allocated                          */
/********************************************************************/
void multi_uni(int nc, int nt, const double *signal, double al, double *sig)
{
  double a;
  int indt, indc;

  for (indt = 0; indt < nt; indt++)
  {
    /* Build one integer code for the channel vector at time indt. */
    sig[indt] = 0.0;
    a = 1.0;
    for (indc = 0; indc < nc; indc++)
    {
      sig[indt] = sig[indt] + a * signal[indc * nt + indt];
      a = a * al;
    }
  }
}

/********************************************************************/
/* complexity                                                       */
/*                                                                  */
/* Kaspar-Schuster production complexity on a (packed) series.      */
/*                                                                  */
/* Flow:                                                            */
/*   1) multi_uni: channels -> one scalar series                    */
/*   2) scan history for longest copyable phrase; count phrases c   */
/*                                                                  */
/* Use when:                                                        */
/*   - mode=='concat' in Python (matrix flattened to 1 x (nc*nt))   */
/*   - or joint with nc <= MAX_CH_PER_GROUP (one group is enough)   */
/*                                                                  */
/* Inputs:                                                          */
/*   nc, nt, signal, al - see multi_uni                             */
/*   sig - workspace of length nt (caller-allocated)                */
/* Output:                                                          */
/*   c   - Lempel-Ziv complexity (phrase count)                     */
/*                                                                  */
/* Notes:                                                           */
/*   Labels step1/step2/goto follow the historical Zozor C style.   */
/*   m tracks production count in the original algorithm; c is the  */
/*   quantity returned to Python.                                   */
/********************************************************************/
void complexity(int nc, int nt, const double *signal, double al,
                double *sig, double *c)
{
  int i, k, kmax;
  int l = 1; /* start index of the current phrase in the sequence */
  int m = 1; /* production / phrase counter (historical variable) */

  /* Pack (or copy if nc==1) into sig[0..nt-1]. */
  multi_uni(nc, nt, signal, al, sig);

  /* At least one phrase exists for a non-empty sequence. */
  *c = 1.0;

step1:
  /* Restart search for a copy of the current phrase in history [0, l). */
  i = 0;
  k = 1;
  kmax = 1;
step2:
  /* Does history starting at i match the current phrase for k symbols? */
  if (*(sig + i + k - 1) == *(sig + l + k - 1))
  {
    k = k + 1;
    if ((l + k) > nt)
    {
      /* Ran off the end of the series: finish last phrase. */
      *c = (*c) + 1.0;
      goto output;
    }
    else
    {
      /* Keep extending the match. */
      goto step2;
    }
  }
  else
  {
    /* Mismatch: remember longest match from this history start. */
    if (k > kmax)
    {
      kmax = k;
    }
    i = i + 1;
    if (i == l)
    {
      /* Exhausted history: emit one new phrase and advance. */
      *c = (*c) + 1.0;
      m = m + 1;
      l = l + kmax;
      if (l + 1 > nt)
      {
        goto output;
      }
      else
      {
        goto step1;
      }
    }
    else
    {
      /* Try next history position. */
      k = 1;
      goto step2;
    }
  }
output:
  return;
}

/********************************************************************/
/* complexity_joint                                                 */
/*                                                                  */
/* Joint (Zozor) Lempel-Ziv for any number of channels.             */
/*                                                                  */
/* WHY NOT ONE multi_uni OVER ALL CHANNELS?                         */
/* Doubles cannot uniquely encode >~53 binary channels. Encoding    */
/* everything in one number would collide different vectors.        */
/*                                                                  */
/* SOLUTION (automatic grouping):                                   */
/*   n_groups = ceil(nc / MAX_CH_PER_GROUP)                         */
/*   Pack each group of <=50 channels into its own scalar series.   */
/*   Two times match iff EVERY group matches at that time.          */
/*   That is equivalent to full channel-vector equality.            */
/*                                                                  */
/* Examples:                                                        */
/*   32 ch  -> 1 group                                              */
/*   64 ch  -> 2 groups                                             */
/*   128 ch -> 3 groups                                             */
/*   256 ch -> 6 groups                                             */
/*                                                                  */
/* Inputs:                                                          */
/*   nc, nt, signal, al - full binary matrix (row-major)            */
/* Output:                                                          */
/*   c - joint Lempel-Ziv complexity                                */
/*                                                                  */
/* Allocates temporary packed[n_groups * nt]; freed before return.  */
/********************************************************************/
void complexity_joint(int nc, int nt, const double *signal, double al,
                      double *c)
{
  int i, k, kmax, g, match;
  int l = 1;
  int m = 1;
  int n_groups;
  int ch_start, ch_end, nc_g;
  double *packed;

  if (nc < 1 || nt < 1)
  {
    *c = 0.0;
    return;
  }

  /* Integer ceil(nc / MAX_CH_PER_GROUP). */
  n_groups = (nc + MAX_CH_PER_GROUP - 1) / MAX_CH_PER_GROUP;

  /* packed[g * nt + t] = integer code for group g at time t. */
  packed = (double *)malloc((size_t)n_groups * (size_t)nt * sizeof(double));
  if (packed == NULL)
  {
    *c = 0.0;
    return;
  }

  /* Pack each channel block independently. */
  for (g = 0; g < n_groups; g++)
  {
    ch_start = g * MAX_CH_PER_GROUP;
    ch_end = ch_start + MAX_CH_PER_GROUP;
    if (ch_end > nc)
    {
      ch_end = nc;
    }
    nc_g = ch_end - ch_start;
    /* signal + ch_start*nt points at the first row of this group. */
    multi_uni(nc_g, nt, signal + ch_start * nt, al, packed + g * nt);
  }

  *c = 1.0;

step1:
  i = 0;
  k = 1;
  kmax = 1;
step2:
  /* Vector match = all group codes match at this offset. */
  match = 1;
  for (g = 0; g < n_groups; g++)
  {
    if (*(packed + g * nt + i + k - 1) != *(packed + g * nt + l + k - 1))
    {
      match = 0;
      break;
    }
  }

  if (match)
  {
    k = k + 1;
    if ((l + k) > nt)
    {
      *c = (*c) + 1.0;
      goto output;
    }
    else
    {
      goto step2;
    }
  }
  else
  {
    if (k > kmax)
    {
      kmax = k;
    }
    i = i + 1;
    if (i == l)
    {
      *c = (*c) + 1.0;
      m = m + 1;
      l = l + kmax;
      if (l + 1 > nt)
      {
        goto output;
      }
      else
      {
        goto step1;
      }
    }
    else
    {
      k = 1;
      goto step2;
    }
  }
output:
  free(packed);
  return;
}
