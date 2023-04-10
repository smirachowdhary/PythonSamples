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

def FindAllIndexes(array,value):
    index = []
    i=0
    while i<len(array):
        if array[i]==value:
            index.append[i]
    return index

def SearchInArray(array,value):
    present = ''
    x = FindAllIndexes(array,value)

    if x != []:
        present = 'This element is present in this array.'
    else:
        present = 'This element is not present in this array.'
    
    return present

testcase = [4,5,88,77,3,6,9,10,77]
print(SortArray(testcase))

testcase = [4,5,88,77,3,6,9,10,77]
print(FindAllIndexes(testcase, 77))

testcase = [4,5,88,77,3,6,9,10,77]
print(SearchInArray(testcase, 3))