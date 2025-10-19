class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):   
        return self.__tamanho


    def setTamanho(self, valor: int):
        if valor < 20 or valor > 50:
            print("fail: tamanho fora do intervalo(20 a 50)")

        elif valor % 2 != 0  :
            print("fail: tamanho deve ser número par")  

        else:
            self.__tamanho = valor

            print("tamanho válido!") 


chinela = Chinela()

for tamanho in [15, 41, 40]:
    print("Tentando tamanho:", tamanho)
    chinela.setTamanho(tamanho)
    if chinela.getTamanho() != 0:
        break
        
print("Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())