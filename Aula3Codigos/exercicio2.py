
class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        salario_final = self.salario_base + self.bonus
        return salario_final


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, vendas, taxa_comissao):
        super().__init__(nome, salario_base)
        self.vendas = vendas
        self.taxa_comissao = taxa_comissao

    def calcular_salario(self):
        comissao = self.vendas * self.taxa_comissao
        salario_final = self.salario_base + comissao
        return salario_final


gerente = Gerente("Adalberto", 5000, 1000)
vendedor = Vendedor("Rodolfo", 1500, 10000, 0.05)

print(gerente.calcular_salario())
print(vendedor.calcular_salario())
