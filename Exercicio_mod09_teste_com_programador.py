class Celular:
    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo
        self.bateria = 100
    

    def fazer_chamada(self,custo_bateria):
        print(f"\n---Chamada no {self.modelo}---")
        try:
            self.bateria -= custo_bateria
        except TypeError:
            print("Erro: Ocusto da bateria deve ser um número!")
        else:
            print(f"Sucesso! Bateria atual: {self.bateria}%")
        finally: 
            print("Sistema finalizado.")

