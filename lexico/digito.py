import re

class Digito:

    def automoto(entrada):
        estado = "0"
        i = 0
        while i < len(entrada):
            simb = entrada[i]
            if estado == "0":
                if re.match(r"[0-9]", simb) != None:
                    estado = "1A"

                elif simb == "-":
                    estado = "1B"
                
                else:
                    estado = "0"
            
            elif estado == "1A":
                if re.match(r"[0-9]", simb) != None:
                    estado = "2A"
                
                elif simb == ",":
                    estado = "1B"

                else:
                    estado = None 

            elif estado == "1B":
                if re.match(r"[0-9]", simb) != None:
                    estado = "1A"
                
                else:
                    break
            
            elif estado == "2A":
                if re.match(r"[0-9]", simb) != None:
                    estado = "2A"
                
                else:
                    break
            
            i += 1

        if estado == "2A" or estado == "1A":
            return True

        else:
            return False