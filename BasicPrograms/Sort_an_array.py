# This code will return you a sorted array (which means the array will be organized in ascending  order).

def SortArray(array):
    
    i=0
    while i < len(array):
        j=0
        while j < len(array):
            if array[i]<array[j] and i<j:
                x=array[i]
                array[i]=array[j]
                array[j]=x
            if array[i]>array[j] and i>j:
                x=array[i]
                array[i]=array[j]
                array[j]=x
            j+=1
        i+=1
    
    i=0
    while i < len(array)/2:
        x=array[i]
        array[i]=array[-1-i]
        array[-1-i]=x
        i+=1
    
    return array

def SearchIndex_in_Array(array,value):
    index = array.index(value)
    return index

testcase = [4,5,88,77,3,6,9,10,88]
print(SortArray(testcase))

testcase = [4,5,88,77,3,6,9,10,88]
print(SearchIndex_in_Array(testcase, 77))