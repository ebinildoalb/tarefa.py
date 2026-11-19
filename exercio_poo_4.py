import random
numero_secreto = random.randint(1,100)
tentativas = 7
tentativas_usadas = 0

print ("Bem_vindo ao jogo do número secreto!")
print("tentei adivinhar um número entre 1 e 100.")
print("tens 7 tentativas. boa sorte!")

while tentativas > 0:
    print("\nTentativas que faltam:",tentativas)
    palpite = int(input("qual é o teu palpite? (0 para saire"))

    if palpite == 0 :
     print("saiste do jogo. o numero secreto era:", numero_secreto)
     break       
 

    tentativas_uasadas = tentativas_usadas +1
    tentativas =  tentativas -1

    if palpite == numero_secreto:
     print("parabens ! acertaste em " , tentativas_usadas, "tentativas.")
     break

    elif  palpite > numero_secreto:
     print("o numero secreto é menor ")
    else:
      print("o numero seceto é maior.")

