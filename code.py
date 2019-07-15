n=int(input())
for i in range(n):
    S=input()
    for j in range(0,len(S),2):
        print(S[j],end='')
    print(' ',end='')
    for k in range(1,len(S),2):
        print(S[k],end='')
    print('')
