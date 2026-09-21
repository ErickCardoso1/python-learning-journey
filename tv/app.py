from rich import print
from rich.traceback import install
from rich import inspect
from rich.panel import Panel

import os


install()
class Tv:
    def __init__(self, modelo):
        self.modelo = modelo
        self.canal = 1
        self.volume = 0
        self.ligado = False
        self.verCanal = '[red]1[/] 2 3 4 5'
        self.verVolume = '■■■■■'
    
    def avancar_canal(self):
        if self.ligado:
            if self.canal == 5:
                self.canal = 1
                return
            self.canal += 1
    def voltar_canal(self):
        if self.ligado:
            if self.canal == 1:
                self.canal = 5
                return
            self.canal -= 1
        
    def aumentar_volume(self):
        if self.ligado:
            if self.volume == 5:
                return
            self.volume += 1
        
    def diminuir_volume(self):
        if self.ligado:
            if self.volume == 0:
                return
            self.volume -= 1

    def desligarLigar(self):
        self.ligado = not self.ligado
    
    def mostrarTv(self):
        if self.ligado:
            match self.canal:
                case 1: self.verCanal = '[red]1[/] 2 3 4 5'
                case 2: self.verCanal = '1 [red]2[/] 3 4 5'
                case 3: self.verCanal = '1 2 [red]3[/] 4 5'
                case 4: self.verCanal = '1 2 3 [red]4[/] 5'
                case 5: self.verCanal = '1 2 3 4 [red]5[/]'
            match self.volume:
                case 0: self.verVolume = '■■■■■'
                case 1: self.verVolume = '[red]■[/]■■■■'
                case 2: self.verVolume = '[red]■■[/]■■■'
                case 3: self.verVolume = '[red]■■■[/]■■'
                case 4: self.verVolume = '[red]■■■■[/]■'
                case 5: self.verVolume = '[red]■■■■■[/]'

            painel = Panel(f'''
            
            
            Canal = {self.verCanal}\n
            Volume = {self.verVolume}
            
            
            ''', title=self.modelo, width=50)
            print(painel)
        else:
            painel = Panel(f'''
            
            
            [red]{self.modelo} DESLIGADA[/]
            
            
            ''', title=self.modelo, width=50)
            print(painel)

class ControleRemoto:
    def __init__(self, objTv: object):
        self.objTv = objTv
    
    def botao_apertado(self, tipo):

        match tipo:
            case '>': self.objTv.avancar_canal()
            case '<': self.objTv.voltar_canal()
            case '-': self.objTv.diminuir_volume()
            case '+': self.objTv.aumentar_volume()
            case '@': self.objTv.desligarLigar()



tv1 = Tv('Smart TV')
c1 = ControleRemoto(tv1)

while(True):

    os.system('cls')
    tv1.mostrarTv()
    print(f' @ {"[red]OFF[/]" if tv1.ligado else "[green]ON[/]"} < CH{tv1.canal} >  - VOL{tv1.volume} + : ')
    choice = str(input())
    if choice in ('>', '<', '-', '+', '@'):
        c1.botao_apertado(choice)
    elif choice == '0':
        exit()
    elif choice == '1':
        inspect(tv1)
        exit()