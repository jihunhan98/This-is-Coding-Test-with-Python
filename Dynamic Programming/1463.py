#1로 만들기
#1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
#2. X가 2로 나누어 떨어지면, 2로 나눈다.
#3. 1을 뺀다.

#1로 만드는 연산의 최솟값을 구한다.

n = int(input())
d = [0] * (n+1) #메모제이션

for i in range(2, n+1):
    d[i] = d[i-1] + 1 #1을 빼는 거는 디폴트로

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1) #3으로 나누어지면 3으로 나누어진 것과 1을 뺀거중 최솟값.
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1) #2으로 나누어지면 2으로 나누어진 것과 위의 최솟값의 최솟값

print(d[n])