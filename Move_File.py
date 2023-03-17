import os;
import shutil

from_dir = "/Users/sunny/Desktop/Sunny/Folder"
to_dir = "/Users/sunny/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file_name in list_of_files:

    name, extention = os.path.splitext(file_name)
    # print(name)
    # print(extention)

    if extention == '':
        continue
    if extention in ['.txt', '.doc', '.docx','.pdf']:
        path1= ""

        path1 = from_dir + '/' + file_name                             
        path2 = to_dir + '/' + "Image_Files"                        
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name   

        
        if os.path.exists(path2):
          print("Moving " + file_name + ".....")


          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)