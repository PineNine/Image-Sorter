# Had a image sorted that i made but decided to make new from scratch
# really messy stuff going on and hope to clean it up a bit in the future
# still a beginner in python soooo ya

import os
import pathlib
import shutil
import datetime as dt

# needs an unorganized folder to be able to organized the photos
PATH = os.getcwd() + "\\UNORDER"
CWD_PATH = os.getcwd()

#could add more raw file extensions
raw_ext = (".NEF")

for dirPath, dirNames, fileNames in os.walk(PATH):
    for a in fileNames:
        cwFile = str(dirPath + "\\" + a)
        b = os.path.getmtime(cwFile)

        modTime = str(dt.datetime.fromtimestamp(b))[:10]
        extFile = pathlib.Path(cwFile).suffix
        newPath = str(CWD_PATH + "\\" + modTime)

        if not os.path.exists(newPath):
            os.mkdir(newPath)
            print("Made new Directory at: \n", newPath)
            print("-" * 50)
        if extFile in raw_ext:
            if not os.path.exists(newPath + "\\RAW"):
                os.mkdir(newPath + "\\RAW")
                print("Made new RAW Directory in: \n", newPath )
                print("-" * 50)
            shutil.move(cwFile, newPath + "\\RAW")
            print(f"Moved {a} into {newPath}")
        else:
            shutil.move(cwFile, newPath)
            print(f"moved {a} into: {newPath}")