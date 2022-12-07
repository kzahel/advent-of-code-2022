data = open('1.txt').read()
data = [list(map(int,d.split('\n'))) for d in data.split('\n\n')]

#print(data)

# just the max
#print(max(sum(d) for d in data))


sums = [sum(d) for d in data]

sums.sort()
sums.reverse()

print(sum(sums[0:3]))
