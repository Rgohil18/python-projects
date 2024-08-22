def Max_product(array):
    for i in array:
        for y in array:
            array = [i*y]
            print("largest product is",max(array))

list1 = [1,2,3,4,5]
Max_product(list1)
