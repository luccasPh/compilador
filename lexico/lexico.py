from lexico.identificador import Identificador as iden
from lexico.digito import Digito as digi
from lexico.simbolo_especial import SimboloEspecial as simb
from lexico.comentario import Comentario as come

import re

class Lexico:
    #metodo que inicializa as variaveis da classe
    def __init__(self):
        self.tolken = "" #armazena o tolken gerado pelos automos
        self.estado = "q0" #guarda o estado do automo selecionado
        self.auto = 0 #seleciona o automo
    
    def analisador(self, arquivo):
        for linha in arquivo.readlines():
            linha += "\n" #gambiarra para fazer reconhecer ultimo caracter do arquivo
            i = 0
            while i < len(linha):
                #seleciona o automo com base no caracter da linha selecionada
                if self.auto == 0:
                    if linha[i:2] == "@@" or linha[i:2] == "//" or linha[i:2] == "..":
                        self.auto = 1

                    elif iden.automoto(linha[i], self.estado):
                        self.auto = 2
                    
                    elif linha[i] == "-":
                        if re.match(r"[0-9]", linha[i+1]):
                            self.auto = 3

                        else:
                            self.auto = 4

                    elif digi.automoto(linha[i], self.estado):
                        self.auto = 3

                    elif simb.automoto(linha[i], self.estado):
                        self.auto = 4
                    
                    else:
                        i += 1

                #automo de cometario quando for selecionado
                elif self.auto == 1:
                    #encerra o automato
                    if self.estado == "q4":
                        print("Comentario")
                        
                        #limpa o tolken e reinicia o estado e automoto
                        self.tolken = ""
                        self.estado = "q0"
                        self.auto = 0
                    
                    else:
                        #verifica se o caracter e valido no automato
                        self.estado = come.automoto(linha[i], self.estado)
                        i += 1
                        
                #automo de identificador/palavra reservada quando for selecionado
                elif self.auto == 2:
                    #verifica se o caracter e valido no automato
                    if iden.automoto(linha[i], self.estado):
                        self.estado = iden.automoto(linha[i], self.estado)
                        self.tolken += linha[i]
                        i += 1
                    
                    else:
                        #encerra o automato
                        if self.estado == "q1" or self.estado == "q3":
                            #verifica se e palavra reservada
                            if iden.palavra_reservada(self.tolken):
                                print(f"RESERVADO: [{self.tolken}]")
                            
                            else:
                                print(f"INDENTIFICADOR: [{self.tolken}]")
                        
                        else:
                            print(f"ERROR: [{self.tolken}]")

                        #limpa o tolken e reinicia o estado e automoto
                        self.tolken = ""
                        self.estado = "q0"
                        self.auto = 0
                
                #automo de digito quando for selecionado
                elif self.auto  == 3:
                    #verifica se o caracter e valido no automato
                    if digi.automoto(linha[i], self.estado):
                        self.estado = digi.automoto(linha[i], self.estado)
                        self.tolken += linha[i]
                        i += 1
                    
                    #encerra o automato
                    else:
                        if self.estado == "q1-1" or self.estado == "q3":
                            print(f"DIGITO: [{self.tolken}]")
                        
                        else:
                            print(f"ERROR: [{self.tolken}]")
                        #limpa o tolken e reinicia o estado e automoto
                        self.tolken = ""
                        self.estado = "q0"
                        self.auto = 0

                #automo de digito quando for selecionado
                elif self.auto == 4:
                    #verifica se o caracter e valido no automato
                    if simb.automoto(linha[i], self.estado):
                        self.estado = simb.automoto(linha[i], self.estado)
                        self.tolken += linha[i]
                        i += 1
                    
                    #encerra o automato
                    else:
                        if self.estado == "q1-1" or self.estado == "q1-2" or self.estado == "q2":
                            print(f"SIMBOLO: [{self.tolken}]")
                        
                        else:
                            print(f"ERROR: [{self.tolken}]")
                        
                        #limpa o tolken e reinicia o estado e automoto
                        self.tolken = ""
                        self.estado = "q0"
                        self.auto = 0
        
        #verifica no final se automoto de cometario ainda esta selecionado
        if self.auto == 1:
            print("ERRO NO COMETARIO")