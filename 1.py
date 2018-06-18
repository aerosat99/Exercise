'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

size = int(input('Max = '))

list0 = list(range(1,size+1))  # list(range(1000)) -> 0~999까지 1000개 / list(range(1,1001)) -> 1부터 1000까지 1000

def make_3m_list(size) :
    list1 = []
    for v in list0 :
        if v % 3 == 0 :
            list1.append(v)
    return set(list1)

def make_5m_list(size) :
    list2 = []
    for v in list0 :
        if v % 5 == 0 :
            list2.append(v)
    return set(list2)

def make_15m_list(size) :
    list3 = []
    for v in list0 :
        if v % 15 == 0 :
            list3.append(v)
    return set(list3)


set3 = make_3m_list(size)
set5 = make_5m_list(size)
set15 = make_15m_list(size)
set_t = set3 | set5 | set15    # 중복을 한개만 놔두고 합집합으로

list_set_t = list(set_t)

print('3 = %s / 5 = %s / 3 or 5 = %s / Total = %s'%(len(set3), len(set5), len(set15), len(set_t)))  # 집합의 원소 개수는 len으로 센다

sum = 0
for v in list_set_t :
    sum += v
print('Sum = %s'%sum)
