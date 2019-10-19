'''
    Copyright (c) Fotis Antonatos. 2019
    
    drivesync is a tool that keeps files on your computer in sync with those on your removable drives.
    
'''

from datetime import datetime
from os.path import exists
from sys import exit
import subprocess
import time
import os


# Data



# Functions

'''
#   reads instructions from the drivesync configuration file located in the given drive
def parseInstructions(driveLetter):
    with open(driveLetter + ':\\drivesync.inf', 'r') as file:
        # parse the entire instruction file
        instructions = []
        for line in file:
            instructions.append(line)
            
    return instructions
''' 

def isSyncEnabled(driveLetter):
    if exists(driveLetter + ':\\syncexec.bat'):
        return True
    return False

def getDrives():
    drives = []
    for drive in range(ord('A'), ord('Z') + 1):
        if exists(chr(drive) + ':'):
            drives.append(chr(drive))
    return drives
    
'''
#   Runs when a drive is inserted, (runs the sync)
def onDriveInsertion(driveLetter):                  
    sync = isSyncEnabled(driveLetter)
    if sync:
        print(parseInstructions(driveLetter))
        
    return sync
'''


# Execution
print("drivesync launched")


# Start Routine
print('drivesync running start routine')



# Drive Monitor
print('drivesync now monitoring drives')

previousDrives = getDrives()
while True:
    currentDrives = getDrives(); timenow = datetime.now()
    
    # Trigger if change in system drives
    if currentDrives.__len__() > previousDrives.__len__():
        # find out which drive was inserted
        driveLetters = list( set(currentDrives) - set(previousDrives) )
        
        print("[{}] Drive(s) {} Inserted.".format(timenow.strftime("%d %b, %Y %H:%M:%S"), driveLetters))
        
        for driveLetter in driveLetters:
            # handle the event for each drive
            
            if isSyncEnabled(driveLetter) == False:
                break;
            
            theScript = r"{}:\\syncexec.bat".format(driveLetter)

            # ensure the instruction will run on the target drive, by changing this script's working directory
            absolute_path = os.path.abspath(theScript)
            directory = os.path.dirname(absolute_path)
            os.chdir(directory)
            
            subprocess.call(theScript)
            
            
            # done handling drive
    
    # Run on drive removal
    if currentDrives.__len__() < previousDrives.__len__():
        driveLetters = list( set(previousDrives) - set(currentDrives) );
        print("[{}] Drive(s) {} Removed.".format(timenow.strftime("%d %b, %Y %H:%M:%S"), driveLetters))
    
    time.sleep(1) # my default = 1 sec
    previousDrives = currentDrives


# Close Program
print('drivesync closing')
sys.exit(0)


