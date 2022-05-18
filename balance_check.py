from main import Stack

opening = ['[','{','(']
closing = [']','}',')']


def balance_checker(string):
    balance = True
    s = Stack()
    for symbol in string:
        if symbol in opening:
            s.push(symbol)
        elif symbol in closing:
            ind = closing.index(symbol)
            if len(s.all_elements()) > 0 and (opening[ind] == s.all_elements()[len(s.all_elements()) - 1]):
                s.pop()
            else:
                balance = False
    return balance


print(balance_checker(input('Введите строку: ')))
