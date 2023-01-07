#정렬해야 할 배열
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i #맨 처음 인덱스를 최솟값으로 설정
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:  #만약 j가 최솟값보다 작다면
            min_index = j  #j를 최솟값으로 설정
    arr[i], arr[min_index] = arr[min_index], arr[i] #전부 비교 후, 최솟값과 현재 인덱스와 스왑

print(arr)