import os

print(os.getcwd())

# we can't read and write a file at the same time - it helps to use tempfile in this case
import tempfile

print(tempfile.gettempdir())

print(os.listdir())

print(os.path.exists('c:\\Users'))

print(os.path.isdir('c:\\Users'))

# Homework: write a program that scans any folder and should return the information
# about the total size of this folder
