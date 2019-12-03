d = { "am" : 1, "as" : 45, "lm" : 3}
print (d)

a = dict(short = 'dict', longer = 'dictionary')
print(a)

b = dict.fromkeys(['a', 'b', 'c'], 1)
print(b)

c = {a : a ** 2 for a in  range(7)}
print(c)

person = {'name' : {'first_name' : 'Harutyun', 'last_name' : 'Baghdagulyan'}, 'address' : ['Yerevan', 'Shahumyan 4th street',
'17/1 home'], 'phone' : {'home_phone' : '010775219', 'mobile' : '+37455802822'}}
print(person["name"]["first_name"])
print(person['address'][0])