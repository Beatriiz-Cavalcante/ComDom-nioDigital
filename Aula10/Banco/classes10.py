'''Crie uma classe que tenha os atributos, número da conta, saldo, statuss da conta (se ela está ativa ou não), nome
do cliente, tipo da conta, e que possibilite ao cliente, depositar, sacar, verificar saldo e possibilidade de ativar
a conta ou desativar a conta. Para desativar uma conta é necessário que o saldo esteja zerado'''

class ContaBancaria():
    def __init__(self, numeroConta, nomeCliente, tipoConta):
        self.numeroConta = numeroConta
        self.nomeCliente = nomeCliente
        self.tipoConta = tipoConta
        self.saldo = 0.0
        self.status = False

    def ativaConta(self):
        if self.status == False:
            self.status = True
            print("Conta Ativada com sucesso")
        else:
            print("A conta já estava ativa!")

    def desativaConta(self):
        if self.status == True:
            if self.saldo > 0:
                print(f"O saldo atual da conta é {self.saldo}. Para que a conta seja desativada é necessário que esteja zerado")
                self.sacar(self.saldo)
                print(f"Saldo atual igual a {self.saldo}. Agora a conta será desativada...")
                self.status = False
                print(f"A conta de número {self.numeroConta} pertencente a {self.nomeCliente} do tipo {self.tipoConta} está desativa")
            else:
                print(f"Saldo atual igual a {self.saldo}. Agora a conta será desativada...")
                self.status = False
                print(f"A conta de número {self.numeroConta} pertencente a {self.nomeCliente} do tipo {self.tipoConta} está desativa")
        else:
            print("A conta já estava desativa!")
    def depositar(self,valorDeposito):
        if self.status == True:
            self.saldo = self.saldo + valorDeposito
        else:
            print("Essa conta não existe")

    def sacar(self, valorSaque):
        if self.status == True:
            if valorSaque > self.saldo:
                print("Saldo insuficiente")
            else:
                self.saldo = self.saldo - valorSaque
        else:
            print("Essa conta não existe")

    def verificaSaldo(self):
        if self.status == True:
            print(f"O saldo atual é de {self.saldo}")
        else:
            print("Essa conta não existe")









