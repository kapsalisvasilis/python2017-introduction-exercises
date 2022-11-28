def binarysearchrec(lst, key, low, high):

    if low>high:

        return -1

    else:

        mid=(low+high)//2

        if key==lst[mid]:

            return mid

        elif key<lst[mid]:

            return binarysearchrec(lst, key, low, mid-1)

        else:

            return binarysearchrec(lst, key, mid+1, high)

 

l=[1,2,3,4,5,6,7,8,9]

print(binarysearchrec(l,2,2,8))
