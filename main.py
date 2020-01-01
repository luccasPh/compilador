from lexico.lexico import Lexico

arquivo = open("teste1.txt", "r")

#inicializar o lexico
lexico = Lexico()

#analisa o arquivo passado
res = lexico.analisador(arquivo)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))