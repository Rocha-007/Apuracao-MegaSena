import csv
import random
import string


def gerar_id():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"AP-{codigo}"


def gerar_numeros():
    return sorted(random.sample(range(1, 61), 6))


def gerar_csv(nome_arquivo="apostas.csv", quantidade_linhas=10):
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        for _ in range(quantidade_linhas):
            identificador = gerar_id()
            numeros = gerar_numeros()

            escritor.writerow([identificador] + numeros)


if __name__ == "__main__":
    gerar_csv()
    print("Arquivo apostas.csv gerado com sucesso!")