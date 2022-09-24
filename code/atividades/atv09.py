"""
Crie uma classe em pyhton conforme o diagrama. 

Crie um objeto setando os valores por meio do método construtor.

Em seguida faça um método chamado toString para printar 
na tela todos os atributos da classe.
"""

class Veiculo:
    def __init__(self):
        self.modelo = "Corolla"
        self.portas = "4"
        self.cor = "Prateado"
        self.ano = "2022"

    def toString(self):
        print("Informacoes do Veiculo:\n")
        print("Modelo: ", self.modelo)
        print("Qtd. Portas: ", self.portas)
        print("Cor: ", self.cor)
        print("Ano: ", self.ano)

carro = Veiculo()

carro.toString()
