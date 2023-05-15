# PythonGUI

Small applications for implementing python GUI with tkinter,



## Installation

Use PYINSTALLER to install

- `pyinstaller -F -w -i icon.icns textEditor.py`   # (-w remove terminal window )
- OR
- `pyinstaller -F textEditor.py --noconsole`



#### OR

echo the bat's path :

%~dp0
pyinstaller -F -w -i icon.ico texteditor.py --clean --workpath ./pybuilds/builds --distpath ./pybuilds/dists -n myApp
