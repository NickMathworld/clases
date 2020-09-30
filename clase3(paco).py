cadenas = [1,2,3]

dic = {'persona':"tipo 1",
        'nombre':"Nick Madworld",
        'edad': 20
}

cadenas.append(dic)
cadenas.append("hola paco")
# print(dic)
# print(cadenas[3])

# for index in range(len(cadenas)):
#     print(cadenas[index])

def fun(n):
    if n == 0:
        return 0
    return fun(n-1)+n
#1+2+3+4+5
# fun(5)
# fun(4)+5
# fun(3)+4
# fun(2)+3
# fun(1)+2
# fun(0)+1
# fun(0)
# print(fun(5))

pila = []
pila.append(1)
pila.append(2)
pila.append(3)


while len(pila) > 0:
    print(pila.pop())
print(pila)
#([{}])
def validateString(input):
    contenido = input
    parentesis = []
    for x in contenido:
        if x == "(":
            parentesis.append(x)
        elif x == ")":
            if len(parentesis) == 0:
                return False
            parentesis.pop()
            
    if len(parentesis) == 0:
        return True
    return False
#hola mundo
def palindromo(s):
    for x in range(int(len(s)/2)):
        if s[x] != s[len(s)-x-1]:
            return False
    return True
# 
# (,(
# 
#queues
    #FIFO
#stacks
    #LIFO
#dequeues
#trees
#graphs
#linked list

# ans = validateString("()((())() ()(())()() )")
ans = palindromo("anitalavalatina")
print(ans)