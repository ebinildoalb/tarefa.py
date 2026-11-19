def calcularMedia (nota1,  nota2, nota3):
 return (nota1 + nota2 + nota3) / 3
print("Bem_vindo á calculadora de Média!")

nota1 = float (input("insira a primeira nota"))
nota2 = float (input("insira a segunda nota"))
nota3 = float (input("insira a terceira nota"))

media =  calcularMedia(nota1, nota2, nota3 )
print("A média das tres notas é",  media)

