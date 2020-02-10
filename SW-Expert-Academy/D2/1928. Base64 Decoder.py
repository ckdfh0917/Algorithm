# 디버깅용 시험 제출시 제거
import sys
sys.stdin = open('input2.txt','r')            # 표준입력을 콘솔창에서 파일로 변경

munja_dict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25, 'a':26, 'b':27, 'c':28, 'd':29, 'e':30, 'f':31, 'g':32, 'h':33, 'i':34, 'j':35, 'k':36, 'l':37, 'm':38, 'n':39, 'o':40, 'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,'z':51,'0':52,'1':53,'2':54,'3':55,'4':56,'5':57,'6':58,'7':59,'8':60,'9':61,'+':62,'/':63}

q = int(input())

for test_case in range(1, q + 1):
    list_a  = list(map(str, input()))
    print('#{} ' .format(test_case), end='')


    num_list = []
    for i in range(len(list_a)):
        num_list.append(munja_dict[list_a[i]])

    #print('num_list')
    #print(num_list)
    #print(num_list[0] << 6)

    new_list = 0
    #print(new_list << 6)

    for j in range(0,len(num_list),4):
        new_list = 0
        for i in range(4):
            #print(num_list[i])
            #print(bin(num_list[i]))
            new_list = (new_list << 6) + num_list[i+j]
            #print(bin(new_list))
        #print(new_list)

        print(chr(new_list >> 16), end='')
        print(chr((new_list >> 8) & 0xff), end='')
        print(chr(new_list & 0xff), end='')
        #print()
    print()

# 8비트 중 하위 6비트씩 묶어 앞에서 부터 8비트씩 새로운 비트를 생성
# 숫자에서 다시 문자로 넘어갈때는 아스키코드의 숫자를 이용해야함
# 기존에 주어진 Encoding을 이용하면 안됨