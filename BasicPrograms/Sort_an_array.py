def SortArray(array):
    
    # i=0
    # while i < len(array):
    #     j=0
    #     while j < len(array):
    #         if array[i]<array[j] and i<j:
    #             x=array[i]
    #             array[i]=array[j]
    #             array[j]=x
    #         j+=1
    #     i+=1
    
    # i=0
    # while i < len(array)/2:
    #     x=array[i]
    #     array[i]=array[-1-i]
    #     array[-1-i]=x
    #     i+=1

    for i in range(0,len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                print(f"{i}--{j}--swapped--{array[i]}--{array[j]}")
                x=array[i]
                array[i]=array[j]
                array[j]=x
        print (f"{i}th pass")
        print (array)
    
    return array

def FindAllIndexes(array,value):
    index = []
    i=0
    while i<len(array):
        if array[i]==value:
            index.append(i)
        i+=1
    return index

def SearchInArray(array,value):
    present = ''
    x = FindAllIndexes(array,value)

    if x != []:
        present = 'This element is present in this array.'
    else:
        present = 'This element is not present in this array.'
    
    return present
# def FindANum(upper_limit, lower_limit, value): 

def BinarySearch(array,value):
    x=(len(array)-1)//2
    index=0
    i=0
    while i<len(array):
        if array[x]==value:
            index=x
            break
        else:
            if x > array.index(value):
                x=(len(array)-x)/2
            if x < array.index(value):
                x=x/2
        i+=1
    return index

# testcase = [4,5,88,77,3,6,9,10,77]
testcase = [9,2,4,5]
print(SortArray(testcase))

#testcase = [4,5,88,77,3,6,9,10,77]
#print(FindAllIndexes(testcase, 77))

#testcase = [4,5,88,77,3,6,9,10,77]
#print(SearchInArray(testcase, 3))

#testcase = [4,5,88,77,3,6,9,10,77]
#print(BinarySearch(testcase, 6))