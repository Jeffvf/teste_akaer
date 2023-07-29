import pandas as pd
import time

def le_dados_licencas (filename):
    dados = pd.read_excel('Input_Teste_Python_Dados Exercicio 4 I.xlsx')
    dados.loc[:, 'Start Time'] = pd.to_datetime(dados['Start Time'], dayfirst=True)
    dados.loc[:, 'End Time'] = pd.to_datetime(dados['End Time'])

    return dados

def le_dados_usuario (filename):
    dados = pd.read_excel('Input_Teste_Python_Dados Exercício 4 II.xlsx')

    dados['Tempo Inicio'] = pd.to_datetime(dados['Data Inicio'] + ' ' + dados['Hora Inicio'])
    dados['Tempo Termino'] = pd.to_datetime(dados['Data Termino'] + ' ' + dados['Hora Termino'])

    return dados

def main():
    inicio = time.time()
    dados_licencas = le_dados_licencas('Input_Teste_Python_Dados Exercicio 4 I.xlsx')
    dados_usuario = le_dados_usuario('Input_Teste_Python_Dados Exercício 4 II.xlsx')

    usuarios_licencas = dados_licencas.merge(dados_usuario, left_on=['Start Time', 'End Time'], right_on=['Tempo Inicio', 'Tempo Termino'], how='left')

    usuarios_licencas = usuarios_licencas[['Usuario', 'Start Time', 'End Time']]

    # preenche nomes que nao foram encontrados com 'Unknown'
    usuarios_licencas['Usuario'] = usuarios_licencas['Usuario'].fillna('Unknown')

    usuarios_licencas.to_excel('ex_4_output.xlsx', index=False)

    fim = time.time()

    tempo_execucao = fim - inicio

    print(f"Tempo de execução: {tempo_execucao:.2f} segundos")

if __name__ == '__main__':
    main()