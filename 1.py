'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

size = int(input('Max = '))

list0 = list(range(1, size + 1))

def make_3m_list(size) :
    list3m = []
    for v in list0 :
        if v % 3 == 0 :
            list3m.append(v)
    return list3m

def make_5m_list(size) :
    list5m = []
    for v in list0 :
        if v % 5 == 0 :
            list5m.append(v)
    return list5m

set3m = set(make_3m_list(size))
set5m = set(make_5m_list(size))
set3_5m = set3m | set5m
print('3 : %d / 5 : %d / 3 or 5 : %d'%(len(set3m), len(set5m), len(set3_5m)))

list_t = list(set3_5m)

summ = 0
for v in list_t :
    summ += v 
print(summ)
