# CORRIGIDO
from desafios.desafio040.classe040 import *

def main():
    u = [Usuario("José", "jjsilva@hotmail.com"),
         Usuario("Ana", "aninha@gmail.com")]
    a = [Aluno("Maria", "Administração", "3º ano"),
         Aluno("Paulo", "Gastronomia", "1º ano")]

    exportar_dados(XML(), a)
    exportar_dados(JSON(), u)


if __name__ == "__main__":
    main()