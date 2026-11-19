def calcularMedia(n1,n2,n3):
 return  (n1+n2+n3) /3
print("bem_vindo a calculadora de média")

nota1 = float(input("insere a primeira nota"))
nota2 = float(input("insere a segunda nota"))
nota3 = float(input("insere a terceira nota"))

média = calcularMedia(nota1,nota2,nota3)

print ("a média das tres notas é" , média)
