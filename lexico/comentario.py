import re

class Comentario:

    #automoto para gera o tolken
    @staticmethod
    def automoto(simb, estado):
        if estado == "q0":
            if simb == "/":
                return "q1-1"
            
            elif simb == ".":
                return "q1-2"
            
            elif simb == "@":
                return "q1-3"
            
            else:
                return False
        
        elif estado == "q1-1":
            if simb  == "/":
                return "q2-1"
            
            else:
                return False
        
        elif estado == "q1-2":
            if simb  == ".":
                return "q2-2"
            
            else:
                return False
        
        elif estado == "q1-3":
            if simb  == "@":
                return "q2-3"
            
            else:
                return False
        
        elif estado == "q2-1":
            if simb  == "/":
                return "q3-1"
            
            else:
                return "q2-1"
        
        elif estado == "q2-2":
            if simb  == ".":
                return "q3-2"
            
            else:
                return "q2-2"
        
        elif estado == "q2-3":
            if simb  == "\n":
                return "q4"
            
            else:
                return "q2-3"
        
        elif estado == "q3-1":
            if simb  == "/":
                return "q4"
            
            else:
                return "q2-1"
        
        elif estado == "q3-2":
            if simb  == ".":
                return "q4"
            
            else:
                return "q2-2"    