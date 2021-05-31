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
    lista_array_analogicos = []
    trig_counter = 0
    for i in keys_dados_analogicos:
        if i == 'TRIG':
            break
        trig_counter += 1

    for i in range(0, trig_counter):
        array_dados_float_analogicos = array_dados[i].astype(np.float32)
        lista_array_analogicos.append(array_dados_float_analogicos)

    indice_aster = np.where(array_dados[trig_counter] == '"*"')
    indice_maior = np.where(array_dados[trig_counter] == '">"')

    if indice_maior:
        trig = indice_maior[0]
    else:
        if indice_aster:
            trig = indice_aster[0]
        else:
            trig = 0

    lista_array_analogicos.append(trig)

    dict_dados_analogicos = dict(zip(keys_dados_analogicos, lista_array_analogicos))

    return dict_dados_analogicos, dict_info_geral


if __name__ == '__main__':

    canais_analogicos, informacoes = loading_cev(r'C:\Users\Helena\PycharmProjects\loadingcev\oscilografias\CEV_10377_R.CEV')
    print(canais_analogicos.keys())
    print(canais_analogicos['TRIG'])
    plt.plot(canais_analogicos['IN(A)'])
    plt.show()
