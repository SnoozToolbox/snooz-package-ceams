
# snooz-package-ceams

`snooz-package-ceams` contains three core packages—`CEAMSModules`, `CEAMSTools`, and `CEAMSApps`—developed by the [CEAMS team](http://ceams-carsm.ca). Distributed with the Snooz Toolbox, these packages provide specialized modules, tools, and applications for sleep data analysis.

This repository holds the development version of the CEAMS packages. Once modifications to the packages are complete and validated, they are released in the `snooz-toolbox` (or `snooz-toolbox-ceams` for CEAMS members) repository, ready for distribution with the Snooz installer.

## snooz-package-template Fork

This repository is a fork of [snooz-package-template](https://github.com/SnoozToolbox/snooz-package-template.git).

Scripts for creating packages, modules, tools, and apps can be found in the `utils` folder.

## CEAMS Packages

### CEAMSModules Package

Modules serve as building blocks for creating analysis pipelines, referred to as processes. Each module is designed to perform a single task, such as filtering a signal.

The `CEAMSModules` package is located in the **modules** folder. It includes a variety of modules organized into categories like Detectors, Events Utilities, File I/O, Signal Processing, and Statistics.

### CEAMSTools Package

Tools provide an abstraction layer over processes, offering a user-friendly, step-by-step interface.

Tools within Snooz are divided into three categories, each accessible from the Snooz menu bar:

- **Preprocessing:** Includes importers, converters, extractors, and the artifact detection tool.
- **Processing:** Includes sleep stage analyses, event detectors, and power spectral analysis.
- **Postprocessing:** Includes secondary analyses, such as detector performance evaluation, cohort report transposition, and slow wave event analysis.

The `CEAMSTools` package is located in the **tools** folder.

For more information about the tools in the `CEAMSTools` package, please refer to the documentation: [User Guide - Tools](https://snooz-toolbox-documentation.readthedocs.io/user_guide/tools/tools.html).

### CEAMSApps Package

An app in Snooz is a standalone application that can be loaded dynamically. As the name suggests, an app is a fully featured application that runs within Snooz. Multiple apps can be registered, but only one can run at a time.

The `CEAMSApps` package is located in the **apps** folder. Currently, Snooz includes a single app: the Oximeter viewer.


