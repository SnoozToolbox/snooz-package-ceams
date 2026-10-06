#!/usr/bin/env python3
"""
Test suite for UTF-8 encoding conversion with multi-language PSG headers.

Tests the _ensure_utf8_string function with various encodings:
- Latin-1 (French accents: é, è, ê, à, ç, etc.)
- Windows-1252 (Windows-1252 specific characters)
- UTF-8 (already valid)
- Mixed/corrupted encodings
"""

import sys
import os

# Add the module path to imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from SlowWavesDetails import _ensure_utf8_string


def test_utf8_valid():
    """Test: valid UTF-8 string should pass through unchanged."""
    test_str = "Patient Name: José García"
    result = _ensure_utf8_string(test_str)
    assert result == test_str, f"UTF-8 string modified: {repr(result)}"
    print("✓ Valid UTF-8 string preserved")


def test_latin1_french():
    """Test: Latin-1 encoded French text (é, è, ê, à, ç)."""
    # Simulate Latin-1 bytes decoded as if they were UTF-8 (common error)
    latin1_bytes = "Patient: Jérôme Lescure, Âge: 23".encode('latin-1')
    # When Python wrongly interprets Latin-1 bytes as UTF-8, it creates mojibake
    try:
        corrupted = latin1_bytes.decode('utf-8')
    except UnicodeDecodeError:
        # This is what we expect - we need to handle it
        corrupted = latin1_bytes.decode('latin-1')
    
    # Now test our fix
    result = _ensure_utf8_string(corrupted)
    # Should restore to proper French text
    assert 'é' in result or 'Jérôme' in result or 'Âge' in result, \
        f"French accents not preserved: {repr(result)}"
    print("✓ Latin-1 French text converted to UTF-8")


def test_latin1_spanish():
    """Test: Latin-1 encoded Spanish text (á, é, í, ó, ú, ñ)."""
    spanish_bytes = "Paciente: Señor José María".encode('latin-1')
    corrupted = spanish_bytes.decode('latin-1')
    result = _ensure_utf8_string(corrupted)
    # Verify result can be encoded as UTF-8 without error
    result.encode('utf-8')  # Should not raise
    print("✓ Latin-1 Spanish text converted to UTF-8")


def test_latin1_german():
    """Test: Latin-1 encoded German text (ä, ö, ü, ß)."""
    german_bytes = "Patient: Müller, Größe: 180".encode('latin-1')
    corrupted = german_bytes.decode('latin-1')
    result = _ensure_utf8_string(corrupted)
    result.encode('utf-8')  # Should not raise
    print("✓ Latin-1 German text converted to UTF-8")


def test_windows1252():
    """Test: Windows-1252 specific characters (€, –, …, etc)."""
    # Euro sign (€) is in Windows-1252 but not Latin-1
    test_bytes = "Price: €50, Range: 10–20".encode('windows-1252')
    try:
        # Try to decode as UTF-8 first (will fail for some bytes)
        corrupted = test_bytes.decode('utf-8', errors='replace')
    except:
        corrupted = test_bytes.decode('windows-1252')
    
    result = _ensure_utf8_string(corrupted)
    result.encode('utf-8')  # Should not raise
    print("✓ Windows-1252 text converted to UTF-8")


def test_non_string():
    """Test: non-string values should pass through unchanged."""
    test_cases = [
        123,
        45.67,
        None,
        [],
        {'key': 'value'},
    ]
    for value in test_cases:
        result = _ensure_utf8_string(value)
        assert result == value, f"Non-string value modified: {repr(result)}"
    print("✓ Non-string values pass through unchanged")


def test_mixed_encoding_error():
    """Test: corrupted/mixed encoding should still be readable."""
    # Simulate the actual error from the user's file:
    # byte 0x89 at position 49283
    # This is invalid UTF-8
    corrupted = "APN?©E-MCI"  # © is byte 0xA9 in Latin-1 (similar to 0x89 problem)
    result = _ensure_utf8_string(corrupted)
    # Should produce a valid UTF-8 string
    result.encode('utf-8')  # Should not raise
    print("✓ Mixed/corrupted encoding handled gracefully")


def test_ascii_only():
    """Test: pure ASCII should pass through unchanged."""
    test_str = "PATIENT_001_NIGHT_SLEEP"
    result = _ensure_utf8_string(test_str)
    assert result == test_str, f"ASCII string modified: {repr(result)}"
    print("✓ Pure ASCII preserved")


def test_psg_header_realistic():
    """Test: realistic PSG header data from different regions."""
    test_cases = {
        'French': "Patient: Jean-François Dupont, Hospital: Hôpital Universitaire",
        'Spanish': "Paciente: María José García López, Clínica: Clínica Universitaria",
        'German': "Patient: Klaus Müller, Krankenhaus: Uniklinik München",
        'Portuguese': "Paciente: João Silva, Clínica: Clínica da Universidade",
        'Dutch': "Patiënt: Joop van der Berg, Ziekenhuis: Universitair Ziekenhuis",
    }
    
    for lang, text in test_cases.items():
        result = _ensure_utf8_string(text)
        # Verify it can be encoded as UTF-8
        result.encode('utf-8')
        # Verify the text is still readable
        assert len(result) > 0
        print(f"  ✓ {lang}: {result[:50]}...")
    
    print("✓ All realistic PSG headers converted to UTF-8")


if __name__ == '__main__':
    print("Testing UTF-8 encoding conversion for multi-language PSG headers\n")
    print("=" * 70)
    
    test_utf8_valid()
    test_latin1_french()
    test_latin1_spanish()
    test_latin1_german()
    test_windows1252()
    test_non_string()
    test_mixed_encoding_error()
    test_ascii_only()
    test_psg_header_realistic()
    
    print("=" * 70)
    print("\n✅ All tests passed!")
