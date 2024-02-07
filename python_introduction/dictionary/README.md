## Creating dictionary 
### Creating dictionary to translate instruction into a binary code 

The nature of a dictionary

The advantages of a dictionary over the list
    
    { key: value}
The difference between a dictionary key and a dictionary value
    
Inserting items in a dictionary

Extracting items from a dictionary

    regs = {'r0': 0, 'r1': 1, 'r2': 2, 'r3': 3, 'r4': 4}
    aaa = regs.get('r3')
    bbb = regs['r3']
    print(aaa, bbb) # aaa = 3 bbb = 3
Using a dictionary to solve a problem