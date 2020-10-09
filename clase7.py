def binary_exp(base, pw):
    aux_base = base
    ans = 1
    while(pw > 0):
        if pw%2 == 1:
            ans*=aux_base
            ans = ans%100000000007
        aux_base = (aux_base*aux_base)%100000000007
        pw//=2
    return ans%100000000007

# O(n)
# O(log_2(n))
print(binary_exp(3,1234567891231264532116))