def printFunction():
    # This will print the content inside on console
    # print('Hello World!')

    print('1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.')
    print('2. Knead the dough for 10 minutes')
    print('3. Add 3g of Salt')
    print('4. Leave to rise for 2 hours')
    print('5. Bake at 200 degrees C for 30 minutes')


    '''
    You can print a single or double quote, just alternate them inside the print like:
    print('Hello "Double Quotes" World!')
    print("Hello 'Single Quotes' World!")
    print('Alternatively you can \"escape\" the quote)
    '''

    # You can Concatenate a String like
    print('Hello' + 'World') #HelloWorld
    print('Hello', 'World') #Hello World

def inputFunction():
    # You can request a user input using
    input('This is an Input: ')

def variables():
    name = input('Enter you name: ')
    # If i want to print the name on cosole, i can just
    print(name)

    # If i have this
    name = 'Jack'
    print(name)

    name = 'Ana'
    print(name)
    # The output will be
    # Jack
    # Ana