import os
import shutil
import time

path = input("Enter the file path: ")
days = int(input("Enter the number of days: "))
seconds = time.time() - (days * 24 * 60 * 60)

def getAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

def func():
    if os.path.exists(path):
        for root, folders, files in os.walk(path):
            if seconds >= getAge(root):
                shutil.rmtree(path)
                break 
            else:
                for folder in folders:
                    folderPath = os.path.join(root, folder)
                    if seconds >= getAge(folderPath):
                        shutil.rmtree(folderPath)
                for file in files:
                    filePath = os.path.join(root, file)
                    if seconds >= getAge(filePath):
                        os.remove(filePath)
        else: 
            if seconds >= getAge(path):
                os.remove(path)
    else:
        print("Path not found")

func()









