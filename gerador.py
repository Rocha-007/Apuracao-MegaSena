import csv
import random
import string
import sys


def gerar_id():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"AP-{codigo}"


def gerar_numeros(quantidade=6):
    return sorted(random.sample(range(1, 61), quantidade))


def validar_aposta(numeros):
    return 6 <= len(numeros) <= 15


def gerar_csv(nome_arquivo, quantidade_linhas):
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        linhas_geradas = 0

        while linhas_geradas < quantidade_linhas:
            identificador = gerar_id()

            quantidade_numeros = random.randint(6, 15)
            numeros = gerar_numeros(quantidade_numeros)

            if validar_aposta(numeros):
                escritor.writerow([identificador] + numeros)
                linhas_geradas += 1


def main():
    if len(sys.argv) != 2:
        print("Uso: py gerador.py <quantidade_de_linhas>")
        sys.exit(1)

    try:
        quantidade_linhas = int(sys.argv[1])
    except ValueError:
        print("Erro: a quantidade de linhas deve ser um número inteiro.")
        sys.exit(1)

    if quantidade_linhas <= 0:
        print("Erro: a quantidade de linhas deve ser maior que zero.")
        sys.exit(1)

    gerar_csv("apostas.csv", quantidade_linhas)

    print(
        f"Arquivo apostas.csv gerado com "
        f"{quantidade_linhas} linhas."
    )


if __name__ == "__main__":
    main()