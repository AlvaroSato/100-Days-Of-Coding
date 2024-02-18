'''
Write a program that adds the digt in a 2 digit number e.g. if the input was 35, then the output should be 3 + 5 = 8.
'''

if __name__ == "__main__":
    twoDigit = input("Write a Two Digit Integer Number: ")
    if(len(twoDigit) != 2):
        raise ValueError('Please, insert a two digit integer number'.upper())
    try:
        sum = int(twoDigit[0]) + int(twoDigit[1])
        print(sum)
    except:
        print("Sorry, something gone wrong")