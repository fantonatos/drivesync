from datetime import datetime
from os.path import exists
from sys import exit
import time

'''
    Fotis Antonatos
    24 Sep, 2019
    
    Last Modified: 25 Sep, 2019
    
'''

# Data

#           look for drives with the id "debug1" inside the drivesync.inf file
#           "documents" is a built-in link to the user's documents library
test_commands = [   "sync debug1 with directory documents" 
                    "sync debug2 with subdirectory .../Pictures/SummerVacation1999"]
test_drive = "G"

DEBUG = False


# Functions

# Returns true if drive is set up for sync
def isSyncEnabled(driveLetter):
    if exists(driveLetter + ':\\drivesync.inf'):
        return True
    return False

# Returns list of all drives on the system
def getDrives():
    drives = []
    for drive in range(ord('A'), ord('Z') + 1):
        if exists(chr(drive) + ':'):
            drives.append(chr(drive))
    return drives

def onDriveInsertion(driveLetter):
    sync = isSyncEnabled(driveLetter)
    #if sync:
    #    file = open(driveLetter + ":\\drivesync.inf", "r")      
        
    return sync

# Execution
print("drivesync launched")


# Start Routine
print('drivesync running start routine')


# Drive Monitor
print('drivesync now monitoring drives')

previousDrives = getDrives()
while True:
    currentDrives = getDrives(); timenow = datetime.now()
    
    if DEBUG:
        print("Testing current drives {} against previous drives {}".format(currentDrives, previousDrives))
    
    # Run on drive insertion
    if currentDrives.__len__() > previousDrives.__len__():
        # Find out which drive was inserted
        driveLetters = list( set(currentDrives) - set(previousDrives) );
        print("[{}] Drive(s) {} Inserted.".format(timenow.strftime("%d %b, %Y %H:%M:%S"), driveLetters))
        
        # for now we assume only one drive was inserted
        print("Running Sync: {} {}".format(driveLetters[0], onDriveInsertion(driveLetters[0])))
        
    # Run on drive removal
    if currentDrives.__len__() < previousDrives.__len__():
        driveLetters = list( set(previousDrives) - set(currentDrives) );
        print("[{}] Drive(s) {} Removed.".format(timenow.strftime("%d %b, %Y %H:%M:%S"), driveLetters))
    
    time.sleep(1)
    previousDrives = currentDrives
    
    

# Close Program
print('drivesync closing')
sys.exit(0)


