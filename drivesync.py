from os.path import exists
import time

'''
    Fotis Antonatos
    24 Sep, 2019
    
'''

# Data

#     look for drives with the id "debug1" inside the drivesync.inf file
#     "documents" is a built-in link to the user's documents library
commands = [ "sync debug1 with directory documents" 
            "sync debug2 with subdirectory .../Pictures/SummerVacation1999"]


# Functions

# Returns true if drive is set up for sync
def isSyncEnabled(driveLetter):
    if exists(driveLetter + ':\\drivesync.inf'):
        return True;
    return False;

# Returns list of all drives on the system
def getDrives():
    drives = []
    for drive in range(ord('A'), ord('Z') + 1):
        if exists(chr(drive) + ':'):
            drives.append(chr(drive))
    return drives

def onDriveInserted(driveLetter):
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
    print(currentdrives)
    
    # Run on drive insertion
    if currentdrives.__len__() > previousDrives.__len__():
        print("Drive(s) Inserted.")
        
    # Run on drive removal
    if currentdrives.__len__() < previousDrives.__len__():
        print("Drive(s) Removed.")
        
    time.sleep(1)
    previousDrives = currentdrives;
    
    

# Close Program
print('drivesync closing')
exit();

