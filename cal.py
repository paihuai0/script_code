list1 = [69478.29161048493, 5497.284569672957, 19903.860983456812, 5134.362541983892, 684.9658020746069, 5761.186632137044, 313.7170339576281, 10930.276780568556]
list2 = [53622.797424316406, 4331.233734130859, 14587.872800827026, 3322.9260997772217, 575.8620986938477, 4552.413063049316, 209.7103500366211, 7552.345956802368]
list3 = [
28964,
912,
13560,
8004,
256,
1220,
296,
39431
]

for i in range(len(list3)):
    result = list2[i] / list3[i]
    print('%.2f' % result)