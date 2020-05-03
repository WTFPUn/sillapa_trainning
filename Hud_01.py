#from https://programming.in.th/task/rev2_problem.php?pid=2001
import numpy as np
import timeit

start = timeit.default_timer()
n = int(input('input n :'))
k = int(input('input k :'))


lines = []
kfar = []
tsum = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
#print(text)
#print(len(text))
text = text.split('\n')
text = list(map(int,text))
print(text)
#print(kfar)
kmatch = []
for i in range(len(text)):
    i = i+1
    if i % 2==1  and k > 0 :
        kmatch.append(text[i-1])
    elif i % 2 ==0 and k>0 :
        kmatch.append(text[i-1])
        summ = kmatch[1] - kmatch[0]
        tsum.append(summ)
        k = k-1
        print(kmatch)
        kmatch = []
    else:
        break

print(sum(tsum))
stop = timeit.default_timer()
