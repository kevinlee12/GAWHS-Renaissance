#Code for Cx_freeze

from cx_Freeze import setup, Executable

#copyDependentFiles=True
#silent = False
#includes = ["tkinter",'tkinter.ttk','sys','re','csv','os','datetime']
#build_exe_options = {"packages": ["os","tkinter",'tkinter.ttk','sys','re','csv','os','datetime'], "include_files":['logowhite.gif']}

##exe=Executable(
##     script="Rencard.py",
##     base="Win32Gui",
##     icon="logo.ico"
##     )
##setup(name='RenCard',
##     version = "2.0",
##     description = "Renaissance Card Application",
##     options = {"build_exe": build_exe_options},
##     executables=[exe]
## ) 


#Redo

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os",'tkinter','sys','re','csv','datetime'],'include_files':['logowhite.gif']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe=Executable(
     script="Rencard.py",
     base="Win32Gui",
     icon="logo.ico"
     )

setup(  name = "RenCard",
        version = "1.0",
        description = "RenCard App",
        options = {"build_exe": build_exe_options},
        executables = [exe]
        )
