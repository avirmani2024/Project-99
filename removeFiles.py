import os
import shutil
import time 
import stat




def main():
    path = input("Enter the name of directory to be sorted:")
    days = 30
    deleted_folders_count = 0
    deleted_files_count = 0 
    seconds = time.time() - (days * 24 * 60 * 60)

    
    if os.path.exists(path):


        for root_folders, folders, files in os.walk(path):

            if seconds >= getFileOrFolderAge(root_folders):
                removerFolder(root_folders)
                deleted_folders_count += 1
                break

            else: 
                for folder in folders: 
                    folder_path = os.path.join(root_folders, folder)
                    if seconds >= getFileOrFolderAge(folder_path):
                        removerFolder(folder_path)
                        deleted_folders_count += 1
        

                for file in files:
                    file_path = os.path.join(root_folders, files)
                    if seconds >= getFileOrFolderAge(file_path):
                        removerFiles(file_path)
                        deleted_files_count += 1

            
        else:

            if seconds >= getFileOrFolderAge(path):
                removerFiles(path)
                deleted_files_count += 1
                
    else:
        print("Path not found")

    

def removerFolder(path):

    if not os.remove(path):
        print("Path deleted")

    else:
        print("Removal unsccefull")

def removerFiles(path):

    if not os.remove(path):
        print("Path deleted")

    else:
        print("Removal unsccefull")



def getFileOrFolderAge():
    ctime = os.stat(path).st_ctime

    return ctime


def remove_folder(path):

	if not shutil.rmtree(path):

		
		print(" Removal successfull")

	else:

		
		print("Unable to delete")


if __name__ == '__main__':
    main()





        
        
        




