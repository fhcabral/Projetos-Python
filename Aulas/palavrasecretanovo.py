palavra_secreta = "banana fish"
letra_acertada = " "
letra_adivinhada = []
tentativa = 0
import os 

while True:
    letra_digitada = input("Digite uma letra: ")

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra \n")
        continue
    
    if letra_digitada in letra_adivinhada:
        print("Esta letra ja foi digitada \n")

    if letra_digitada in palavra_secreta:
        letra_acertada+=letra_digitada
        letra_adivinhada.append(letra_digitada)
        print(f"continua na tentativa {tentativa} \n")
    else:
        print("Letra nao esta na palavra secreta")
        letra_adivinhada.append(letra_digitada)
        tentativa+=1
        print(f"tentativa {tentativa} \n")
   

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    
    

    if tentativa == 10:
         os.system('cls')
         print('VOCÊ EXCEDEU O NUMERO DE TENTATIVAS \n')
         print("**************** \n** GAMER OVER ** \n****************")
         break
    
    print("palavra formada:", palavra_formada)           

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        break
   

        
   
    
    
    