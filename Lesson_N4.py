"""
allteams = ["Ararat-Armenia", "Shirak", "Urartu", "Pyunik", "Kayrat", "Zhetisu", "BATE", "Gomel",]
print(allteams)
allteams.remove ("Kayrat", )
print(allteams)
"""
L = []
Lis = [1, 56, "x", 34, 2.34, ["S", "t", "r", "o", "k", "a"]]
print(Lis)
a = [a + b for a in "list" if a != "s" for b in "soup" if b != "u"]
print(a)
#Ավելացնում է էլեմենտ ցանկի վերջում(append)։
L.append(23)
L.append(34)
print(L)
b = [ 24, 67]
#ընդլայնում է ցանկը, մեկ ուրիշ ցանկով։(extend)
L.extend(b)
print(L)
#Ավելացնում է էլեմենտ ըստ ինդեքսի, այսինքն ըստ հերթական համարի(insert)
L.insert(1, 56) #այսինքն 1 ինդեքսում տեղադրել 56 թիվը
print(L)
L.append(34)
#ջնջում է էլոմենտը ցուցակից, բայց եթե նույն արժեքով մեկից ավելի էլեմենտ է լինում, ջնջում է միայն առաջինը։(remove)
L.remove(34)
print(L)
#Հեռացնում է ըստ ինդեքսի, եթե ինդեքսը չի նշվում ապա հեռացնում է վերջին ավելացրած էլեմենտը։(pop)
L.pop(0)
print(L)
#ցույց է տալիս էլեմենտի ինդեքսը(հերթական համարը)(index)
print(L.index(56))
#ցույց է տալիս թե տվյալ արժեքով քանի էլեմենտ կա ցանկում:(count)
print(L.index(24))
#Սորտավորում է ըստ հերթականության:(sort)
L.sort()
print(L)
#Հակառակ է դասավորում։(reverse)
L.reverse()
print(L)
#մաքրում է ողջ ցուցակը:(clear)
L.clear()
print(L)