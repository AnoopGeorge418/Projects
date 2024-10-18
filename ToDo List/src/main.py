from functionalities import add, view, update, delete

def main():
    print('Welcome to a termninal based todo list application')

    print('1: Add Tasks \n'
          '2: View Tasks \n'
          '3: Update Tasks \n'
          '4: Delete Tasks')
          
    while True:
        try:
            print('\n')
            choose = input('Enter the number: ')
            if choose == '1':
                add()
            elif choose == '2':
                view()
            elif choose == '3':
                update()    
            elif choose == '4':
                delete()
            elif str(choose).lower() == 'q':
                break
            
        except ValueError:
            print('Please enter number.')


if __name__ == '__main__':
    main()