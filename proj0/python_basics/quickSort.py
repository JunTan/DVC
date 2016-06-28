def myquickSort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [x for x in lst if x < pivot]
    large = [x for x in lst if x > pivot]
    return myquickSort(less) + [pivot] + myquickSort(large)

def quickSort(lst):
    if len(lst) <= 1: 
        return lst
    smaller = [x for x in lst[1:] if x < lst[0]]
    larger = [x for x in lst[1:] if x >= lst[0]]
    return quickSort(smaller) + [lst[0]] + quickSort(larger)

# Main Function
if __name__ == '__main__':    
    lst = [2,4,5,1]
    print quickSort(lst)    
    