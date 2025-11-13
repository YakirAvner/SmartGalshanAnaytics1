import os
import shutil
import glob
import argparse


def copy_db_file(source_folder, dataBaseFolder):
    if not os.path.isdir(dataBaseFolder):
        os.makedirs(dataBaseFolder)
    db_files = glob.glob(os.path.join(
        source_folder, '**', 'Galshan*.db'), recursive=True)

    # Copying SqLite DBs to a different folder:
    for file in db_files:
        dt = os.path.basename(os.path.dirname(os.path.dirname(file)))
        new_file_name = f"Galshan_{"-".join(dt.split('-')[::-1])}.db"
        shutil.copy(file, os.path.join(dataBaseFolder, new_file_name))
        print(f"Copied {new_file_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source_folder")
    parser.add_argument("--dataBaseFolder")
    args = parser.parse_args()
    source_folder = args.source_folder
    dataBaseFolder = args.dataBaseFolder
    print(f"source_folder: {source_folder}")
    print(f"dataBaseFolder: {dataBaseFolder}")
    copy_db_file(source_folder, dataBaseFolder)
