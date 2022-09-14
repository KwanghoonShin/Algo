# 큰 수의 법칙 

n,m,k=list(map(int,input().split())) # n개의 자연수, M : 더하는 횟수, K: 연속해서 더하지 못하는 횟수
num_array=list(map(int,input().split()))

num_array_asc=sorted(num_array,reverse=True)
print(num_array_asc)

num_firstLrgst=num_array_asc[0]
num_secondLrgst=num_array_asc[1]

target_sum=0
count=0

print(num_firstLrgst,num_secondLrgst)

while count!=m: # count로 선언한 값이 m이 될 때 까지
    for i in range(k): # 연속해서 더 할 수 있는 횟수(K) 동안
        target_sum+=num_firstLrgst # 배열에서 가장 큰 수를 계속 더함
        print("for문 :", target_sum)
        count+=1 # 카운터 증가 (카운터는 m과 비교하기 위해 존재)
    
    if count!=m:# 최대 덧셈 횟수을 충족하지 않았을 때 
        target_sum+=num_secondLrgst # 두번째로 큰 수를 더함
        print("if문 :", target_sum)
        count+=1 # 카운터 증가 

print(target_sum)
