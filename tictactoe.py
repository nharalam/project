# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pprint



empty = ""
player1 = 'X'
player2 = 'O'
A = [[player1, empty, empty], [empty, empty, empty], [empty, empty, empty]]

print(A)

def check_board():
    for i in A:
        if i is not empty:
            print(empty)
        else:
            print(notempty)