input_list=[-2,89,8,9]

print(input_list)


def bubble_sort(initial):
    temp=0
    #print(initial)
    for i in range(len(initial)):
        for j in range(i):
            if initial[i] < initial[j]:
                temp = initial[j]
                initial[j] = initial[i]
                initial[i] = temp

    return initial

outputlist=bubble_sort(input_list)
print (outputlist)
