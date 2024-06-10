
a = [5,3,2,1,4]

def bubble_sort(l):   #bubble sort algorithm
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

bub_sort = bubble_sort(a.copy())


def selection_sort(l):   #selection sort algorithm
    for i in range(len(l)-1):
        min_idx = i
        for j in range(i+1,len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
    return l

sel_sort = selection_sort(a.copy())


def insertion_sort(l): #insertion sort algorithm
    for i in range(1,len(l)):
        x = l[i]
        for j in range(i-1,-2,-1):
            if l[j] > x:
                l[j+1] = l[j]
            else:
                break
        l[j+1] = x 
    return l

ins_sort = insertion_sort(a.copy())


def quick_sort(l): #quick sort algorithm
    def partition(low,high):
        pivot = l[high]
        i = low - 1 
        for j in range(low,high):
            if l[j] <= pivot:
                i += 1
                l[i],l[j] = l[j],l[i]
        l[i+1],l[high] = l[high],l[i+1]
        return i+1
    def qs(low,high):
        if low < high:
            pi = partition(low,high)
            qs(low,pi-1)
            qs(pi+1,high)
    qs(0,len(l)-1)
    return l

q_sort = quick_sort(a.copy())


def merge_sort(l): #merge sort algorithm
    def ms(l):
        if len(l) <= 1:
            return l
            
        mid = len(l) // 2
        left = ms(l[:mid])
        right = ms(l[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []  
        i = j = 0  
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    return ms(l)

m_sort = merge_sort(a.copy())


def bucket_sort(l):     #bucket sort algorithm
    max_value = max(l)
    num_buckets = len(l)
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets based on their ranges
    for num in l:
        bucket_index = int(num / max_value * (num_buckets - 1))
        buckets[bucket_index].append(num)
    
    for bucket in buckets:
        bucket.sort()
    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += bucket
    
    return sorted_arr
  
buc_sort = bucket_sort(a.copy())



print(bub_sort)
print(sel_sort)
print(ins_sort)
print(q_sort)
print(m_sort)
print(buc_sort)




