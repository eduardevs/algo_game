def bubble_sort(tab):

    for i in range(0, len(tab)):
        for j in range(0, len(tab) - 1 - i):
            if(tab[j] > tab[j+1]):
               tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

print('write list of numbers for bubble sort')
tab_str = input().split(',')

tab = [int(num) for num in tab_str]

print(bubble_sort(tab))

