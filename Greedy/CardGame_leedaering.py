# 숫자 카드 게임 
# N : 행의 개수
# M : 열의 개수 

n,m=map(int,input().split())
dataCard=[]

for i in range(n): # 뽑은 카드를 2차원 리스트에 저장 
    dataCard.append(list(map(int,input().split())))
    
list_min=[] # 각 행의 최소값을 저장할 리스트 

for j in range(n): # 각 행에 접근하여, 최소값을 list_min에 저장 
    list_min.append((min(dataCard[j])))

target_num=max(list_min) # 최소값들이 저장된 리스트 중 최대값 뽑기 

print(target_num)
    
