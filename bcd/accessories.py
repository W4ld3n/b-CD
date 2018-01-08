import os
import os.path
import random

#This is the source of your music directory
music_dir = "/media/malte/mybook4/Music"

barcode_mapping = "./barcode_mapping.tsv"
def listDirs():
    for dirpath, dirs, files in os.walk():
        print dirpath


def barcodeDirs():
    dirs = []
    try:
        for x in os.walk(music_dir):
            dirpath = x[0]
            if (os.path.isfile(dirpath + "/barcode")):
                dirs.append(dirpath)
    except Exception as e:
        print "Fail"

    return dirs

def readBarcode(path):
    f = open(path, "r")
    return f.read().strip()

def createBarcodeMapping():
    f = open(barcode_mapping,"w")
    dirs = barcodeDirs()
    for dirpath in dirs:
        f.write(readBarcode(dirpath + "/barcode") + "\t" +dirpath + "\n")
    f.close()

def loadBarcodeMapping():
    with open(barcode_mapping) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    mapping = {}
    for line in content:
        line = line.split("\t")
        mapping[line[0].strip()] = line[1].strip()

    return mapping

def listFiles(mypath):
    try:
        #print os.listdir(mypath)
        onlyfiles = []
        for f in os.listdir(mypath):
            completePath = os.path.join(mypath, f)
            #Check for supported formats
            if os.path.isfile(completePath):
                if(any (ext in completePath for ext in [".ogg",".mp3",".wav","wma"])):
                    #print "File: " + completePath
                    onlyfiles.append(completePath)
            elif os.path.isdir(completePath):
                #print "Dir: " + completePath
                onlyfiles.extend(listFiles(completePath+"/"))
        return onlyfiles
    except Exception as e:
        print "Failed to list Songs"
        return []



def chooseSong(path):
    try:
        while True:
            files = listFiles(path)
            r = random.randrange(0,len(files)-1)
            f = files[r]
            return f
    except Exception as e:
        print "Failed to choose Song"

def barcodeByDir(path):
    mapping = loadBarcodeMapping()
    for key in mapping:
        if mapping[key] == path:
            return key
    return ""

def randomSong():
    mapping = loadBarcodeMapping()
    files = mapping.values()
    r = random.randrange(0,len(files)-1)
    f = files[r]
    s = chooseSong(f)
    return [s,barcodeByDir(f)]
