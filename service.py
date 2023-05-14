def transfer():
    sender = input('Enter your phone number: ')
    recepient = input('Enter recepient phone number: ')
    amount = float(input('Enter transfer amount: '))
    print(
        f"""
        Sender: {sender}
        Recepient: {recepient}
        Amount: {amount}
        
        Transfer success!!!
        """
    )