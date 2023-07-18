import os
from pathlib import Path
import time
import json
from pymongo import MongoClient
from flask import Flask,jsonify
from dotenv import load_dotenv


load_dotenv()
# def userDirFile():
#     path = input("Please enter the path to files: ")
# #     file = input("Please enter the file names with appropriate extension with comma ")
# #     fileNew = list(file)
# #     # Check the operating system
#     if os.name == 'nt':  # Windows
#         path = path.replace('/', '\\').replace('\\', '\\\\')
#         path.replace(' ', '')

#     else:
#         path = path.replace(' ', '')
    
#     return path


def readDirFileLocation(file):
    # path = userDirFile()
    path = os.getcwd()
    # dir = os.path.isdir(path)
    if not os.path.isdir(path):  # if path is not  valid
        print("Please enter the valid directory")
    else:
        result = []        
        # for each in os.scandir(path):
        for each in Path(path).iterdir():  #two operation found in os module scadr and iterddir fro Path module, tried both, iter module seems to be givig the path with file name to process further.
            if each.is_file() and each.name in file:   #Checking whether the file name and it is file matches
                result.append(str(each))
            # else:
            #     raise "Configuration file not found, please check these two files exist and provide variable input as ['file1.ext', 'file2.ext'] "
            # # if each.name == file and each.is_file():
        return result
# print(readDirFileLocation(['server.yml','database.yml']))





def extractdata(file):
    try:
        database, server = readDirFileLocation(file)
    except: 
        raise print({f"An error occurred while reading the file:. Please check the name and extension of the file and use http://127.0.0.1:5000/getData/[filename.extension,filename2.extension] format to process both files."})
             #  print(database, server)
    finalDatabaseDict = {}
    finalServerDict = {}
    with open(database, 'r') as f:     
        for each in f:  # Readinge ach in line from result
            # print(each)
            if '=' in each:    #if = is there , we could have replace with any fucntion
                key, value = each.strip().split('=')  # We are stripping and rmeoving any content and splitting based on special variable
                finalDatabaseDict[key] = value # appendig the value to dictionary
                continue
            else:
                pass 
    with open(server, 'r') as f:
        for each in f:
            # print(each)
            if '=' in each:
                key, value = each.strip().split('=')
                finalServerDict[key] = value
                continue
            else:
                pass
    return [finalDatabaseDict, finalServerDict]
# print(extractdata(['server.yml','database.yml']))

def getJSON(file):
    finalDatabaseDict, finalServerDict = extractdata(file)     
    client = MongoClient(os.environ.get('MONGO_URI'))
    db = client['PythonAssignment']
    database = db['databaseCred']  #creating collection databasecred and itsobject
    server = db['serverCred']   # creating collection server servercre and its object

    databaseJSON = json.dumps(finalDatabaseDict)  #Loading data in to json format
    serverJSON = json.dumps(finalServerDict)

    database.insert_one(finalDatabaseDict)  #Inserting the data as json format
    server.insert_one(finalServerDict)

    return f"Database: \n{databaseJSON} \n Server: \n {serverJSON}"
 
# print(getJSON(['databas.yml','server.yml']))

# def getData(file):
#     databaseJSON, serverJSON = getJSON(file)

#     for key,value in databaseJSON.items():
#         print(f" {key}:{value}")
    
#     for key,value in serverJSON.items():
#         print(f"{key}:{value}")



     # extracting teh data from dict and storing in json format using pymomgo, json and creating object these classes

# print(getJSON(['server.yml','database.yml']))

# def get_data(file):
#     app=Flask(__name__)

    







# print(userDirFile())
# path, file = userDirFile()
# print(f"Path: {path}")
# print(f"File: {file}")