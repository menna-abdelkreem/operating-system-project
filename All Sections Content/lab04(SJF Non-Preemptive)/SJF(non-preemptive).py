n = int(input("Enter the number of processes: "))
burst = []
for i in range(n):
    burst.append(int(input(f"Enter the burst time of process {i + 1}: ")))
burst.sort()
waiting = [0] * n
for i in range(1, n):
    waiting[i] = waiting[i - 1] + burst[i - 1]
average_waiting = sum(waiting) / n
print("burst times:", burst)
print("waiting times:", waiting)
print("Average Waiting Time:", average_waiting)
