def swap(elements,start,end):
    elements[start],elements[end]=elements[end],elements[start]
    
def partition(elements,start,end):
    pivot_index=start
    pivot=elements[start]
    while start<end:
        while start<len(elements) and elements[start]<=pivot:
            start+=1
        while elements[end]>pivot:
            end-=1
        if start<end:
            swap(elements,start,end)
        swap(elements,pivot_index,end)
        return end

def quicksort(elements,start,end):
    if start<end:
        pi=partition(elements,start,end)
        quicksort(elements,start,pi-1)
        quicksort(elements,pi+1,end)
elements=[11,7,2,9,29,28,15]
quicksort(elements,0,len(elements)-1)
print(elements)
