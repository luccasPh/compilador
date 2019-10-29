import re

class Identificador:
    #verifica se o tolken e palavara reservada
    @staticmethod
    def palavra_reservada(entrada):
        reservada = [
            "programa", 
            "se", 
            "entao", 
            "senao", 
            "enquanto", 
            "faca", 
            "ate", 
            "repita", 
            "inteiro", 
            "real",
            "caractere", 
            "caso", 
            "escolha", 
            "fimescolha", 
            "procedimento", 
            "funcao", 
            "de", 
            "para", 
            "fimse",
            "inicio", 
            "fim"
        ]
        
        if entrada in reservada:
            return True
        
        else:
            return False

    #automoto para gera o tolken
    @staticmethod
    def automoto(simb, estado):
        if estado == "q0":
            if re.match(r"[aA-zZ]", simb):
                return "q1"
            
            else:
                return False

        elif estado == "q1":
            if simb == "-":
                return "q2"
                
            elif re.match(r"[a-z0-9]", simb):
                return "q1"
            
            else:
                return False

        elif estado == "q2":
            if re.match(r"[a-z]", simb):
                return "q3"
            
            else:
                return False

        elif estado == "q3":
            if re.match(r"[a-z0-9]", simb):
                return "q1"
            
            else:
                return False
