import sys

print("start")
multipleline = '''line1
line2
line3'''
print(multipleline)
print(len(multipleline))
print(multipleline[0])
print(multipleline[6:].upper())
l = multipleline.find('line2')
st = 'find = '+ str(l)
print(st)
print(multipleline[l:])
print('count = ' +str(multipleline.count('line')))
# print("start")
# print(sys.version)
# print(sys.executable)
# str = "havar"
# print(str.upper())
# print("havar")
# name = input("Your name?")
# print(name.lower())
# # print(greet('Corey'))
