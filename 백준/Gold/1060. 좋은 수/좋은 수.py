import sys
from collections import deque
import heapq
import copy
#input=sys.stdin.readline
#sys.setrecursionlimit(100000000)

l=int(input())
S=list(map(int,input().split()))
S.sort()
n=int(input())
L=[]
ans=[]
q=0
if S[0]==2:
    ans.append([0,1])
elif S[0]>2:
    L.append([S[0]-1,1])
    q+=1
for i in range(l-1):
    if S[i+1]-S[i]-1==1:
        ans.append([0,S[i]+1])
    else:
        L.append([S[i+1]-S[i]-1,S[i]+1])
        q+=1
L.sort()
for i in S:
    ans.append([0,i])
for a,b in L:
    p=0
    q=a//2
    k=0
    while p<q and k<n:
        m=0
        if p>1:
            m=sum(range(p))
        ans.append([sum(range(a-1,a-p-2,-1))-m,b+p])
        ans.append([sum(range(a-1,a-p-2,-1))-m,b+a-1-p])
        k+=2
        p+=1
    if a%2:
        m=0
        if p>1:
            m=sum(range(p))
        ans.append([sum(range(a-1,a-p-2,-1))-m,b+p])
ans.sort()
p=len(ans)
k=1
while p<n:
    ans.append([0,S[l-1]+k])
    p+=1
    k+=1
for i in range(n):
    print(ans[i][1],end='')
    if i!=n-1:
        print(end=' ')