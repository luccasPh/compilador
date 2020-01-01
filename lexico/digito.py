import re

class Digito:
    #automoto para gera o tolken
    @staticmethod
    def automoto(simb, estado):
        if estado == "q0":
            if re.match(r"[0-9]", simb):
                return "q1-1"

            elif simb == "-":
                return "q1-2"
            
            else:
                return False

        elif estado == "q1-1":
            if re.match(r"[0-9]", simb):
                return "q1-1"
            
            elif simb == ",":
                return "q2"
            
            else:
                False

        elif estado == "q1-2":
            if re.match(r"[0-9]", simb):
                return "q1-1"
            
            else:
                return False

        elif estado == "q2":
            if re.match(r"[0-9]", simb):
                return "q3"
            
            else:
                return False

        elif estado == "q3":
            if re.match(r"[0-9]", simb):
                return "q3"
            
            else:
                return False