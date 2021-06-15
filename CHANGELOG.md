**v1.4.1**
* Added import for `createJail`.

**v1.4.0**
* Added new submodule `jail`.
* Reorganized several files to work slightly differently.
* Redid the imports.

**v1.3.2**
* Moved the raising of the `TemplateError` in the `drake` module so that it wouldn't include the "During the handling of the above exception" part.

**v1.3.1**
* Fixed setup.py requiring requirements already be installed to run.

**v1.3.0**
* Adjusted drake files to be core and not builder.
* Added error handling for no top or bottom text in drake.
* Added new submodule `realization`.

**v1.2.0**
* Added new submodule `test_font` for displaying an image to demonstrate the font.
* Added some custom exceptions.

**v1.1.3**
* Added new option `number` to the uno generator. This will replace the number in the "or draw 25" section if specified.

**v1.1.2**
* Fixed several doc strings.

**v1.1.1**
* Corrected the requirements to include Pillow and numpy.

**v1.1.0**
* Moved the data for the `trash` submodule into a separate file from `__init__.py` to fit the standard of the other submodules.
* Added new submodule: `ship`.
* Adjusted several file names to fit the naming convention.

**v1.0.0**
* Initial release.
