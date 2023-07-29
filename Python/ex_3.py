import pandas as pd
import datetime
import time

def le_dados(filename):
    dados_licencas = pd.read_excel(filename)
    dados_licencas = dados_licencas[['User Name', 'Start Time', 'End Time', 'License Type']]

    dados_licencas.loc[:, 'Start Time'] = pd.to_datetime(dados_licencas['Start Time'], dayfirst=True)
    dados_licencas.loc[:, 'End Time'] = pd.to_datetime(dados_licencas['End Time'])

    return dados_licencas

def atribui_id(dados):
    dados['ID'] = 0

    # atribui um id para cada username
    unique_names = dados['User Name'].unique()
    id_map = {name: i + 1 for i, name in enumerate(unique_names)}

    # adiciona o id no dataframe principal
    for i, nome in enumerate(id_map):
        dados.loc[dados['User Name'] == nome, 'ID'] = i + 1

    return dados

def soma_de_horas(user_data):
    date = []
    total = 0
    for i in range(3):
        row = user_data.iloc[i]
        if len(date) == 0:
            date.append(row['Start Time'])
            date.append(row['End Time'])
        elif date[1] > row['Start Time']:
            date.pop()
            date.append(row['End Time'])
        else:
            end_date = date.pop()
            start_date = date.pop()
            total += (end_date - start_date).total_seconds()
            
            date.append(row['Start Time'])
            date.append(row['End Time'])

    total += (date[1] - date[0]).total_seconds()
    total_hours = str(datetime.timedelta(seconds = total))
    
    return total_hours

def atribui_horas(dados):
    df = pd.DataFrame(columns=['ID', 'Username', 'Licencas', 'Dia', 'Tempo de Uso'])
    size = len(dados)
    j = 3

    for i in range(0, size, 3):
            total = soma_de_horas(dados.iloc[i:j])
            
            username = dados['User Name'][i]
            date = dados['Start Time'][i].date()
            user_id = dados['ID'][i]

            # concatena licencas utilizadas no mesmo dia
            license = dados.iloc[i: j]['License Type']
            license_str = ", ".join(license.astype(str))
            
            df.loc[len(df)] = [user_id, username, license_str, date, total]
            
            j += 3

    return df

def main():
    inicio = time.time()
    
    dados_licencas = le_dados('Input_Teste_Python_exercicio 3.xlsx')

    dados_licencas = atribui_id(dados_licencas)

    # organiza os dados de acordo com nome de usuario e 
    # data de inicio do acesso
    dados_licencas = dados_licencas.sort_values(['User Name', 'Start Time'])

    # reseta o indice para que se consiga iterar pelas linhas
    # do dataframe na ordem classificada anteriormente
    dados_licencas = dados_licencas.reset_index(drop=True)

    df = atribui_horas(dados_licencas)

    df.to_excel('ex_3_output.xlsx', index=False)
    
    fim = time.time()

    tempo_execucao = fim - inicio

    print(f"Tempo de execução: {tempo_execucao:.2f} segundos")

if __name__ == '__main__':
    main()