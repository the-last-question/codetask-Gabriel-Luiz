def __verifyPerfectNumber(num):
    Sum_divisor = 0
    for i in range(1, num):
        if(num % i == 0):
            Sum_divisor = Sum_divisor + i

    if (Sum_divisor == num):
        return True
    else:
        return False

def __main__():
   for i in range(1, 10000):
        if(__verifyPerfectNumber(i)):
             print(" %d É um número perfeito" %i)
    
        
__main__()