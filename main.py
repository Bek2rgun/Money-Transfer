from service import transfer

def main():
    user_action = input('Enter 1 to transfer\n Enter 2 to exit\n')
    while True:
        if user_action == '1':
            transfer()
            user_action = input('Enter 1 to transfer\n Enter 2 to exit\n')
        elif user_action == '2':
            print('Goodbye!')
            break
        else:
            print('Incorrect command')
    

if __name__ == '__main__':
    main()