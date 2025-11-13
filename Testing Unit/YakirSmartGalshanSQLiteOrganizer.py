from pathlib import Path
from tkinter import Tk, filedialog
import os
import shutil
import glob
import argparse

# Folder Explorer Selector Method:


def FolderExplorer():
    root = Tk()
    root.withdraw()
    folderNameSelector = filedialog.askdirectory(
        initialdir=Path.home(), title="Select a Folder")
    path = Path(folderNameSelector)
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    return (path)


# The folder where I want to find the db file.

source_folder = FolderExplorer()

# The destination of the db file.

destination_file = FolderExplorer()
dbFolderName = input("Enter a db folder name for db file containment: ")
dataBaseFolder = destination_file / dbFolderName
dataBaseFolder.mkdir(parents=True, exist_ok=True)


# Copying SqLite DBs to a different folder:

for file in source_folder.rglob("Galshan.db"):
    dt = os.path.basename(os.path.dirname(os.path.dirname(file)))
    new_file_name = f"Galshan_{"-".join(dt.split('-')[::-1])}"
    shutil.copy(file, os.path.join(dataBaseFolder, new_file_name))
    print(f"Copied {new_file_name}")


# try:
#         shutil.copy(file, dataBaseFolder)
#         print(f"Copied {file.name}, (from->{file.name}) to {dataBaseFolder}")
#     except PermissionError:
#         print(f"Permission denied: Skipped {file}, it's locked | read-only!!!")
#     except Exception as e:
#         print(f"Skipped {file}: {e}")


# flag = False
# for folder in source_folder.iterdir():
#     if folder.is_dir():
#         for folder2 in folder.iterdir():
#             for file in folder2.iterdir():
#                 if file.suffix == ".db":
#                     flag = True
#                     print(f"Found DB: {file.name} in {folder.name}")
#                     shutil.copy(file, dataBaseFolder)
#                     print(
#                         f"The file {file.name} is copied in {dataBaseFolder}")
# if not flag:
#     print("No DB has been found!!!")
