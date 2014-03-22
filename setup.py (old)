#Code for Cx_freeze
#Original setup script

from cx_Freeze import setup, Executable

copyDependentFiles=True
silent = True
includes = ["tkinter",'tkinter.ttk','sys','re','csv','os','datetime']
exe=Executable(
     script="RenCard.py",
     base="Win32Gui",
     icon="logo.ico"
     )
setup(name='RenCard',
     version = "1.0",
     options = {
       "build_exe" : {
           "includes": includes,
           },
       },
     executables=[exe],
 ) 
