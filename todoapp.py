uinput = 'random'
data=[]

def showmenu():
    print('Menu')
    print('1. Add an item')
    print('2. Mark as done')
    print('3. View items')
    print('4. Exit')

while uinput!='4':
    showmenu()
    uinput = input('Enter your choice: ')
    if uinput == '1':
        item = input('What is to be done? ')
        data.append(item)
        print('Added item',item)
    elif uinput == '2':
        item = input('what is to be marked as done? ')
        if item in data:
            data.remove(item)
            print('Removed item:',item)
        else:
           print('Item does not exist in the list')
    elif uinput == '3':
        print('List of todo items')
        for item in data:
            print(item)
    elif uinput == '4':
        print('Goodbye')
    else:
        print('Please Enter one of 1,2,3 or 4')
