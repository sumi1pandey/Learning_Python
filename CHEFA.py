t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # your code goes here
    
    a.sort(reverse = True)
    
    chefcount = 0
    
    for i in range(0,n,2):
        chefcount += a[i]
    
    print(chefcount)
