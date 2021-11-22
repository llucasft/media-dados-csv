import csv

media_living = 0
media_lot = 0
media_above = 0


def calculo_media(txt, lista):
    print(txt)
    # Somando o Total de Square Feet e a quantidade de casas
    quantidade_lista = 0
    total_lista = 0

    for valor in lista:
        # Quantidade de casas
        valor = int(valor)
        quantidade_lista = float(quantidade_lista + 1)
        # Total Square Feet
        total_lista += valor
    print('Total de cômodos: {}'.format(quantidade_lista))
    print('Total sqft: {}'.format(total_lista))
    # Pegando a média do Total Square Feet dividido pelo total de casas
    media = float(total_lista / quantidade_lista)
    media = round(media, 2)
    # Resultado da divisão
    print(f'Média igual a {media:.2f}')
    print('-' * 30)
    return media


living = []
lot = []
above = []


with open("C:/Users/USUARIO/desafiopython/kchousedata.csv", mode="r") as arq:

    tabela = csv.reader(arq, delimiter=',')

    # Lendo a tabela linha por linha e separando as colunas que vou utilizar
    for l in tabela:
        living.append(l[5])
        lot.append(l[6])
        above.append(l[12])

    # Removendo os nomes das colunas para não interferir na soma
    living.pop(0)
    lot.pop(0)
    above.pop(0)

    media_living = calculo_media(txt='SQFT_LIVING', lista=living)

    media_lot = calculo_media(txt='SQFT_LOT', lista=lot)

    media_above = calculo_media(txt='SQFT_ABOVE', lista=above)

    espaços = ['sqft_living', 'sqft_lot', 'sqft_above']
    comodos = [media_living, media_lot, media_above]
    posição = 0

    with open("C:/Users/USUARIO/desafiopython/resultado.csv", mode="w", newline='') as resultado:

        campos = ['comodo', 'media']

        criador = csv.DictWriter(resultado, fieldnames=campos)

        criador.writeheader()

        for ambiente in comodos:
            criador.writerow({'comodo': espaços[posição], 'media': comodos[posição]})
            posição += 1
