# PyCharm stubs for GIMP 3 Python Modules

This repository contains pre-generated stubs for `gi.repository.Gimp` and `gi.repository.cairo` modules that can aid you in developing Python plug-ins for GIMP 3 or later, by providing code completion suggestions.

While PyCharm can automatically generate Python stub files for most GIMP binary modules such as `gi.repository.GimpUi` or `gi.repository.Gtk`, PyCharm may fail to generate stubs for `gi.repository.Gimp` and `gi.repository.cairo` on some platforms [due to a bug](https://gitlab.gnome.org/GNOME/gimp/-/issues/10562).

Technical note: The source code responsible for generating PyCharm stubs was modified to ignore any exceptions along the process (omitting any faulty global variables, classes, etc. that raise an exception), allowing stubs for `gi.repository.Gimp` and `gi.repository.cairo` to be generated.


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
