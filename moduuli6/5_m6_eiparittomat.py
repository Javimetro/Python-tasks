def parittomatpois (list):
    for n in list:
        if n % 2 == 0:
            list2.append(n)
    print(list)
    print(list2)

list = [1,2,3,4,5,6,7,8,9]
list2 = []

parittomatpois(list)