print("This program detect consecutive tokens")
max_red = input("how many token are you looking for?")
max_red = int(max_red)
num_red = 0
go = 1
while go == 1:
    y = input("Which token is it? Red or White?")
    if y == 'w':
        num_red = 0
    else:
        num_red = num_red + 1
    if num_red == max_red:
        go = 0
        break
print(num_red, "Red found")
