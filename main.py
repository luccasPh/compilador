from lexico.lexico import Lexico

with open('arquivo.txt', 'r') as file:
    data = file.read().replace('\n', '')

print(data)