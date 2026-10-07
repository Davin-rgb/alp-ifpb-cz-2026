estojo = []
i = 0
while i !=2:
    print('Bem Vindo')
    print('1- Adiciona algo ao estojo')
    print('2- Parar o programa')
    print('3- Ver o estojo')
    i = int(input('Escolha uma opção:'))    
    if i == 1:
        i = input("Escreva o que deseja adicionar:")
        estojo.append(i)
        print(estojo)  
    elif i == 2:
        print('encerrando programa')
        break
    elif i == 3:
        for i in estojo:
            print(i)