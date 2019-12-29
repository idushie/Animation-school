import os

myDir = "/net/homedirs/rvolodin/data/files"

print os.listdir(myDir) # returns []
print os.listdir('.') # prints all content in the current folder (where this file lives)

fileFullPath = os.path.join(myDir, 'someFile.py') # returns updated path
subfolder = os.path.join(myDir, 'newFolder')

# check if it's a file
if os.isfile(fileFullPath):
    pass # do something with the file

# relative paths also work
print os.isfile('./someFile.txt')

# check if it's a folder
if os.path.isdir(subfolder):
    pass # do something with the dir

# absolute path to the current file (where this code is written)
thisFile = os.path.abspath(__file__)
thisDir = os.path.dirname(thisFile)

# check if path exists
print os.path.exists(myDir)

# OTHER useful commands

p = '/net/homedirs/rvolodin/data/files/myPlugin.py'

print os.path.basename(p)
# out: myPlugin.py

print os.path.commonprefix(['/net/homedirs/folderB/myPlugin.py', '/net/homedirs/FolderA/myPlugin.py'])
# out: /net/homedirs/

print os.path.dirname(p)
# out: /net/homedirs/rvolodin/data/files/

print os.path.getsize(p)
# out: 1520 bytes

print os.path.join('net', 'homedirs', 'rvolodin', 'text.txt')
# out: net/homedirs/rvolodin/text.txt

print os.path.split(p)
# out: ('/net/homedirs/rvolodin/data/files', 'myPlugin.py')

print os.path.splitext(p)
# out: ('/net/homedirs/rvolodin/data/files/myPlugin', '.py')


"""========================================================================================================
os.walk(path) - получить список всех файлов, директорий (а так же их внутренний список) для указанного пути
"""


p = '/net/homedirs/rvolodin/sandbox/shit/testProject'
import os

#get list of files and folders inside some path

for dirpath, dirnames, filenames in os.walk(p):
    print dirpath
    print dirnames
    print filenames

    #if we want to print just top folder list - we need to use break
    #break

""" out:
        /net/homedirs/rvolodin/sandbox/shit/testProject #path
        ['newFolder']    #inner folders
        ['__init__.py', '__main__.py', 'test.py', 'temp.py', 'myPlugin.py'] #files
        /net/homedirs/rvolodin/sandbox/shit/testProject/newFolder #inner folder
        []    #inner folders in this folder "newFolder"
        ['test.txt']  #inner files in this folder "newFolder"
"""

# More hacker way
(_, _, filenames) = os.walk(p).next()
print filenames #will print ['__init__.py', '__main__.py', 'test.py', 'temp.py', 'myPlugin.py']