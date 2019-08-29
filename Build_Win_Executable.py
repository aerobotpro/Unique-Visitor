#!/usr/bin/python3
from os import system, name;from time import sleep
cc = input("Do you still need to install Pyinstaller?. Its a dependency!(y/n): ")
if cc == "y":
    try:
        system("pip3 install pyinstaller")
    except Exception:
        system("pip install pyinstaller")     
else:
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')   
    print("Continuing..")
print("\n[Compile an exe] *Run from same directory as script!!*\n")
name = input("Whats your filename?: ")
bicon = str(input("Are You Adding An Icon?(y/n): "))     
if bicon == "y":
    icon = input("\nWhats your icon filename?: ")
    print("\nAttempting to compile (with icon)")
    args = str(f"pyinstaller -F {name} -i {icon}")
elif bicon != "y":
    print("\nAttempting to compile (without icon)")
    args = str(f"pyinstaller -F {name}")
process = system(args)
if process == 1:
    print("\n[Error] - Failed To Compile Executable")
else:
    print("\nExecutable succesfully compiled!")
sleep(.2);print("<-------------------|>\r", end="");sleep(.2);print("<-------------------\\>\r", end="");sleep(.2);print("<------------------_->\r", end="");sleep(.2);print("<----------------/--->\r", end="")
sleep(.2);print("<--------------|----->\r", end="");sleep(.2);print("<------------\\------->\r", end="");sleep(.2);print("<----------_--------->\r", end="");sleep(.2);print("<-------/------------>\r", end="")
sleep(.2);print("<----|--------------->\r", end="");sleep(.2);print("<---\\---------------->\r", end="");sleep(.2);print("<--_----------------->\r", end="");sleep(.2);print("<-/------------------>\r", end="")
sleep(.2);print("<|------------------->\r", end="");sleep(.2);print("<\\------------------->\r", end="");sleep(.2);print("<_------------------->\r", end="");sleep(.2);print("</------------------->\r", end="")
sleep(.2);print("<|------------------->\r", end="");sleep(.2);print("<\\------------------->\r", end="");sleep(.2);print("<_------------------->\r", end="");sleep(.2);print("</------------------->\r", end="")
sleep(.2);print("<|------------------->\r", end="");sleep(.2);print("<-/------------------>\r", end="");sleep(.2);print("<--_----------------->\r", end="");sleep(.2);print("<---\\---------------->\r", end="")
sleep(.2);print("<----|--------------->\r", end="");sleep(.2);print("<-------/------------>\r", end="");sleep(.2);print("<----------_--------->\r", end="");sleep(.2);print("<------------\\------->\r", end="")
sleep(.2);print("<--------------|----->\r", end="");sleep(.2);print("<--------------/----->\r", end="");sleep(.2);print("<--------------_----->\r", end="");sleep(.2);print("<--------------\\----->\r", end="")
sleep(.2);print("<-----------------|-->\r", end="");sleep(.2);print("<------------------/->\r", end="");sleep(.2);print("<-------------------_>\r", end="");sleep(.2);print("<-------------------\\>\r", end="")
sleep(.2);print("<-------------------|>\r", end="")    
