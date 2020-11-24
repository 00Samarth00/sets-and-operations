#Let the 2 sets be:-
print('Let the 2 sets be:-')
set1=[1,2,4,6,7,3]
print('set1.',set1)
set2=[5,9,7,8,4,0]
print('set2.',set2)

set4=[]
for x in set1:
    if x in set2 and set1:
        set4.append(x)

    else:
        None

#Union of set1 & set2:-
print('Union of set1 and set2:')
set3=(set1+set2)
for i in set3:
    if i in set1 and set2:
        set3.remove(i)
set3+=set4
print(set3)

#Intersection of set1 and set2:-
print('Intersection of set1 and set2:')

print(set4)

#Difference of set1 and set2:-
print('Difference of set1 and set2:')
set5=set1.copy()
for num in set4:
    set5.remove(num)

print(set5)

#Symmetric Difference of set1 and set2:-
print('Symmetric Difference of set1 and set2:')
set6=set2.copy()
for num in set4:
    set6.remove(num)

set6+=set5

print(set6)
