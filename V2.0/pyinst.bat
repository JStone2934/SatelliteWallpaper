@echo on
pip install virtualenv
pip install pyinstaller
virtualenv satwp
call satwp\Scripts\activate
pip install pyinstaller
pip install opencv-python
pip install pillow
pip install pywin32
pip install pystray==0.18.0
pyinstaller -n ·ç±©ÑÛ -F -w -p satwp\Lib\site-packages -i .\icon.png --add-data ".\icon.png;."  tray.py 
pause