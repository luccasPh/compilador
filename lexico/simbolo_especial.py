import re

class SimboloEspecial:
    #automoto para gera o tolken
    @staticmethod
    def automoto(simb, estado):
        if estado == "q0":
            if re.match(r"[.;,*/(){}|@]", simb):
                return "q2"

            elif re.match(r"[-+>:]", simb):
                return "q1-1"
            
            elif simb == "<":
                return "q1-2"
            
            elif simb == "=":
                return "q1-3"

            else:
                return False

        elif estado == "q1-1":
            if re.match(r"[=]", simb):
                return "q2"
            
            else:
                return False

        elif estado == "q1-2":
            if re.match(r"[>=]", simb):
                return "q2"
            
            else:
                return False
        
        elif estado == "q1-3":
            if simb == ">":
                return "q2"
            
            else:
                return False


