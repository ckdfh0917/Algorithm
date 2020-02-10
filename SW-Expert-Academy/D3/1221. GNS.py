import sys
sys.stdin = open('input.txt', 'r')

num_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
str_dict = {0:"ZRO",1: "ONE",2: "TWO",3: "THR",4: "FOR",5: "FIV",6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"
}
q = int(input())

for test_case in range(1, q + 1):
    tc, num = map(str, input().split())
    num = int(num)
    print(tc)

    numbers = list(map(str, input().split()))
    aa = []
    for i in range(num):
        aa.append(num_dict[numbers[i]])
    aa.sort()
    res = []
    for i in range(num):
        res.append(str_dict[aa[i]])
    print(' '.join(res))