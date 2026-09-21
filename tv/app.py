from rich import print
from rich.traceback import install
from rich.panel import Panel

install()
class Tv:
    def __init__(self, modelo):
        self.modelo = modelo
        self.canal = 1
        self.verCanal = '[yellow]1[/] 2 3 4 5'
    
    def avancar_canal(self):
        if self.canal == 5:
            self.canal = 1
            return
        self.canal += 1
    
    def mostrarTv(self):
        match self.canal:
            case 1: self.verCanal = '[yellow]1[/] 2 3 4 5'
            case 2: self.verCanal = '1 [yellow]2[/] 3 4 5'
            case 3: self.verCanal = '1 2 [yellow]3[/] 4 5'
            case 4: self.verCanal = '1 2 3 [yellow]4[/] 5'
            case 5: self.verCanal = '1 2 3 4 [yellow]5[/]'
        
        painel = Panel(self.verCanal, title=self.modelo)
        print(painel)

class ControleRemoto:
    def __init__(self, objTv: object):
        self.objTv = objTv
    
    def botao_avancar_canal(self, apertou):

        if apertou == True:
            self.objTv.avancar_canal()




tv1 = Tv('Smart TV')
c1 = ControleRemoto(tv1)

tv1.mostrarTv()