from lexico.identificador import Identificador as iden
from lexico.digito import Digito as digi
from lexico.simbolo_especial import SimboloEspecial as simb
from lexico.comentario import Comentario as come

import re, sys

class Lexico:
    #metodo que inicializa as variaveis da classe
    def __init__(self):
        self.tolken_value = "" #armazena o tolken gerado pelos automos
        self.estado = "q0" #guarda o estado do automo selecionado
        self.auto = 0 #seleciona o automo
        self.tolken_id = ""
        self.linha = 0
        self.error = False
    
    def selecionar_automoto(self, linha, i):
        if re.match(r"[ \n\t]", linha[i]):
            return False
        
        elif linha[i] == "@" or linha[i] == "/" or linha[i] == ".":
            if linha[i+1] == "@" or linha[i+1] == "/" or linha[i+1] == ".":
                self.auto = 1
            
            else:
                self.auto = 4

            return True

        elif iden.automoto(linha[i], self.estado):
            self.auto = 2

            return True
        
        elif linha[i] == "-":
            if re.match(r"[0-9]", linha[i+1]):
                self.auto = 3

            else:
                self.auto = 4

            return True

        elif digi.automoto(linha[i], self.estado):
            self.auto = 3

            return True

        elif simb.automoto(linha[i], self.estado):
            self.auto = 4

            return True
        
    
    def chamar_automoto(self, linha, i):

        #automo de cometario
        if self.auto == 1:

            #encerra o automato
            if self.estado == "q4":
                self.tolken_value = ""
                self.estado = "q0"
                self.auto = 0
                self.tolken_id = ""

                return False
            
            else:
                #verifica se o caracter e valido no automato
                self.estado = come.automoto(linha[i], self.estado)
                
                return True
                
        #automo de identificador/palavra reservada quando for selecionado
        elif self.auto == 2:

            #verifica se o caracter e valido no automato
            if iden.automoto(linha[i], self.estado):
                self.estado = iden.automoto(linha[i], self.estado)
                self.tolken_value += linha[i]
                
                return True
            
            else:
                #encerra o automato
                if self.estado == "q1" or self.estado == "q3":
                    #verifica se e palavra reservada
                    if iden.palavra_reservada(self.tolken_value):
                        self.tolken_id = self.tolken_value
                        return 'ok'
                    
                    else:
                        self.tolken_id = "identificador"
                        return 'ok'
                
                else:
                    return -1
        
        #automo de digito quando for selecionado
        elif self.auto  == 3:

            #verifica se o caracter e valido no automato
            if digi.automoto(linha[i], self.estado):
                self.estado = digi.automoto(linha[i], self.estado)
                self.tolken_value += linha[i]
                
                return True
            
            #encerra o automato
            else:
                if self.estado == "q1-1" or self.estado == "q3":
                    self.tolken_id = "digito"
                    return 'ok'
                
                else:
                    return -1

        #automo de simbolo quando for selecionado
        elif self.auto == 4:

            #verifica se o caracter e valido no automato
            if simb.automoto(linha[i], self.estado):
                self.estado = simb.automoto(linha[i], self.estado)
                self.tolken_value += linha[i]
                
                return True
            
            #encerra o automato
            else:
                if self.estado == "q1-1" or self.estado == "q1-2" or self.estado == "q1-3" or self.estado == "q2":
                    self.tolken_id = self.tolken_value
                    return 'ok'
                
                else:
                    return -1

    
    def analisador(self, arquivo):
        for linha in arquivo.readlines():
            self.linha += 1
            linha += "\n"
            i = 0
            while i < len(linha):
                #seleciona o automo com base no caracter da linha selecionada
                if self.auto == 0:
                    if not self.selecionar_automoto(linha, i):
                        i += 1
                
                else:
                    situ = self.chamar_automoto(linha, i)
                    if situ == -1:
                        print(f"ERROR Lexico linha {self.linha}: {self.tolken_value}")
                        self.error = True
                        sys.exit()

                    elif situ == True:
                        i += 1
                            
                    elif situ == 'ok':
                        self.tolken_value = ""
                        self.estado = "q0"
                        self.auto = 0

                        yield self.tolken_id
                
        #verifica no final se automoto de cometario ainda esta selecionado
        if self.auto == 1:
            print(f"ERROR Lexico linha {self.linha}: cometario não fechado")
            self.error = True
            sys.exit()