import csv
import random
import string


def gerar_id():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"AP-{codigo}"


def gerar_numeros(quantidade=6):
    return sorted(random.sample(range(1, 61), quantidade))


def validar_aposta(numeros):
    return 6 <= len(numeros) <= 15


def gerar_csv(nome_arquivo="apostas.csv", quantidade_linhas=10):
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        for _ in range(quantidade_linhas):
            identificador = gerar_id()

            quantidade_numeros = random.randint(1, 15)
            numeros = gerar_numeros(quantidade_numeros)

            if validar_aposta(numeros):
                escritor.writerow([identificador] + numeros)


if __name__ == "__main__":
    gerar_csv()
    print("Arquivo apostas.csv gerado com sucesso!")