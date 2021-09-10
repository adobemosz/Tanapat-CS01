from typing import List


def matrix(lists):
    for i in range(int(number[0])):
        x = input().split()
        lists.append(x)
def totals():
    for o in range(int(number[0])):
        for p in range(int(number[1])):
            z = int(m[o][p])+int(n[o][p])
            total.append(z)
def print_matirx():
    for l in range(len(total)):
        if (l+1)%int(number[1]) == 0:
            print(total[l], end='')
number = input().split()
m = []
n = []
total = []
matrix(m)
matrix(n)
totals()
print_matirx()
