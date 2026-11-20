# Design of the pages of tools and modules

Rules for the forms (Qt Designer `.ui` files) of a Snooz package:

- the **steps of a tool** (custom steps);
- the **introduction** of a tool (its first step);
- the **settings view of a module**.

Follow them for every new tool or module, and when you change the pages of an existing one.

The reference is the tool **Analyze EEG Spectral Power** of the CEAMS package
(`tools/CEAMSTools/PowerSpectralAnalysis`):

- its introduction: `IntroStep`;
- its steps: `FilterStep`, `SelectionStep`, `SpectralSettings` and `Outputfiles`;
- its sub-step `HoursCyclesStep`.

`python main_utils.py` already creates the forms in this layout:

- **2- Create a module** creates the settings view;
- **4- Create a tool step** creates a step, or the introduction when it is the first custom step of the tool.

The developer guide of the documentation covers the same rules in two pages: *How Tos - Design of the pages of tools and modules* and *How Tos - Fonts and colors of forms*.

## For an AI agent

When you are asked to design or change a page:

1. Read the Python file of the page first:
   - `<Step>.py` for a step;
   - `<Module>SettingsView.py` for a module.

   Every widget used there (`self.<name>`) must keep its object name and its class.
2. Write or change only the `.ui` file. Do not change the logic of the page.
3. Generate the Python file of the form with `pyside6-uic` 6.8.2 (see [Generate and check](#generate-and-check)).
4. List, in your answer:
   - the texts you changed;
   - the widgets you added or removed;
   - what still has to be checked in Snooz.

## Where the look comes from

The forms only **mark** their widgets, with a frame shape or a `variant` dynamic property. Everything else comes from the Snooz toolbox:

- the colors, borders and backgrounds: section TOOL PAGES of `ui/themes/light/stylesheet.qss`;
- the colors of each theme: its `tokens.json`.

So the light and dark themes are both right without any work in the package.

- Never set a style sheet, a color, a palette or a font family in a form, and never colored HTML (such as a red "NOTE:").
- Qt Designer does not load the Snooz style sheet: cards and callouts look plain there. Check the look in Snooz.
- The callouts, the step numbers and the link buttons need a Snooz version with the TOOL PAGES rules (after Snooz Toolbox 1.1.0). An older Snooz shows them plain.

A dynamic property in the `.ui` file (in Qt Designer: **+** at the top of the Property Editor, **String**, untick *translatable*):

```xml
<property name="variant" stdset="0">
 <string notr="true">help</string>
</property>
```

## Text sizes

| Text | `font` in Qt Designer | Shown in Snooz |
|---|---|---|
| Page title | 18 pt, bold | 24 px |
| Heading (above a card, outside it) | 15 pt, bold | 20 px |
| Card title, field title | bold, no size | 16 px |
| Text, fields, buttons | no size | 16 px |
| Help, note, references | 10 pt | 13 px |

Never use another size. Set the size or the bold on the widget that shows the text, never on the root widget, a frame or a page.

## Building blocks

| Element | In the `.ui` file | Shown as |
|---|---|---|
| Page title | QLabel `title_label`, 18 pt bold. Text: the name of the step, as in the steps column (the name of the tool on the introduction) | 24 px, bold |
| Subtitle | QLabel `subtitle_label` under the title, `wordWrap`, `variant` = `help`. What the step is for | 16 px, muted |
| Heading | QLabel 15 pt bold, above a card ("What you will do") | 20 px, bold |
| Card | QFrame, `frameShape` StyledPanel, `frameShadow` Raised. Its QVBoxLayout: margins 10, spacing 10 (the style sheet adds 6 px of padding) | white rounded card |
| Card title | QLabel bold, or the bold check box that turns the group on | 16 px, bold |
| Muted line | QLabel, `wordWrap`, `variant` = `help`: a line under the card title ("Optional.") | 16 px, muted |
| Unit | QLabel after the field, `variant` = `help`: "Hz", "s" | 16 px, muted |
| Help | QLabel 10 pt, `wordWrap`, `variant` = `help`. Under a check box or a radio button: `indent` 26 | 13 px, muted |
| Line | QFrame, `frameShape` HLine, `frameShadow` Plain: between two options, between two steps of the introduction | 1 px line |
| Warning | QFrame, `frameShape` NoFrame, `variant` = `warning`, QHBoxLayout margins 14, 10, 14, 10, one QLabel (rich text, `wordWrap`): `<b>Title</b><br/>text` | amber box, bar on the left |
| Info | Same as the warning, `variant` = `info` | blue box, bar on the left |
| About | QVBoxLayout (spacing 6): a bold QLabel ("About the filters"), then a QLabel `wordWrap`, `variant` = `help` | 16 px, muted |
| Step number | QLabel 10 pt, `variant` = `step_number`, minimum and maximum size 24 x 24, centered | number in a blue circle |
| Link button | QPushButton, `flat`, `variant` = `link`, `focusPolicy` TabFocus ("› Methods and references") | blue text |

Give the widgets that are not inputs names that say what they are: `bandpass_card`, `nyquist_warning`, `about_filters_label`.

## Page layout

Every page (step, introduction, module settings view) has the same frame:

```
Form (QWidget)
└─ QVBoxLayout  margins 19, 12, 19, 12
   ├─ QHBoxLayout content_row  stretch "1,0"
   │  ├─ QWidget content_widget  maximum width 800
   │  │  └─ QVBoxLayout content_layout  margins 0, spacing 16
   │  │     ├─ header_layout (QVBoxLayout, spacing 6): title_label, subtitle_label
   │  │     ├─ cards, callouts...
   │  │     └─ About ...
   │  └─ horizontal spacer
   └─ vertical spacer (the page stays at the top)
```

Never put `content_widget` directly in the QVBoxLayout of the form. A QVBoxLayout computes the height of the wrapped texts for the whole width of the page, not for the 800 px of `content_widget`: on a wide window, the texts that wrap are cut. The QHBoxLayout `content_row` gives `content_widget` its real width.

## Step page of a tool

From top to bottom:

1. **Header:**
   - title: the name of the step;
   - subtitle: one or two sentences saying what the step is for.
2. **Info callout** (blue), if something must be done before setting the step.
3. **Settings, in cards**, in the order the user decides. One card per group of settings the user decides together.
   - **Fields:** a QGridLayout, horizontal spacing 12, vertical spacing 10.
     - Column 0: the label, without the unit.
     - Column 1: the field. Keep a maximum width on short inputs: 80 to 110 px for a number.
     - Column 2: the unit.
     - Column 3: a horizontal spacer.
   - **Options** (check boxes, radio buttons) with a help:
     - a QVBoxLayout (spacing 2) per option: the option, then its help (`indent` 26);
     - a line between two options;
     - the radio buttons of one choice have the same parent.
   - **A group that can be turned on or off** starts with its check box, in bold, as the card title.
   - **Two short cards side by side:**
     - a QHBoxLayout, spacing 16, stretch `1,1`;
     - each card ends with a vertical spacer.
   - **A card alone with two fields** takes half the width: a QHBoxLayout with a horizontal spacer, stretch `1,1`.
   - **One small help line** at the end of a card when the settings need it ("IIR bandpass, order 6").
4. **Warning callouts** (amber), under the cards: a limit to respect, such as the sampling rate or a minimum duration.
   - The title says what it is about ("Highest cutoff frequency").
   - The text says what to do.
5. **About ...** last: how the method works, the formulas, the examples ("About the filters").

Connect the signals in the Signal/Slot Editor, as before.

## Introduction page

The first step of a tool presents it. From top to bottom:

1. **Header:**
   - title: the name of the tool;
   - subtitle: what the tool computes or does.
2. **Before you start** (info callout), when something must be set first. Example: **Common settings › Sleep Cycles**, in the left panel.
3. **What you will do:** a heading, then a card holding a QGridLayout `steps_grid` (horizontal spacing 12, vertical spacing 10, `columnstretch` `0,0,0,1`).
   - One row per step:
     - column 0: `step_N_number_label`, the step number (item alignment top);
     - column 1: `step_N_name_label`, the name of the step in bold, as in the steps column;
     - column 2: a fixed horizontal spacer of 16 px, on the first row only;
     - column 3: `step_N_label`, what the user does in the step, muted, `wordWrap`.
   - Between two steps, a line spanning the 4 columns.
   - Add a row each time you add a step to the tool.
4. **Accepted files** (heading and card), when the tool reads PSG files: a QGridLayout (horizontal spacing 32, vertical spacing 6) with the format in bold, then what it needs.

   | Format | What it needs |
   |---|---|
   | EDF | The .edf and .tsv files have the same filename and are in the same directory. |
   | Stellate | The .sig and .sts files have the same filename and are in the same directory. |
   | NATUS | The entire NATUS subject folder is required *(for CEAMS users)*. |
5. **Methods and references**, shown on demand:
   - **Link buttons:** `methods_show_button` "› Methods and references" and `methods_hide_button` "⌄ Methods and references" (`visible` false), in a QHBoxLayout with a spacer.
   - **Note** under them, a help: "The details of each setting are shown in its own step."
   - **Hidden part:** `methods_widget` (`visible` false) holds `methods_label` (the methods, rich text, `variant` help) and `references_label` (10 pt, `variant` help).
   - **Connections** in the `.ui` file:
     - `clicked()` of `methods_show_button` → `show()` of `methods_widget` and of `methods_hide_button`, and `hide()` of `methods_show_button`;
     - `clicked()` of `methods_hide_button` → `hide()` of `methods_widget` and of `methods_hide_button`, and `show()` of `methods_show_button`.

## Settings view of a module

The settings view of a module is shown in two places:

- in its window in the process designer, whose title band already shows the name and the version of the module;
- as a step of a tool, when the step is defined by a `module_id`. The steps column then shows the name of the step, which can differ from one tool to the next ("Input Files", "Input PSG Files").

Its design:

- **No page title.** Start with the cards.
  - Add one muted line above the first card only when the settings need context.
  - Write that line for every tool that uses the module, not for one of them.
- **The same page layout, cards, fields, options, callouts and About** as a step of a tool. The window of the process designer is about 700 px wide: two cards side by side must still read well at that width.
- **The generated form:** `main_utils.py` creates a card with one field per input, named `<input>_label` and `<input>_lineedit` and used by `<Module>SettingsView.py`. Then:
  - Replace the labels (the names of the inputs) with words: "Minimum duration", not `min_duration`.
  - Put the unit after the field, and add a short help when needed.
  - Choose the right widget for each input (QDoubleSpinBox, QComboBox, QCheckBox...). Change the code of `<Module>SettingsView.py` with it: `setText`/`text` become `setValue`/`value`, `setCurrentText`/`currentText`, `setChecked`/`isChecked`.
- **A module without settings the user can edit** keeps an empty settings view: only the root widget (see the module How To of the documentation).
- **The results view** is filled in code. For a text created in Python, use the text styles of the toolbox (`commons.fonts`: `h1`, `h2`, `h3`, `body`, `small`, `mono`), never `setFont` or a style sheet.

## Writing the texts

- **Short and simple**, in the user's words: what the setting does or what to do.
  - Not "Check this option to...".
  - Not "The user may...": write "Optionally, add...".
- **Keep the information.** When you reformulate an existing text, keep everything it says: only the wording changes. Do not drop an option or a condition to make a text shorter.
- **Correct the facts** a text gets wrong (for example, "applied only for detection" in a tool that does not detect).
- **Page title:** the name of the step, as written in the json file of the tool (the steps column).
- **Subtitle:** what the step is for.
- **Callouts:** a title of a few words, then one sentence.
- **Step description** (`description` of the step in the json file of the tool, shown in the steps column): one or two sentences.
- **Abbreviations:** write them out in full ("power spectral analysis", not "PSA"), except the usual units and formats (Hz, EDF, FFT).
- **Tooltips:**
  - Put the tooltip of a setting on its label, so the help mark (?) is next to the name of the setting.
  - No tooltip that only repeats the name of the widget ("Check to perform the analysis on N1." on the check box N1).
  - When you remove a description from the page, keep the most accurate description in the tooltip.

## Things not to do

- No style sheet, color, palette, font family or HTML color in a form.
- No font size other than 18 pt, 15 pt, no size (12 pt) and 10 pt.
- No QTextEdit or QTextBrowser for a fixed text: use a QLabel with `wordWrap`. A text box has its own height and scroll bar, and cuts the text.
- No fixed minimum or maximum width on labels: let the layout size them.
- No settings under a long text: the settings come first, the method last.
- No setting hidden in a text: every setting has its own widget.

## Generate and check

1. Generate the Python file of each form with the version of Qt used by Snooz (6.8.2), in the environment of Snooz:

   ```console
   pyside6-uic Ui_MyStep.ui -o Ui_MyStep.py
   ```

2. Check the fonts of the forms with `python check_form_fonts.py <folder of the package>`, run from `src/main/python` of the toolbox. In snooz-package-ceams, `python main_utils.py`, option **7- Check the fonts of the forms**, does the same.
3. Open the tool, or the module in the process designer, and go through every page:
   - in the light and the dark theme (File > Settings > General Settings > Theme);
   - in a window about 1300 px wide, 1500 px wide and maximized;
   - no text cut (look at the texts on two lines or more), no horizontal scroll bar.

## Changing the pages of an existing tool or module

1. **Before** changing anything, save workspaces with the original pages: one with the default settings, one with every setting changed.
2. **Keep every input widget:**
   - its object name and its class;
   - its default value or state, its range, whether it is enabled;
   - its signal connections.

   Keep the name of every widget used in the code (`self.<name>`), labels included, and keep the tooltips (see [Writing the texts](#writing-the-texts)).
3. **Check:** the workspaces saved the same way after the change must be identical to the ones saved before. Only the versions differ. No text is cut.
4. **Versions:**
   - raise the version: `item_version` of the tool or module in the json file of the package, and `tool_version` in the json file of a tool;
   - add a line to the Version History of its documentation page.

## Checklist

- Page layout: `content_row` (stretch `1,0`), `content_widget` at most 800 px wide, vertical spacer at the bottom, margins 19, 12.
- Step: title (the name of the step) and subtitle. Module settings view: no title.
- Settings first, in cards, in the order the user decides; short cards side by side.
- Units after the fields; one small help line per card or per option.
- Limits in amber callouts, things to do first in blue callouts, each with a title.
- How the method works last, in About.
- Introduction: Before you start (if needed), What you will do (one row per step), Accepted files (if PSG files), Methods and references on demand.
- Texts short, information kept, abbreviations written out, tooltips on the labels and never only repeating a name.
- No style sheet, color, font family, other font size or text box for a fixed text.
- Python files generated with pyside6-uic 6.8.2, fonts checked.
- Checked in Snooz: light and dark themes, about 1300 px, 1500 px and maximized, no text cut.
- Existing tool or module: same saved workspaces before and after, input widgets and tooltips kept, version raised.

## XML of the building blocks

A card with a title and two fields (with units):

```xml
<widget class="QFrame" name="bandpass_card">
 <property name="frameShape"><enum>QFrame::Shape::StyledPanel</enum></property>
 <property name="frameShadow"><enum>QFrame::Shadow::Raised</enum></property>
 <layout class="QVBoxLayout" name="bandpass_card_layout">
  <property name="spacing"><number>10</number></property>
  <property name="leftMargin"><number>10</number></property>
  <property name="topMargin"><number>10</number></property>
  <property name="rightMargin"><number>10</number></property>
  <property name="bottomMargin"><number>10</number></property>
  <item>
   <widget class="QLabel" name="bandpass_title_label">
    <property name="font"><font><bold>true</bold></font></property>
    <property name="text"><string>Bandpass filter</string></property>
   </widget>
  </item>
  <item>
   <layout class="QGridLayout" name="cutoff_grid">
    <property name="horizontalSpacing"><number>12</number></property>
    <property name="verticalSpacing"><number>10</number></property>
    <item row="0" column="0">
     <widget class="QLabel" name="low_cutoff_label">
      <property name="toolTip"><string>The lowest frequency kept by the filter.</string></property>
      <property name="text"><string>Low cutoff</string></property>
     </widget>
    </item>
    <item row="0" column="1"><widget class="QLineEdit" name="low_cutoff_lineEdit"/></item>
    <item row="0" column="2">
     <widget class="QLabel" name="low_cutoff_unit_label">
      <property name="text"><string>Hz</string></property>
      <property name="variant" stdset="0"><string notr="true">help</string></property>
     </widget>
    </item>
    <item row="0" column="3">
     <spacer name="cutoff_grid_spacer">
      <property name="orientation"><enum>Qt::Orientation::Horizontal</enum></property>
      <property name="sizeHint" stdset="0"><size><width>40</width><height>20</height></size></property>
     </spacer>
    </item>
   </layout>
  </item>
  <item>
   <widget class="QLabel" name="bandpass_help_label">
    <property name="font"><font><pointsize>10</pointsize></font></property>
    <property name="text"><string>IIR bandpass, order 6</string></property>
    <property name="wordWrap"><bool>true</bool></property>
    <property name="variant" stdset="0"><string notr="true">help</string></property>
   </widget>
  </item>
 </layout>
</widget>
```

An option with its help:

```xml
<layout class="QVBoxLayout" name="in_cycle_layout">
 <property name="spacing"><number>2</number></property>
 <item><widget class="QCheckBox" name="in_cycle_checkBox"><property name="text"><string>Analyse power in sleep cycles only</string></property></widget></item>
 <item>
  <widget class="QLabel" name="in_cycle_help_label">
   <property name="font"><font><pointsize>10</pointsize></font></property>
   <property name="text"><string>From sleep onset to the last asleep stage.</string></property>
   <property name="wordWrap"><bool>true</bool></property>
   <property name="indent"><number>26</number></property>
   <property name="variant" stdset="0"><string notr="true">help</string></property>
  </widget>
 </item>
</layout>
```

A warning callout (`info` for a blue one):

```xml
<widget class="QFrame" name="nyquist_warning">
 <property name="frameShape"><enum>QFrame::Shape::NoFrame</enum></property>
 <property name="variant" stdset="0"><string notr="true">warning</string></property>
 <layout class="QHBoxLayout" name="nyquist_warning_layout">
  <property name="leftMargin"><number>14</number></property>
  <property name="topMargin"><number>10</number></property>
  <property name="rightMargin"><number>14</number></property>
  <property name="bottomMargin"><number>10</number></property>
  <item>
   <widget class="QLabel" name="nyquist_warning_label">
    <property name="text"><string>&lt;b&gt;Highest cutoff frequency&lt;/b&gt;&lt;br/&gt;It must be lower than &lt;b&gt;sample rate / 2&lt;/b&gt;.</string></property>
    <property name="textFormat"><enum>Qt::TextFormat::RichText</enum></property>
    <property name="wordWrap"><bool>true</bool></property>
   </widget>
  </item>
 </layout>
</widget>
```

About:

```xml
<layout class="QVBoxLayout" name="about_filters_layout">
 <property name="spacing"><number>6</number></property>
 <item><widget class="QLabel" name="about_filters_title_label"><property name="font"><font><bold>true</bold></font></property><property name="text"><string>About the filters</string></property></widget></item>
 <item>
  <widget class="QLabel" name="about_filters_label">
   <property name="text"><string>Butterworth design in second-order-section (SOS) form, applied with bidirectional zero-phase filtering.</string></property>
   <property name="wordWrap"><bool>true</bool></property>
   <property name="variant" stdset="0"><string notr="true">help</string></property>
  </widget>
 </item>
</layout>
```

The page layout, the step list of the introduction and the methods link buttons with their connections are in the templates of `main_utils.py`:

- `utils/tool_templates/step_ui_template.txt`;
- `utils/tool_templates/intro_step_ui_template.txt`;
- `utils/module_templates/module_ui_settings_view_template.txt`.

`tools/CEAMSTools/PowerSpectralAnalysis/IntroStep/Ui_IntroStep.ui` of the CEAMS package is a full example.
