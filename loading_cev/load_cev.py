import numpy as np
import matplotlib.pyplot as plt

def loading_cev(file_path):
    with open(f'{file_path}') as f:
        lines = f.readlines()
        nomes_canais = lines[6].split(',')
        nomes_geral = lines[4].split(',')

        keys_dados_analogicos = []
        keys_geral = []

    for nomes in nomes_canais:
        keys_dados_analogicos.append(nomes.replace('"', ""))

    for nomes in nomes_geral:
        keys_geral.append(nomes.replace('"', ""))

    dict_info_geral = dict(zip(keys_geral, lines[5].split(',')))
    count = 0
    dados = []
    for line in lines:
        count += 1
        colunas = line.split(',')
        if colunas[0] == '"SETTINGS"':
            break
        else:
            if count > 7:
                dados.append(colunas)

    array_dados = np.array(dados)
    array_dados = array_dados.T

    fim_analogicos = np.where(array_dados == ' ')

    lista_array = []
    for i in range(0, fim_analogicos[0][0]):
        array_dadod_float = array_dados[i].astype(np.float32)
        lista_array.append(array_dadod_float)
    dict_dados_analogicos = dict(zip(keys_dados_analogicos, lista_array))

    return dict_dados_analogicos, dict_info_geral


if __name__ == '__main__':

    canais_analogicos, informacoes = loading_cev(r'C:\Users\Helena\PycharmProjects\loadingcev\oscilografias\CEV_S128_R_L60_10154.CEV')
    plt.plot(canais_analogicos['IN'])
    plt.show()
