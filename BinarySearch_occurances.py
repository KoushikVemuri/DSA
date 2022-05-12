
################### PROBLEM #######################
# Problem: Find index of all the occurances of a number from sorted list
# Solution here tries to find an index of a number using binary search. Now since the list is sorted,
# it can do left and right scan from the initial index to find all occurances of a given element
# This method is not most efficient and I want you to figure out even a better way of doing it. In
# any case below method is still effective


def binary_search(num, num_tofind, left_index, right_index):
    if left_index > right_index:
        return -1
    
    mid_index = left_index+ right_index//2
    mid_number = num[mid_index]
    
    if mid_number == num_tofind:
        leftofMid = mid_index-1
        rightofMid = mid_index +1
        num_indices = [mid_index]
        while num_tofind== num[leftofMid]:
            num_indices.append(leftofMid)
            leftofMid-=1
            
        while num_tofind== num[rightofMid]:
            num_indices.append(rightofMid)
            rightofMid+=1
            
        return num_indices
    
    if mid_number > num_tofind:
        right_index = mid_index-1
        
    if mid_number < num_tofind:
        left_index = left_index + 1

    return binary_search(num,num_tofind, left_index, right_index)
    


numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
num_tofind = 44
print("the index of the number to find is", binary_search(numbers, num_tofind,0,len(numbers)-1))
