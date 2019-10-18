from lexico.identificador import Indentificador as iden
from lexico.digito import Digito as digi
from lexico.comentario import Comentario as come
from lexico.simbolo_especial import SimboloEspecial as simb

class Lexico:

    def analisador(codigo):
        cometario  = False
        for linhas in codigo.readlines():

            if come.automoto(linhas):
                if linhas[0] in '@' and linhas[-1] in '\n':
                    print("Cometario")
                    cometario = False
                
                elif linhas[0] in '/' and linhas[-1] in '/':
                    print("Cometario")
                    cometario = False

                elif not cometario:
                    cometario = True

                else:
                    cometario = False
                    print("Cometario")
            
            elif not cometario:
                entradas = linhas.split(" ")
                for entrada in entradas:
                    entrada = entrada.replace("\n", "")

                    if iden.automoto(entrada):
                        if iden.reservado(entrada):
                            print(f"[{entrada}] Palavara Reservada")
                        else:
                            print(f"[{entrada}] Indetificador")
                        pass
                    
                    elif digi.automoto(entrada):
                        print(f"[{entrada}] Digito")
                        pass
                    
                    elif simb.automoto(entrada):
                        print(f"[{entrada}] Simbolo Especial")
                        pass
                        
                    else:
                        print(f"[{entrada}] Erro lexico")
            
        if cometario:
            print("Erro lexico")