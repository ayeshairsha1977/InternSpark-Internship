import os
import shutil
import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
# files types
file_types= {
    "Movies":[".mp4",".mkv"],
    "Musics":[".mp3"],
    "Documents":[".pdf",".docx",".txt"],
    "Images":[".png",".jpg",".jpeg"]
}
def add_file():
    source=input("Enter file name or full path:")
    destination_folder=input("Enter Destination Folder:")
    if not os.path.isabs(source):
        source=os.path.abspath(source)
    if not os.path.exists(source):
        print("file doesn't exist")
        return 
    if not os.path.exists(destination_folder):
        print("Destination Folder doesn't exist")
        return 
    try:
        file=os.path.basename(source)
        destination=os.path.join(destination_folder,file)
        shutil.move(source,destination)
        print(f"Move {file} to {destination_folder}")
        logging.info(f"Move {file} to {destination_folder}")
    except Exception as e:
        print("Error:",e)
        logging.error(str(e))

def rename_file():
    source=input("Enter full file path:")
    old_name=os.path.basename(source)
    new_name=input("Enter new file name:")
    if not os.path.exists(source):
        print("Path does not exist")
        return
    folder=os.path.dirname(source)
    new_path=os.path.join(folder,new_name)
    if os.path.exists(new_path):
        print("file name already exit!")
        return
    try:
        os.rename(source,new_path)
        print("file renamed Succesfullly")
        logging.info(f"renamed {old_name} to {new_name}")
    except Exception as e:
        print("Error:",e)
        logging.info(str(e))

def delete_file():
    source=input("Enter file path:")
    if not os.path.exists(source):
        print("Path does not exists")
        return 
    confirm=input("Are you sure?(yes/no):")
    if confirm.lower()=="yes":
        os.remove(source)
        print("Succesfully deleted the file")
        logging.info(f"{os.path.basename(source)} is deleted successfully!")
    else:
        print("Deleted operation Cancelled")


    

def organize_files(path):
    # checking folder path exit
    if not os.path.exists(path):
        print("Folder does not exits")
        return 
    files=os.listdir(path)
    for file in files:
        file_path=os.path.join(path,file)
        if os.path.exists(file_path):
            extension=os.path.splitext(file)[1].lower()
            for folder,extensions in file_types.items():
                if extension in extensions:
                    folder_path=os.path.join(path,folder)

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    destination=os.path.join(folder_path,file)
                    try:
                        shutil.move(file_path,destination)
                        print(f"Moved {file} to {folder}")
                        logging.info(f"Moved {file} to {folder}")
                    except Exception as e:
                        print("Error:",e)
                        logging.error(str(e))

def show_statistics():
    source=input("Enter folder path:")
    if not os.path.exists(source):
        print("Folder does not exists.")
        return
    folders=os.listdir(source)
    total_files=0
    print("="*4+"Folder Statics"+"="*4)
    for folder in folders:
        folder_path=os.path.join(source,folder)
        if os.path.isdir(folder_path):
            files=os.listdir(folder_path)
            file_count=len(files)
            total_files+=file_count
            print(f"{folder} : {file_count}" )
    print(f"Total files: {total_files}" )

while True:
    print("\n======FILE AUTOMATION TOOL======")
    print("1. Add File")
    print("2. Rename File")
    print("3. Delete File")
    print("4. Organize Files")
    print("5. Show Folder Statistics")
    print("6. Exit")
    choice=input("Enter your Choice:")
    match choice:
        case "1":
            add_file()
        case "2":
            rename_file()
        case "3":
            delete_file()
        case "4":
            path=input("Enter folder path:")
            organize_files(path)
        case "5":
            show_statistics()
        case "6":
            print("Termination program....")
            break
        case _:
            print("Invalid choice")
