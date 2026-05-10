n=int(input("number of prosseces: "))
arrival=[]
burst=[]
for i in range(n):
    
    arrival.append(int(input(f"P{i+1} Arrival: ")))
    burst.append(int(input(f"P{i+1} Burst: ")))
remaining=burst.copy()
time=0
complention=[0]*n
while sum(remaining)>0:
    smallest=-1
    for i in range(n):
        if remaining[i]>0 and arrival[i]<=time:
            if smallest==-1 or remaining[i]<remaining[smallest]:
                smallest=i
    if smallest!=-1:
        remaining[smallest]-=1
        time+=1
        if remaining[smallest]==0:
            complention[smallest]=time
            
    else:
        time+=1
waiting=[0]*n
for i in range(n):
    waiting[i]=complention[i]-arrival[i]-burst[i] 
avarage=sum(waiting)/n    
print("Waiting ",waiting)
print("Avarage ",avarage)            
               