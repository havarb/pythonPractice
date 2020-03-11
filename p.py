import sys

print("start")


s = ['var1', 'var2', 'var3',4]

print(s)
print(s[0])
print(len(s))
print(type(s[-1]))
s.remove('var1')
s.append('havar')
print(sorted(s))
print(s)

for n, val in enumerate(s, start=2):
    print('value' + str(n) + ' = ')
    print(val)

student = {'name':'John', 'age':20, 'courses': ['Math','Cmop']}
print(student['name'])
print(student.get('phone'))
print(student.items())
#num = 3.14
#print(type(num))

multipleline = '''line1
line2
line3'''
#print(type(multipleline))
'''
print(multipleline)
print(len(multipleline))
print(multipleline[0])
print(multipleline[6:].upper())
l = multipleline.find('line2')
st = 'find = '+ str(l)
print(st)
print(multipleline[l:])
print('count = ' +str(multipleline.count('line')))
print(multipleline.replace('line','havar',2))

name = 'Havar'
family = 'Bat'
s0 = 'the name is %s, %s' %(name.upper(),family)
s = 'Hello {} , Welcome {} {}'.format(name,name,family)
s2 = f'Hello {name.upper()} , Welcome {name} {family}'
print(s0)
print(s)
print(s2)
'''
#print(dir(name))
#print(name.islower())
#print(help(str))
# print("start")
# print(sys.version)
# print(sys.executable)
# str = "havar"
# print(str.upper())
# print("havar")
# name = input("Your name?")
# print(name.lower())
# # print(greet('Corey'))
