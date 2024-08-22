def fn(list,target):
    for i in list:
        if (i==target):
            print(f"{target} is in the list")
        else:
            print("The num is not in list")
x = [1,2,3,4,5,68,5,7,4,]
y = 68
fn(x,y)
