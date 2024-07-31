import shutil
import os
import dataset

source1 = open(r"C:\Users\ravig\OneDrive\Desktop\python-projects\dataset\Animals")
print(source1)
source2 = list[source1]
for i in source2:
    for x in i:
        list1=[x]
    if (list1=="jpg."):
        os.rename(r"C:\Users\ravig\OneDrive\Desktop\python-projects\dataset\Animals",
                  "C:\Users\ravig\OneDrive\Desktop\python-projects\dataset\Animalsnew")
