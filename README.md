# PythonGUI

Small applications for implementing python GUI with tkinter,


#### To compile for different distro (MacOS, Windows etc)

- Run the following Installation script on different machines.

## Installation

Use PYINSTALLER to install

- `pyinstaller -F -w -i icon.icns TextEditor.py`   # (-w remove terminal window )
- OR
- `pyinstaller -F TextEditor.py --noconsole`

#### OR

echo the bat's path :

%~dp0
pyinstaller -F -w -i icon.ico Texteditor.py --clean --workpath ./pybuilds/builds --distpath ./pybuilds/dists -n myApp
