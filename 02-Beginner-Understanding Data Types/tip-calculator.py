if __name__ == "__main__":
    print('Welcome to the tip Calculator')
    bill = float(input('What was the total bill? '))
    tip = float(input('What percentage tip would you like to give? 10, 12, 15? '))
    split = int(input('How many peoples to split the bill? '))

    totalBill = bill + (bill * (tip/100))
    print(f'\n\nYour total bill: {totalBill}')

    print(f'Each person need to pay: {totalBill/split}')