stats = {'days_passed': 78, 'material_learned': ['programming', 'cryptography', 'servers']}
print('Days passed: ')
print(stats['days_passed'])
print('Material learned: ')
print(stats['material_learned'])
print('favorite subject : ')
print(stats['material_learned'][1])

stats['coffe'] = 4 #add to the dictionarie the key coffe with value 4
print(stats)

stats['days_passed'] += 1 # add 1
stats['coffe'] = 8
print(stats)
