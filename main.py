from lexico.lexico import Lexico

arquivo = open("arquivo.txt", "r")

#inicializar o lexico
lexico = Lexico()

#analisa o arquivo passado
lexico.analisador(arquivo)
