print("Digite o primeiro número:")
numA = int(input())
print("Digite o segundo número:")
numB = int(input())
print("Digite o terceiro número:")
numC = int(input())

if numA > numB:
    if numA > numC:
        print("O maior número é:", numA)
        if numB > numC:
            print("O número do meio é:", numB)
            print("O menor número é:", numC)
        else:
            print("O maior número é:", numA)
            print("O número do meio é:", numC)
            print("O menor número é:", numB)

    else:
        print("O maior número é:", numC)
        print("O número do meio é:", numA)
        print("O menor número é:", numB)
else:
    if numB > numC:
            print("O maior número é:", numB)
            if numA > numC:
                print("O menor número é:", numC)
                print("O número do meio é:", numA)
            else:
                print("O número do meio é:", numC)
                print("O menor número é:", numA)
    else:
        print("O maior número é:", numC)
        print("O número do meio é:", numB)
        print("O menor número é:", numA)
