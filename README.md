# PythonGUI
 Small applications for implementing python GUI with tkinter,


Use PYINSTALLER to install

pyinstaller -F -w -i icon.ico mycode.py    # (-w remove terminal window )
pyinstaller -F mycode.py --noconsole 


echo the bat's path : 

%~dp0
pyinstaller -F -w -i icon.ico texteditor.py --clean --workpath ./pybuilds/builds --distpath ./pybuilds/dists -n myApp