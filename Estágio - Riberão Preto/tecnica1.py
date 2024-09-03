n = 15 #vc pode também usar int(input())
t1 = 0
t2 = 1
cont = 3
seqFibo = []
while cont <= n:
    t3 = t1 + t2
    seqFibo.append(t3)
    t1 = t2
    t2 = t3
    cont += 1
numEsq = 4 #vc pode também usar um int(input())

if numEsq in seqFibo:
    print(f"O {numEsq} pertence a sequência de Fibonacci")
else:
    print(f"O {numEsq} não pertence a sequência de Fibonacci")



