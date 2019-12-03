"""
def func(x, a):
    return x + a
print(func(23, 12))
"""
"""
def func(a, z):
    res = a +" " z
    return res
print(func("Harut", "Baghdagulyan"))
"""

def funkcia (a):
    def norfunkcia(b):
        return a + b
    return norfunkcia

test = funkcia(150)
print(test(100))

"""
def func (x=25, y=2, z=5):
    return x-y*z
print(func())
"""
def matem(a, b, c=2):
    res = a + b
    res *=c
    return res
print(matem(3, 4))

def kortej(*a):
    return a
print(kortej(12, 4, 4))

def slovar(**an):
    return an
print(slovar(a=25, b=15, c=3))

#lambda-անոնիմ ֆունկցիաներ
add = lambda x, y: x+y
print(add(2, 4))
# մյուս գրելաձևը
print((lambda f, g: f*g)(4,'q'))
# lamdan-ով հնարավոր է գրել մյուս բոլորըմ ինչը որ գրվեց def-ով



