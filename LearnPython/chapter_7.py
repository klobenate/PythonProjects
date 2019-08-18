#User Input and While Loops

#message = input("Name:")

#print(message)



'''
End of Chapter
'''


#1
sandwich_orders = ['buffalo chicken', 'pastrami','salami', 'pastrami', 'peperoni', 'vegan', 'pastrami']
finished_orders = []

print('The deli has run out of Pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f'I made you a {sandwich.title()} sandwich!')
    finished_orders.append(sandwich)

print(finished_orders)


