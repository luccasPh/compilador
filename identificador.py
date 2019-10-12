import re

class Indentificador:

    def automoto(entrada):
        estado = 0
        i = 0
        while i < len(entrada):
            simb = entrada[i]
            if estado == 0:
                if re.match(r"[aA-zZ]", simb):
                    estado = 1
                else:
                    break
            elif estado == 1:
                if simb == "-":
                    estado = 2
                
                elif re.match(r"[a-z0-9]", simb):
                    estado = 1

                else:
                    break
            
            elif estado == 2:
                if re.match(r"[a-z]", simb):
                    estado = 3
                
                else:
                    break
            
            elif estado == 3:
                if re.match(r"[a0-z9]", simb):
                    estado = 1
                
                else:
                    break
            
            i += 1
        
        if estado == 1 or estado == 3: 
            if i == len(entrada):
                return True
            else:
                return False
        else:
            return False