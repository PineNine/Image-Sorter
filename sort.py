#still learning python and programming in general
#so everything might be janky and all over the place

#will add log later for now the print stays >:(

#SORTS PHOTOS INTO SEPERATE FOLDERS BY DATE TAKEN
#THEN SORTS RAW FILE INTO ITS ON FOLDER
import os, shutil
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS

PATHDIR = os.getcwd()
UNORGANIZED = PATHDIR + '\\UNORGANIZED'

#ignores other file types except for these
ext = (".JPG", ".NEF")
raw = (".NEF")

#checks if it is the correct file type
def is_ext(file):
    return os.path.splitext(file)[1] in ext
def is_raw(file):
    return os.path.splitext(file)[1] in raw


#folders not to go in
exclude = set(['RAW', 'DEVELOPED', 'UNORGANIZED', 'BATCH'])

#more to be added if i use different file types
filetag = {
    ".JPG": 306,
    ".NEF": 36867,
    ".MOV": 36868
}

def sort_date():
    for folderName, subfolders, filenames in os.walk(UNORGANIZED):
        subfolders[:] = [i for i in subfolders if i not in exclude]
        for filename in filenames:
            print(folderName)
            print(filename)
            
            extTag = filetag[os.path.splitext(filename)[1]]
            print(extTag)
            if is_ext(filename):
                #currentFile = str(Image.open(UNORGANIZED + '\\' + filename).getexif()[36867])
                currentFile = str(Image.open(UNORGANIZED + '\\' + filename).getexif().get(extTag))
                
                fileDate = currentFile[:10].replace(':', '-')
                print(fileDate)
                if not os.path.exists(PATHDIR +'\\' + fileDate[:10]):
                    os.makedirs(PATHDIR + '\\' + fileDate)
                shutil.move(UNORGANIZED + '\\' + filename, PATHDIR + '\\' + fileDate)


def sort_raw():
    for folderName, subfolders, filenames in os.walk(PATHDIR):
        subfolders[:] = [i for i in subfolders if i not in exclude]
        for filename in filenames:
            if is_raw(filename):
                # Creates new folder if it didn't exist
                if not os.path.exists(folderName +'\\RAW'):
                    os.makedirs(folderName + '\\RAW')
                    print()
                    print('=' * 100)
                    print('CREATED NEW DIRECTORY IN ' + folderName)
                #moves the file into the folder
                print("###" + folderName)
                shutil.move(folderName + '\\' + filename, folderName + '\\RAW')
                print('MOVED ' + filename)

#fail safe
def main():
    print("is this the correct directory (y/n)\n\n" + PATHDIR + "\n")
    x = input()
    x = x.lower()
    if x == 'y':
        sort_date()
        sort_raw()
    else:
        exit()

main()