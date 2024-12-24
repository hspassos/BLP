import scipy.io
import numpy as np
import pandas as pd

file_path = "/home/hspassos/mestrado/industrial/demand_data.mat"

# Carregar o arquivo .mat
mat_data = scipy.io.loadmat(file_path)

# Excluir as chaves internas do MATLAB (não queremos "__header__", "__version__", "__globals__")
keys_to_exclude = ['__header__', '__version__', '__globals__']
filtered_data = {key: mat_data[key] for key in mat_data if key not in keys_to_exclude}

# Criar uma lista para armazenar os DataFrames de cada variável
dataframes = []

# Iterar sobre as variáveis, ignorando as chaves especiais (como '__header__', '__version__', etc.)
for key in filtered_data:
    if key.startswith('__'):
        continue  # Ignorar chaves especiais

    # Acessar os dados de cada variável
    data = filtered_data[key]

    # Verificar o tipo de dados e tentar converter para DataFrame
    if isinstance(data, list) or isinstance(data, np.ndarray):
        # Converter para DataFrame, se for uma lista ou array NumPy
        df = pd.DataFrame(data)
        dataframes.append(df)
    else:
        print(f"Não foi possível converter a variável '{key}' para um DataFrame")

# Concatenar todos os DataFrames em um único DataFrame (se desejar)
final_dataframe = pd.concat(dataframes, axis=1)

# Exibir o DataFrame final
print(final_dataframe)

