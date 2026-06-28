# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())
rooms = list(map(int, input().split()))

count = {}

for room in rooms:
    if room in count:
        count[room] += 1
    else:
        count[room] = 1

for room in count:
    if count[room] == 1:
        print(room)
        break
