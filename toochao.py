"""
Function to check minimum bribes
>>> minimumBribes([2,1,5,3,4])
5
"""
def minimumBribes(q):
    ans = 0
    for x in reversed(range(len(q))):
        if q[x]-(x+1) > 2:
            print(q[x]," -- ",x+1)
            print("Too chaotic")
            return
        for y in range(max(0,q[x]-2),x):
            if(q[y] > q[x]):
                ans+=1
    print(ans)

"""
    1 2 3 4 5 6 7 8
    1 2 5 3 4 6 7 8
    1 2 5 3 6 4 7 8
    1 2 5 3 7 4 6 8
    1 2 5 3 7 8 6 4 
"""
minimumBribes([1,2,5,3,7,8,6,4])