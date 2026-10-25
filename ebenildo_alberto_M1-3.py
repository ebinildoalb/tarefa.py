
nome= "ebinildo alberto"
idade = 29
peso = 74.5
hobbies = ["cortador de carne ", "atividades diversas"]

utilizador = {
    "nome": nome,
    "idade": idade,
    "peso": peso,
    "hobbies": hobbies
}
print("Dicionario utilizador:")
print(utilizador)

print("\nValores individuais:")
print("Nome:", utilizador["nome"])
print("Idade:", utilizador["idade"])
print("Peso", utilizador["peso"])
print("Hobbies:", utilizador["hobbies"])

      
idade_como_string  = str(idade)
print(f"\nIdade convertida para string: {idade_como_string} | tipo:{type(idade_como_string)} ")

utilizador["hobbies"].append("viagens")
print("\nDicionario atualizado com novo hobby:")
print(utilizador)
