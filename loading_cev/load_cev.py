import numpy as np
import matplotlib.pyplot as plt


def loading_cev(file_path):
    with open(f'{file_path}') as f:
        lines = f.readlines()
        nomes_canais = lines[6].split(',')
        nomes_geral = lines[4].split(',')

        keys_canais = []
        keys_geral = []

    for nomes in nomes_canais:
        keys_canais.append(nomes.replace('"', ""))

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
            #print(f'linha: {count}, numero de colunas: {len(colunas)}')
            if count > 7:
                dados.append(colunas)

    array = np.array(dados)
    array = array.T
    x = np.where(array == ' ')
    dados2 = []
    for i in range(0, x[0][0]):
        x = array[i].astype(np.float32)
        dados2.append(x)
    dict_dados = dict(zip(keys_canais, dados2))

    return dict_dados, dict_info_geral

if __name__ == '__main__':

    dados, info = loading_cev(r'C:\Users\Helena\PycharmProjects\loadingcev\oscilografias\CEV_10210_R.CEV')
    print(info.keys())