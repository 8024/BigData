def quicksort(array):
    less = []
    greater = []
    if len(array)<=1:
        return array
    pivot = array.pop()
    for x in array:
        if x<=pivot:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less)+[pivot]+quicksort(greater)

if __name__ =="__main__":
    array = [1,3,4,3,5,5,16,34,76,87,324,76,3576,72]
    array = quicksort(array)
    print(array)
    print(list(reversed(array)))
