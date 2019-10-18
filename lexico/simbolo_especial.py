import re

class SimboloEspecial:
    
    def automoto(entrada):
        estado = 0
        i = 0
        while i < len(entrada):
            simb = entrada[i]
            if estado == 0:
                if re.match(r"[.;,*()={}|@]", simb):
                    estado = None

                elif re.match(r"[+-<>:]", simb):
                    estado = 1

                else:
                    break
            
            elif estado == 1:
                if re.match(r"[=>]", simb):
                    estado = 2
                
                else:
                    estado = None
            
            i += 1
        
        if estado == 1 or estado == 2:
            return True

        else:
            return False


