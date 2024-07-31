import os
import shutil
import sys

data_path = r"C:\Users\ravig\OneDrive\Desktop\python-projects\Animals"
data_path_list = os.listdir(data_path)

for i in data_path_list:
    folder_path = os.path.join(data_path,i)
    folder_path_list = os.listdir(folder_path)
    for j in folder_path_list:
        new_name = j.split("_")[1]
        new_name = i + "_" + new_name
        old_image_path =  os.path.join(folder_path,j)
        new_image_path = os.path.join(folder_path,new_name)
        os.rename(old_image_path,new_image_path)


        
