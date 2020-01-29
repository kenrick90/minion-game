def minion_game(string):
    stuart=0
    kevin=0
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for i in range(len(string)):
        if string[i] in vowels:
            kevin+=len(string[i:])
        else:
            stuart+=len(string[i:])

    if stuart>kevin:
        print("Stuart",stuart)
    elif kevin>stuart:
        print("Kevin",kevin)
    else:
        print("Draw")
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)