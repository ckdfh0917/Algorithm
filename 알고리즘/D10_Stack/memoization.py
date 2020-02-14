# memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다
# memo[0]을 0으로 하여 memo[1]sms 1로 초기화한다.

# 메모이제이션 : 연산결과를 저장 -> 중복계산을 안함
# 메모를 저장하기 위한 배열을 할당하고 0으로 초기화


def fibo1(n):
    # n이 이보다 같거나 크고 n이 메모 길이보다 길면 -> 아직 계산되지 않았다면
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
        print(memo)
    return memo[n]  # 아니라면 -> 이미 계산된 값이라면 -> 메모리제이션 배열에 저장된 값을 리턴

memo = [0, 1]
print(fibo1(5))

# DP 적용

def fibo2(n):
    f = [0,1]   # 초기화
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

print(fibo2(5))