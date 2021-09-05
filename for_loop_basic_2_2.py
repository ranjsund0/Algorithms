
def biggie(list):
    for i in range(len(list))
        if list[i] > 0:
            list[i] = "big"
    return list
print(biggie([-1,3,5,-5]))

def positive(nlist):
    count = 0
    for i in range(len(nlist)):
        if nlist[i] > 0:
            count += 1
        nlist[len(nlist)-1] = count
    return nlist

print(positive([-1,1,1,1]))

def sum_total(slist):
    sum = 0
    for i in range(len(slist)):
        sum += slist[i]
    return sum
print(sum_total([1,2,3,4]))

def average(alist):
    sum = 0
    for i in range(len(alist)):
        sum += alist[i]
    return sum/len(alist)
print(average([1,2,3,4]))
    

def length(llist):
    return len(llist)

def minimum(mlist):
    if len(mlist) == 0
        return  false
    else:
        min = mlist[0]
        for i in range(len(mlist)):
        if mlist[i] < min
            min = mlist[i]
        return min

def maximum(maxlist):
    if len(maxlist) == 0
        return false
    else:
        max = maxlist[0]
        for i in range(len(maxlist))):
        if maxlist[i] > max
            max = maxlist[i]
        return max
    
def ultimate(ulist):
    sum = sum_total(ulist)
    avg = average(ulist)
    min = minimum(nums_list)
    max = maximum(ulist)
    len = length(ulist)
    analysis = {
        'sum_total': sum,
        'average': avg,
        'maximum': max,
        'minimum': min,
        'length': len
    }
    return analysis

def rev(rlist):
    list_len =len(rlist)
    for i in range(int(list_len/2)):
        temp = rlist[list_len-1-i]
        rlist[rlist-1-i] = rlist[i]
        rlist[i] = temp
    return rlist
print(rev([37,2,1,-9]))