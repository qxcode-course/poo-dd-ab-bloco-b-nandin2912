class Camisa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self):
        return self.__tamanho  

    def setTamanho(self, valor: str):
        tamanhos_validos = ["pp", "p", "m", "g", "gg", "xg"]
        if valor in tamanhos_validos:
            self.__tamanho = valor

        else:
            print("fail: tamanho invalido. Valores permitidos", ", ".join(tamanhos_validos))



camisa = Camisa()
entradas = ["xp", "xx", "m", "xg"]

for tentativa in entradas:
    print(f"Digitando: {tentativa}")
    camisa.setTamanho(tentativa.upper())
    if camisa.getTamanho() != "":
        break

print("Parabéns, você comprou uma roupa tamanho", camisa.getTamanho())
