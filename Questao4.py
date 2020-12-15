def __is_palindrome(string):
    return string == string[::-1]

def __main__():
    palavra = input("digite a palavra que você deseja verificar: ");
    if(__is_palindrome(palavra)):
        print(palavra + " É um palíndromo.")
    else:
        print(palavra + " Não é um palíndromo.")
        
__main__()