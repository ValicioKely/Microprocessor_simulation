# example using replace() on string
price = 'egg 2$, cheese 4$'
price = price.replace('$', ' Mga')
print(price)

# strip()
x = "###this Is A test? ? ? "
x = x.lstrip('#')
print(x)
print(x.rstrip('?'))
print(x.lower())
print(x.upper())
st = '4' + '5'
print(st)
line = 'LDRl r0,[r2]'
line = line.replace(',', ' ')
line = line.replace('[', '')
line = line.replace(']', '')
line = line.upper()
line = line.lstrip(' ')
line = line.rstrip('\n')
line = line.split(' ')
op = line[0]
value_1 = line[1]
value_2 = line[2]
print(line,'\n', op ,'\n' , value_1, '\n', value_2)
