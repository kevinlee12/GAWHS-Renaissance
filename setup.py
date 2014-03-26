import sys
from cx_Freeze import setup, Executable

copyDependentFiles=True

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os",'tkinter','sys','re','csv','datetime'],'include_files':['logowhite.gif']}


exe=Executable(
     script="Rencard.py",
     base="Win32Gui",
     icon="logo.ico"
     #copyDependentFiles='True'
     )

setup(  name = "RenCard",
        version = "1.0",
        description = "RenCard App",
        options = {"build_exe": build_exe_options},
        executables = [exe]
        )
