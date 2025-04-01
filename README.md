# PyCharm stubs for GIMP 3 Python Modules

PyCharm can automatically generate Python stub files for GIMP 3 binary modules such as `gi.repository.GimpUi`, `gi.repository.Gtk` and many more to provide code completion suggestions when developing Python plug-ins for GIMP 3.

However, PyCharm currently fails to generate modules for `gi.repository.Gimp` and `gi.repository.cairo` modules (the former being the most important module for plug-in development). I worked around the problem by modifying the source code responsible for generating PyCharm stubs to ignore any exceptions along the process (which causes the problematic constants to be omitted in the stubs).

This repository contains the missing stubs for `gi.repository.Gimp` and `gi.repository.cairo` modules.

## Installation

Download the repository and copy the `cairo` and `Gimp` directories to a PyCharm directory containing other generated stubs for GIMP 3 under the `gi/repository` directory.

Assuming you added GIMP Python modules to your Python interpreter in PyCharm, you can find the path as follows:

1. Go to your PyCharm project and display the Project view.
2. Find `External Libraries `, expand it to find `Binary Skeletons`, right-click on the `gi/repository` directory, select `Copy Path/Reference...` and select `Absolute Path`.

It may happen that PyCharm automatically deletes the directories that you just copied when you restart PyCharm. To prevent the directories from being deleted:

* On Linux, run `chattr +i [directory]` for each directory.
* On Windows:
     1. Right-click on a directory, then go to `Properties -> Security -> Advanced`.
     2. Click on your user account (not SYSTEM or Administrators), then click `Disable inheritance`, then `Convert inherited permissions into explicit permissions for this object.`.
     3. Still having your user account selected, click `Edit`.
     4. In the displayed dialog, click `Show advanced permissions`, and then uncheck `Delete` and `Delete subfolders and files`.
     5. Save the changes.
     6. Repeat the above steps for all other directories you wish to keep.
