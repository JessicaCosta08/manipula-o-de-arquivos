cont = 0

with open('resposta.txt', 'w') as arquivo:
    numero_de_pessoas = 10
    for i in range(numero_de_pessoas):
        pergunta = 'Quem é você? '
        nomes =  input(f"nomes {cont + 1}: ")
        cont = cont + 1
        arquivo.write(f"nomes {cont + 1}: {pergunta} {nomes}\n") 
print("Respostas gravadas com sucesso.")