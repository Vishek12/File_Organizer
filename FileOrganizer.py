import os 
import shutil

"""This is a file organzier that takes a destination on your machine and organizes the directory based """


"""Get the destination path and save the files in the destination"""
destination = input("Enter the path: ")
files = os.listdir(destination)

"""Loop through all of them """

for file in files: 

    file_name, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(destination+'/'+extension):
        shutil.move(destination+'/'+file, destination+'/'+extension+'/'+file)

    else: 
        os.makedirs(destination+'/'+extension)
        shutil.move(destination+'/'+file, destination+'/'+extension+'/'+file)