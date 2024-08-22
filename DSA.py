
def two_sum(list,target):
    for i in list:
        for o in list:
            if (i+o==target):
                print(i,o)
x = [1,2,3,4,5]
y = 5
two_sum(x,y)
