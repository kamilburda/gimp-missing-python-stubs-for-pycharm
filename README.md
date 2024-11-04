# PyCharm stubs for GIMP 3 Python Modules

PyCharm can automatically generate Python stub files for GIMP 3 binary modules such as `gi.repository.GimpUi`, `gi.repository.Gtk` and many more to provide code completion suggestions when developing Python plug-ins for GIMP 3.

However, PyCharm currently fails to generate modules for `gi.repository.Gimp` and `gi.repository.cairo` modules (the former being the most important module for plug-in development). I worked around the problem by modifying the source code responsible for generating PyCharm stubs to ignore any exceptions along the process (which causes the problematic constants to be omitted in the stubs).

This repository contains the missing stubs for `gi.repository.Gimp` and `gi.repository.cairo` modules.

## Installation

Download the repository and copy the `cairo` and `Gimp` directories to a PyCharm directory containing other generated stubs for GIMP 3 under the `gi/repository` directory.

Assuming you added GIMP Python modules to your Python interpreter in PyCharm, you can find the path as follows:

1. Go to your PyCharm project and display the Project view.
2. Find `External Libraries `, expand it to find `Binary Skeletons`, right-click on the `gi/repository` directory, select `Copy Path/Reference...` and select `Absolute Path`.


On Windows, the path should be

    C:\Users\<your username>\AppData\Local\JetBrains\<PyCharm directory, e.g. PyCharmCE2023.2>\python_stubs\<number>\gi\repository.


To find the correct `<number>` directory, look for all directories whose name is a number and select the one that contains the `gi` subdirectory.
