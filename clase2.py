a = 20
b = -5
c = 1
d = 2
# a == 20 or b == 20 -> True or False ->C1
# c == 1 or d == 2 -> True or False->C2
# C1 and C2
# and or & ||
# != 
if (a == 20 or b == 20) and (c == 1 or d == 2):
    print("A vale: ",a)
elif a == 19:
    print("A no vale 10")
elif a==18:
    print("cualquier cosa 1")
elif a==17:
    print("Cualquier cosa 2")
else:
    print("Cualquier cosa 3")
# x < 10
# 
for x in range(10):
    print(x)
print("\n")
for x in range(5,10):
    print(x)
print("\n")
cadena = "Brian Zuniga Uribe"
cadenas = ["hola","mundo","nick","madworld"]
primes = [2, 3, 5, 7]
a = "nick"
b = "levi"
c = a+b
## output
## c = nicklevi
ans = ""
for x in cadena:
    if x != "a":
        ans = ans+x
    # x = Z
    # ans = "Brian "
    # ans = ans+x
    # ans = "Brian Z"
#param1 será una cadena
#ch1 será el caracter que debemos eliminar de la cadena param1

def quitaChar(param1, ch1):
    ans = ""
    for x in param1:
        if x != ch1:
            ans = x+ans
    return ans

def volteaCadena(param1):
    ans = ""
    return ans


#inpt = input("Ingresa una cadena: ")
#char = input("Ingresa el char a eliminar: ")
#respuesta = quitaChar(inpt,char)
##print(respuesta)

print("\n")

for cadena in cadenas:
    print(cadena)
    for char in cadena:
        print(char)