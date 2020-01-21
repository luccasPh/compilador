from lexico.lexico import Lexico
import sys

arquivo = open("teste1.txt", "r")


class Sintatico(Lexico):

    def __init__(self):
        Lexico.__init__(self)
        self.tolken = self.analisador(arquivo)
        self.programa()

    # PROGRAMAS E BLOCOS
    def programa(self):
        try:
            cod = "programa"
            if next(self.tolken) != "programa":
                raise Exception()

            cod = "identificador"
            if next(self.tolken) != cod:
                raise Exception()

            cod = ";"
            aux = self.linha
            if next(self.tolken) != cod:
                raise Exception()

            cod = False
            self.bloco()

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")

            sys.exit()

    def bloco(self):
        try:
            cod_tolken = next(self.tolken)
            if cod_tolken == "tipo":
                cod_tolken = self.declara_tipo()

            if cod_tolken == "var":
                cod_tolken = self.declara_var()

            while cod_tolken == "procedimento" or cod_tolken == "funcao":
                if cod_tolken == "funcao":
                    self.declara_funcao()

                else:
                    self.declara_proced()

                cod_tolken = next(self.tolken)

            if cod_tolken:
                self.comando_composto(cod_tolken)

        except:
            sys.exit()
            pass
        
        print("Tudo ok")
    # DECLARAÇOES
    def declara_tipo(self):
        try:
            cod_tolken = next(self.tolken)
            cod = "identificador"
            if cod_tolken != cod:
                raise Exception()

            while cod_tolken == "identificador":
                cod = "="
                if next(self.tolken) != "=":
                    raise Exception()

                cod = "identificador"
                if next(self.tolken) != cod:
                    raise Exception()

                cod = ";"
                aux = self.linha
                if next(self.tolken) != cod:
                    self.linha = aux
                    raise Exception()

                cod = False
                cod_tolken = next(self.tolken)

            return cod_tolken

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")

            sys.exit()

    def declara_var(self):
        try:
            cod = "identificador"
            cod_tolken = next(self.tolken)
            if cod_tolken != cod:
                raise Exception()

            while cod_tolken == "identificador":
                cod = False
                cod_tolken = self.lista_identificador(cod_tolken)

                cod = ":"
                if cod_tolken != cod:
                    raise Exception()

                cod = "identificador"
                if next(self.tolken) != cod:
                    raise Exception()

                cod = ";"
                aux = self.linha
                if next(self.tolken) != cod:
                    self.linha = aux
                    raise Exception()

                cod = False
                cod_tolken = next(self.tolken)

            return cod_tolken

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")
                return False

            sys.exit()

    def lista_identificador(self, cod_tolken):
        try:
            cod = "identificador"
            if cod_tolken != cod:
                raise Exception()

            while cod_tolken == "identificador":
                cod = False
                cod_tolken = next(self.tolken)
                if cod_tolken == ",":
                    cod = "identificador"
                    cod_tolken = next(self.tolken)
                    if cod_tolken != cod:
                        raise Exception()

                else:
                    break

            return cod_tolken

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")
                sys.exit()

            else:
                return cod_tolken

    def declara_proced(self):
        try:
            cod = "identificador"
            if next(self.tolken) != cod:
                raise Exception()

            aux = self.linha
            cod_tolken = next(self.tolken)
            if cod_tolken == "(":
                cod_tolken = next(self.tolken)
                cod = False
                cod_tolken = self.parametros_formais(cod_tolken)

                if cod_tolken == False:
                    cod = False
                    raise Exception()

            cod = ";"
            if cod_tolken != cod:
                self.linha = aux
                raise Exception()

            cod = False
            self.bloco()

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")

            sys.exit()

    def declara_funcao(self):
        try:
            cod = "identificador"
            if next(self.tolken) != cod:
                raise Exception()

            cod_tolken = next(self.tolken)
            if cod_tolken == "(":
                cod_tolken = next(self.tolken)
                cod = False
                cod_tolken = self.parametros_formais(cod_tolken)

                if cod_tolken == False:
                    cod = False
                    raise Exception()

            cod = ":"
            if cod_tolken != cod:
                raise Exception()

            cod = "identificador"
            if next(self.tolken) != cod:
                raise Exception()

            cod = ";"
            aux = self.linha
            if next(self.tolken) != cod:
                self.linha = aux
                raise Exception()

            cod = False
            self.bloco()

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")

            sys.exit()

    def parametros_formais(self, cod_tolken):
        try:
            aux = False
            while cod_tolken != ")":

                if aux:
                    cod_tolken = next(self.tolken)
                    aux = False

                if cod_tolken == "var":
                    cod_tolken = next(self.tolken)

                cod = False
                cod_tolken = self.lista_identificador(cod_tolken)

                cod = ":"
                if cod_tolken != cod:
                    raise Exception()

                cod = "identificador"
                if next(self.tolken) != cod:
                    raise Exception()

                cod = ")"
                cod_tolken = next(self.tolken)
                if cod_tolken != cod:
                    cod = ";"
                    if cod_tolken != cod:
                        raise Exception()

                    else:
                        aux = True

            cod = False
            cod_tolken = next(self.tolken)
            return cod_tolken

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")
                sys.exit()

            else:
                return False

    # COMANDOS
    def comando_composto(self, cod_tolken):
        try:
            cod = "inicio"
            if cod_tolken != cod:
                raise Exception()

            cod = "comando sem rotulo"
            cod_tolken = next(self.tolken)
            while cod_tolken != "fim":
                cod = False
                self.comando_semrotulo(cod_tolken)

                cod = "fim"
                cod_tolken = next(self.tolken)

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")

            sys.exit()

    def comando_semrotulo(self, cod_tolken):
        if cod_tolken == "identificador":
            self.comando_atribucao_procedimento()

        elif cod_tolken == "se":
            self.comando_condicional()

        elif cod_tolken == "enquanto":
            self.comando_repetitivo()

        elif cod_tolken == "leia":
            self.comando_leia()

        elif cod_tolken == "imprima":
            self.comando_imprima()

        else:
            sys.exit()

    def comando_atribucao_procedimento(self):
        try:
            cod_tolken = next(self.tolken)
            aux = self.linha
            if cod_tolken == ":=":
                cod_tolken = self.expressao()

            elif cod_tolken == "(":
                aux = self.linha
                cod_tolken = self.lista_expressoes()
                cod = ")"
                if cod_tolken != cod:
                    self.linha = aux
                    raise Exception()

                cod = ";"
                cod_tolken = next(self.tolken)

            else:
                cod = "atribuição ou procedimento"
                raise Exception

            cod = ";"
            if cod_tolken != cod:
                self.linha = aux
                raise Exception()

        except:
            print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")
            sys.exit()

    def comando_condicional(self):
        try:
            cod_tolken = self.expressao()

            cod = "entao"
            if cod_tolken != cod:
                raise Exception()

            cod = False
            cod_tolken = next(self.tolken)
            self.comando_semrotulo(cod_tolken)

            cod_tolken = next(self.tolken)
            if cod_tolken == "senao":
                cod = False
                cod_tolken = next(self.tolken)
                self.comando_semrotulo(cod_tolken)

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")

            sys.exit()

    def comando_repetitivo(self):
        try:
            aux = self.linha
            cod_tolken = self.expressao()

            cod = "do"
            if cod_tolken != cod:
                self.linha = aux
                raise Exception()

            cod = False
            cod_tolken = next(self.tolken)
            self.comando_semrotulo(cod_tolken)

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")

            sys.exit()

    def comando_leia(self):
        try:
            cod = "("
            aux = self.linha
            cold_tolken = next(self.tolken)
            if cold_tolken != cod:
                self.linha = aux
                raise Exception()

            cod = "identificador"
            cold_tolken = next(self.tolken)

            cod = False
            aux = self.linha
            cold_tolken = self.lista_identificador(cold_tolken)

            cod = ")"
            if cold_tolken != ")":
                self.linha = aux
                raise Exception()

            cod = ";"
            aux = self.linha
            cold_tolken = next(self.tolken)
            if cold_tolken != ";":
                self.linha = aux
                raise Exception()

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")

            sys.exit()

    def comando_imprima(self):
        try:
            cod = "("
            aux = self.linha
            cold_tolken = next(self.tolken)
            if cold_tolken != cod:
                self.linha = aux
                raise Exception()

            cod = False
            aux = self.linha
            cold_tolken = self.lista_expressoes()

            cod = ")"
            if cold_tolken != ")":
                self.linha = aux
                raise Exception()

            cod = ";"
            aux = self.linha
            cold_tolken = next(self.tolken)
            if cold_tolken != ";":
                self.linha = aux
                raise Exception()

        except:
            if cod and not self.error:
                print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")

            sys.exit()

    # EXPRESSOES
    def lista_expressoes(self):
        cod_tolken = self.expressao()

        while True:
            if cod_tolken == "identificador":
                cod_tolken = self.expressao()

            elif cod_tolken == "digito":
                cod_tolken = self.expressao()

            elif cod_tolken == "(":
                cod_tolken = self.expressao()
                

            else:
                break

        return cod_tolken

    def expressao(self):
        cod_tolken = self.expressao_simples()

        if cod_tolken == "=" or cod_tolken == "<" or cod_tolken == "<=" or cod_tolken == ">" or cod_tolken == "=>":
            cod_tolken = self.expressao_simples()

        return cod_tolken

    def expressao_simples(self):

        cod_tolken = self.termo()
        while True:
            if cod_tolken == "+":
                cod_tolken = self.termo()

            elif cod_tolken == "-":
                cod_tolken = self.termo()

            elif cod_tolken == "ou":
                cod_tolken = self.termo()

            else:
                break

        return cod_tolken

    def termo(self):

        cod_tolken = self.fator()
        while True:
            if cod_tolken == "*":
                cod_tolken = self.fator()

            elif cod_tolken == "/":
                cod_tolken = self.fator()

            elif cod_tolken == "e":
                cod_tolken = self.fator()

            else:
                break

        return cod_tolken

    def fator(self):
        try:
            cod = "identificador, digito ou expressão"
            cod_tolken = next(self.tolken)
            if cod_tolken == "identificador":
                cod_tolken = next(self.tolken)
                if cod_tolken == "(":
                    aux = self.linha
                    cod_tolken = self.lista_expressoes()

                    cod = ")"
                    if cod_tolken != cod:
                        self.linha = aux
                        raise Exception()

                    return next(self.tolken)

                else:
                    return cod_tolken

            elif cod_tolken == "digito":
                return next(self.tolken)

            elif cod_tolken == "(":
                aux = self.linha
                cod_tolken = self.expressao()

                cod = ")"
                if cod_tolken != cod:
                    self.linha = aux
                    raise Exception()

                return next(self.tolken)

            else:
                raise Exception()

        except:
            print(f"ERROR Semântico linha {self.linha}: '{cod}' esperado")
            sys.exit()
