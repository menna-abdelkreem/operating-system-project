n = int(input("Enter number of processes: "))
arrival = []
burst  = []
burst = []
priority = []

for i in range(n):
    arrival.append(int(input(f"Enetr P{i+1} arrival: ")))
    burst.append(int(input(f"Enter P{i+1} burst: ")))
    priority.append(int(input(f"Enter P{i+1} priority: ")))

remaining = burst.copy()
time = 0
completion = [0] * n

while sum(remaining) > 0:
    idx = -1
    for i in range(n):
        if arrival[i] <= time and remaining[i] > 0:
            if idx == -1 or priority[i] < priority[idx]:
                idx = i

    if idx != -1:
        remaining[idx] -= 1
        time += 1

        if remaining[idx] == 0:
            completion[idx] = time
    else:
        time += 1

waiting = []
for i in range(n):
    waiting.append(completion[i] - arrival[i] - burst[i])

average = sum(waiting) / n
print("Waiting time: " , waiting)
print("Average Waiting Time:", average)
