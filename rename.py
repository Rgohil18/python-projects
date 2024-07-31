import os 
import sys
import glob
import shutil

dataset_path = r'/Users/vijayrajgohil/Desktop/python_ravi/Animals'

folder_list = os.listdir(dataset_path)

for i in folder_list:

    image_list_path = os.path.join(dataset_path, i)

    image_list = os.listdir(image_list_path) 

    for j in image_list:

        new_name = j.split('_')[1] 
        new_name  = i + '_' + new_name

        old_name_path = os.path.join(image_list_path,j)

        new_name_path = os.path.join(image_list_path, new_name)

        os.rename(old_name_path, new_name_path)

        


    






    

