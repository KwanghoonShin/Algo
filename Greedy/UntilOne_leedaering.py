# Source code (문제: 1이 될 때 까지)

n,k = map(int, input().split()) # n과 k를 공백을 기준으로 구분하여 입력 받는다 (정수형)
result=0

# N이 K로 나누어 떨어지는 수가 될 때 까지 빼기
while True:
    target=(n//k)*k # n이 k로 떨어지지 않는다고 했을 때, K로 나누어 떨어지는 가장 가까운 수 탐색
    # target 값은 k로 나누어 떨어지는 수가 될 것임 
    result+=(n-target) # 1을 빼는 연산을 사용하는 횟수 
    n=target
    
    if n<k:
        break
    
    # K로 나누기
    result+=1 # 나누는 연산 진행할 때 마다 1씩 증가 (더하기)
    n//=k
    
result+=(n-1) # n이 k보다 작아졌을 때, 탈출하고 n이 1보다 클 때 1씩 뺴는 연산을 수행
print(result)
