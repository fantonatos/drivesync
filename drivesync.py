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
    
    return sync

# Execution
print("drivesync launched")


# Start Routine
print('drivesync running start routine')


# Drive Monitor
print('drivesync now monitoring drives')

previousDrives = getDrives()
while True:
    currentdrives = getDrives()
    
    if DEBUG:
        print(str(currentdrives) + " testing against last iteration")
    
    # Run on drive insertion
    if currentdrives.__len__() > previousDrives.__len__():
        print("Drive(s) Inserted.")
        
    # Run on drive removal
    if currentdrives.__len__() < previousDrives.__len__():
        print("Drive(s) Removed.")
    
    time.sleep(1)
    previousDrives = currentdrives
    
    

# Close Program
print('drivesync closing')
sys.exit(0)


