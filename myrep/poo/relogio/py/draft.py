

# 1. controle atraves de gets e sets
# 2. controle iniciando e usando os sets no construtor
# 3. parametros nomeados

# Definir valores de forma controlada
class Hora:
    def __init__(self, h: int = 0, m: int = 0): # parametro default
        self.__hora: int = 0
        self.__min: int = 0
        self.set_hora(h) # validação dentro do init
        self.set_min(m)

    def set_hora(self, value: int): # escrita
        if value < 0 or value > 23:
            print("fail: hora invalida")
            return self
        self.__hora = value
        return self

    def set_min(self, value: int): # escrita
        if value < 0 or value > 59:
            print("fail: minuto invalido")
            return self
        self.__min = value
        return self

    def get_hora(self) -> int: # leitura
        return self.__hora
    
    def get_min(self) -> int:
        return self.__min

agora = Hora()

print(agora.get_hora())
print(agora.get_min())