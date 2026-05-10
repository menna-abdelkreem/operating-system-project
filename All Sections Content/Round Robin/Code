n =int(input("Number of processes: "))
burst = []
for i in range(n):
    burst.append(int(input(f"P{i+1}: ")))
tq = int(input("Time Quantum: "))
remaining = burst.copy()
time =0
completion = [0]*n
while sum(remaining)>0:
    for i in range(n):
        if remaining[i] > 0:
            if remaining[i]> tq:
                time += tq
                remaining[i] -= tq
            else:
                time += remaining[i]
                remaining[i] = 0
                completion[i] = time
waiting = []
for i in range(n):
    waiting.append(completion[i] -burst[i])
average = sum(waiting) / n
print("Waiting Time: ", waiting)
print("Average Time: ", average)

