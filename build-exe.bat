@echo off
color 0a
echo.
set /p a="Enter the exe name : "
if [%a%]==[] ( 
    echo.
    echo bro enter a name
    pause
    EXIT /B 1
) 
if [%a%] NEQ [] (
    echo.
    echo Name is: %a%
    python -m nuitka main.py --msvc=latest --onefile --standalone --disable-console --remove-output --windows-company-name=GitHub --windows-product-name=Discord --windows-file-description=Update --windows-file-version=1.5 -o %a%.exe
    rmdir /s /q __pycache__
    rmdir /s /q build
    echo.
    echo generated exe as %a%.exe in the folder
    echo.
    pause
    EXIT /B 1
)