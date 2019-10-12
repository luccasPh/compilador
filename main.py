from identificador import Indentificador as iden
from digito import Digito as digi
from comentario import Comentario as come
from simbolo_especial import SimboloEspecial as simb

arquivo = open("arquivo.txt", "r")

cometario  = False
for linhas in arquivo.readlines():
    entradas = linhas.split(" ")

    if come.automoto(linhas):
        if linhas[0] in '@' and linhas[-1] in '\n':
            print("Cometario reconhecido")
            cometario = False
        
        elif linhas[0] in '/' and linhas[-1] in '/':
            print("Cometario reconhecido")
            cometario = False

        elif not cometario:
            cometario = True

        else:
            cometario = False
            print("Cometario reconhecido")
    
    elif not cometario:
        for entrada in entradas:
            entrada = entrada.replace("\n", "")

            if iden.automoto(entrada):
                print(f"[{entrada}] Reconhecido como indetificador")
                pass
            
            elif digi.automoto(entrada):
                print(f"[{entrada}] Reconhecido como digito")
                pass
            
            elif simb.automoto(entrada):
                print(f"[{entrada}] Reconhecido como simbolo especial")
                pass
                
            else:
                print(f"[{entrada}] Entrada não reconhecida")
    

if cometario:
    print("Comentario não reconhecido")