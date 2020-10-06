def validate(s):
    stack = []
    ini = 0
    fin = 0
    ans = 0
    l = len(s)
    for x in range(l):
        print(ini)
        if s[x] == ")":
            if len(stack) == 0:
                stack_r = []
                aux_ini = x
                for y in reversed(range(ini,x+1)):
                    if s[y] == "(":
                        if len(stack_r) == 0:
                            aux_ini = y
                            break
                        stack_r.pop()
                        if len(stack_r) == 0:
                            aux_ini = y
                    else :
                        stack_r.append(s[y])
                if len(stack_r) > 0:
                    aux_ini = x+1
                ini = aux_ini
                ans = max(ans,fin-ini+1)
            else:
                stack.pop()
                if len(stack) == 0:
                    ans = max(ans,fin-ini+1)
        else:
            stack.append(s[x])
        fin = fin+1
    return ans

print(validate("(()"))
    