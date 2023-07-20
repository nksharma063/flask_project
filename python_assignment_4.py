import os
from pathlib import Path
import time
import subprocess
import shutil
import sys


def getDir(source,destination):
    sourcePath= Path(source)
    destinationPath= Path(destination)
    if  os.name == 'nt': 
        # sourcePath = source.replace('/','\\')
        # sourcePath = source.replace(' ', '')
        # destinationPath = destination.replace('/','\\')
        # destinationPath = destination.replace(' ','')
        if not os.path.isdir(sourcePath):
            print("Please enter the valid source directory")
        elif not os.path.isdir(destinationPath):
            print("Please enter the valid destination directory")

    else:
        sourcePath = source.replace(' ','')
        destinationPath = destination.replace(' ','')
        if not os.path.isdir(sourcePath):
            print("Please enter the valid source directory")
        elif not os.path.isdir(destinationPath):
            print("Please enter the valid destination directory")

    # if not os.path.isdir(source):
    #     print("Please enter the valid source directory")
    # elif not os.path.isdir(destination):
    #     print("Please enter the valid destination directory")

    return sourcePath, destinationPath


def addingTimestamp(source, destination):
    source,destination = getDir(source,destination)

    for each in os.scandir(source):
        if each.is_file():
            filename, file_extension = os.path.splitext(each.name)
            if os.path.exists(os.path.join(destination, each.name)):
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                new_filename = f"{filename}_{timestamp}{file_extension}"
                shutil.copy2(each.path, os.path.join(destination, new_filename))
            else:
                shutil.copy2(each.path, os.path.join(destination, each.name))

    return "Congratulation, you have copied file, but please check and verify once to make sure that script is working fine or not"    

if __name__ == "__main__":
    print("Usage:python backup.py <D:\\DevOps_HerVired\\testsource> <D:\\DevOps_HerVired\\testdestination> format because pyhton interpret as backslash")
    if len(sys.argv) != 3:
        print("Usage:python backup.py <D:\\DevOps_HerVired\\testsource> <D:\\DevOps_HerVired\\testdestination> format because pyhton interpret as backslash")
        sys.exit(1)
    else:
        print(sys.argv[1])
        print(sys.argv[2])
        source = sys.argv[1]
        destination = sys.argv[2]
    
        result = addingTimestamp(source, destination)

        print(result)




# print(addingTimestamp('D:\\DevOps_HerVired\\testsource', 'D:\\DevOps_HerVired\\testdestination'))


