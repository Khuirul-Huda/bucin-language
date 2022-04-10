# Bucin Language V0.0.1
# Just for fun
import sys
import json


bucinanPath = str(sys.argv[1])
if (bucinanPath == "" ): print("Usage: bucin <filepath>")
bucinanReader = open(bucinanPath)
bucinBasicReader = open('./words/basic.json')

bucinan = bucinanReader.read()
bucinBasicDictionary = json.load(bucinBasicReader)

def bucinTransform(bucinData: str, dictionary):
    bucinCode = bucinData
    for bucinWords in dictionary:
        bucinCode = bucinCode.replace(bucinWords, dictionary[bucinWords])
    return bucinCode

def bucinExecutor(src):
    exec(src)

bucinExecutor(bucinTransform(bucinan, bucinBasicDictionary))
