@echo off
%~dp0
pyinstaller -F -w -i icon.ico textEditor.py --clean --workpath ./pybuilds/builds --distpath ./pybuilds/dists -n myApp

cd ./pybuilds/dists
start myApp.exe