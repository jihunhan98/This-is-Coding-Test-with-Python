d = [0] * 100 #한 번 구한 값을 저장하기 위한 리스트(메모이제이션)

def fibo(x):

    if x == 1 or x == 2: #종료 조건
        return 1

    if d[x] != 0: #이미 계산된 값이라면 그대로 반환
        return d[x]

    #계산한 적이 없으면 점화식에 따라 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
