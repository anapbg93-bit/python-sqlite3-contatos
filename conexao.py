import sqlite3
con = sqlite3.connect("nome_do_banco.bd")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS contato(nome,endereco,telefone)")
print("---CADASTRO DE CONTATO---")
novo_nome = input("Digite o nome: ")
novo_end = input("Digite o endereço: ")
novo_tel = input("Digite o telefone: ")

cur.execute("INSERT INTO contato VALUES (?, ?, ?)", (novo_nome, novo_end, novo_tel))
con.commit()

print('\nDADOS salvos com sucesso!')
print('---------------------------')
print("Lista atualizada:")
res = cur.execute("SELECT * FROM contato")
for linha in res.fetchall():
    print(linha)

con.close()