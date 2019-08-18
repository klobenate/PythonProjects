#def display_message():
#    print("This is a function")

#display_message()

#def favorite_book(book):
#    print(book)


#print('What is your favorite book')

#book_name = input()

#favorite_book(book_name)

#consider def _func_name(*param) <- arbitrary # of param
# **kwargs to pass a key-value pair to a function

'''
End of Chapter
'''

def repair_ticket(first_name, last_name, date, isRush = ''):
    new_ticket = {'name' : first_name, 'last_name': last_name, 'date': date, 'isRush': isRush}

    return new_ticket


created_tickets = []

count = 0


while count < 2:
    f_name = input('First Name: ')
    l_name = input('Last Name: ')
    date = input('Date: ')
    isRush = input('Is this a rush(optional):')

    ticket = repair_ticket(f_name, l_name, date, isRush)

    created_tickets.append(ticket)

    print(created_tickets)

    count += 1