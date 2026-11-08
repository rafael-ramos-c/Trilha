import json

class Transacao:
    def __init__(self, descricao, valor, tipo):
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo

    def exibir(self):
        print(f"Descrição: {self.descricao}")
        print(f"Valor: {self.valor:.2f}")
        print(f"Tipo: {self.tipo}")

class ControleFinanceiro:
    def __init__(self):
        self.transacoes = []
        self.carregar_transacoes()

    def adicionar_transacoes(self, transacao):
        self.transacoes.append(transacao)
        self.salvar_transacoes()
        print("Transação adicionada com sucesso!")

    def listar_transacoes(self):
        if len(self.transacoes) == 0:
            print("Nenhuma transação cadastrada")
        else:
            for transacao in self.transacoes:
                transacao.exibir()
                print("--------------------")

    def calcular_saldo(self):
        saldo = 0

        for transacao in self.transacoes:
                if transacao.tipo == "Receita":
                    saldo += transacao.valor
                elif transacao.tipo == "Despesa":
                    saldo -= transacao.valor

        return saldo


    def salvar_transacoes(self):
        dados = []

        for transacao in self.transacoes:
            dados.append({
                "descricao": transacao.descricao,
                "valor": transacao.valor,
                "tipo": transacao.tipo
            })

        with open("transacoes.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)



    def carregar_transacoes(self):
        try:
            with open("transacoes.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            for item in dados:
                transacao = Transacao(
                    item["descricao"],
                    item["valor"],
                    item["tipo"]
                )

                self.transacoes.append(transacao)

        except FileNotFoundError:
            pass


controle = ControleFinanceiro()

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Listar transações")
    print("4 - Consultar saldo")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    
    if opcao == "1" or opcao == "2":
        descricao = input("Descrição: ").strip()

        if descricao == "":
            print("A descrição não pode estar vazia!")
            continue

        try:
            valor = float(input("Valor: R$ ").replace(",", "."))
        except ValueError:
            print("Valor inválido! Digite um número.")
            continue

        if valor <= 0:
            print("O valor deve ser maior que zero.")
            continue

        if opcao == "1":
            tipo = "Receita"
        else:
            tipo = "Despesa"

        transacao = Transacao(descricao, valor, tipo)
        controle.adicionar_transacoes(transacao)


    elif opcao == "3":
        controle.listar_transacoes()

    elif opcao == "4":
        saldo = controle.calcular_saldo()
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "5":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida!")