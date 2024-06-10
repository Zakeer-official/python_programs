
a = [5,3,2,1,4]

def bubble_sort(l):   #bubble sort algorithm
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return a

bub_sort = bubble_sort(a)

b = [5,3,2,1,4]

def selection_sort(l):   #selection sort algorithm
    for i in range(len(l)-1):
        min_idx = i
        for j in range(i+1,len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
    return l

sel_sort = selection_sort(b)


c = [5,3,2,1,4]

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

ins_sort = insertion_sort(c)


d = [5,3,2,1,4]

def quick_sort(l): #quick sort algorithm
    left = 0
    right = len(l)-1
    pivot = (len(l) - 1) //2
    for i in range(1,len(l)):
        x = l[i]
        for j in range(i-1,-2,-1):
            if l[j] > x:
                l[j+1] = l[j]
            else:
                break
        l[j+1] = x 
    return l

q_sort = quick_sort(d)


print(bub_sort)
print(sel_sort)
print(ins_sort)
print(q_sort)





