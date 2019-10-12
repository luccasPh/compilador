import re

class Comentario:

    def automoto(entrada):
        estado = 0
        i = 0
        while i < len(entrada):
            simb = entrada[i]
            if estado == 0:
                if re.match(r"[@/.]", simb):
                    estado = 1
                else:
                    break
            
            elif estado == 1:
                if re.match(r"[@/.]", simb):
                    estado = 2
                
                else:
                    break
            
            elif estado == 2:
                if re.match(r"[\n]", simb):
                    estado = 4
                
                elif re.match(r"[/.]", simb):
                    estado = 3
            
            elif estado == 3:
                if re.match(r"[/.]", simb):
                    estado = 4

                else:
                    estado = 2
            
            elif estado == 4:
                if re.match(r"[/]", simb):
                    estado = 3
                
                else:
                    estado = 4
            
            i += 1
        
        if estado == 4:
            if i == len(entrada):
                return True

            else:
                return False
        else:
            return False