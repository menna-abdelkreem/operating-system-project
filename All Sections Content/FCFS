n = int(input("number of procceses :"))
burst = []
waiting = [0]
for i in range(n):
    bt = int(input(f" procces {i+1} burst :"))
    burst.append(bt)
for i in range (1,n):
    waiting.append(waiting[i-1] + burst[i-1])    

avg = sum(waiting)/n
print("burst time :", burst)
print("waiting time :",waiting)
print ("average :", avg)        
