import os

# print(os.getcwd())
# os.chdir('/Users/Charles/Desktop')
# print(os.getcwd())

# os.mkdir("New Folder")
# os.rmdir("New Folder")
# os.mkdir("Dir1/Dir2") ### can not handle sub-folder
# os.makedirs("Dir1/Dir2") ### can handle sub-folder
# os.removedirs("Dir1/Dir2")

# os.rename("New Folder", "test")

# print(os.listdir())


for dirpath, dirnames, filenames in os.walk("/Users/Charles/Documents"):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)