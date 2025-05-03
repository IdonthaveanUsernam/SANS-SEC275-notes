fruits = ['Mango', 'Blueberry', 'Pineapple', 'Kiwi']

for fruit in fruits: #create a loop that iterate for each elements in the table fruits and give the variable name fruit to each element of the list
    print(fruit)
    if 'Papaya' not in fruits: 
        print('adding \'Papaya\'')
        fruits.append('Papaya')

bar = '#'
number = 1
for charge in range(1,101):

    print('charging...\t'+ bar)
    print('Currently at %s' %(str(number)))
    
    bar = bar + '#'
    number = number + 1


#looping through a dictionary 

capital = {'Tokyo': '37 million', 'Delhi': '32 million', 'Beijing': '21 million', 'Cairo': '20 million', 'London': '9 million'}
for key, value in capital.items(): #item retrieve both the keys and value
    print(key+' ' + ' approximate population: '+ value)
