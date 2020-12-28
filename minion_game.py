def minion_game(string):
    # your code goes here
    s = len(string)
    con, vow = 0, 0
    for i in range(s):
        if string[i] in "AEIOU":
            vow = vow + (s-i)
        else:
            con = con + (s-i)

    if vow > con:
        print("Kevin", vow)
    elif con > vow:
        print("Stuart", con)
    else:
        print("Draw")




if __name__ == '__main__':
    s = input()
    s = s.upper()
    minion_game(s)
