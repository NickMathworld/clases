def dailyTemperatures(T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    arr = []
    ans = []
    for x in len(T):
        ans.append(0)

    for x in range(len(T)):
        arr.append((T[x],x))

    arr = sorted(arr, key=lambda elt:elt[0])
    
    for x in range(len(arr)):
        current = arr[x][0]
        currentPos = arr[x][1]
        stack = []
        stack.append(currentPos[])
        for y in range(x+1,len(arr)):
            if 


input = [73,74,75,71,69,72,76,73]
dailyTemperatures(input)