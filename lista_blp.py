import scipy.io
import numpy as np
import pandas as pd
import scipy.stats as stats
import pyblp

# Carregar o arquivo .mat
mat_data = scipy.io.loadmat("/home/hspassos/mestrado/industrial/demand_data.mat")

prodsMarket = {'market': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
prodsMarket = pd.DataFrame(prodsMarket)
prodsMarket['prodsMarket'] = mat_data['prodsMarket'].flatten()

# Criar tabela com os dados por produto
data = pd.DataFrame({
    'market_ids': np.repeat(np.arange(len(prodsMarket)), prodsMarket['prodsMarket']),
    'firm_ids': mat_data['f'].flatten(),
    'shares': mat_data['share'].flatten(),
    'prices': mat_data['pr'].flatten(),
    'const': mat_data['ch'][:, 0],
    'char1': mat_data['ch'][:, 1],
    'char2': mat_data['ch'][:, 2],
    'char3': mat_data['ch'][:, 3],
    'costsh1': mat_data['costShifters'][:, 0],
    'costsh2': mat_data['costShifters'][:, 1],
})


# Tabela com os dados para cada mercado
prodsMarket['activefirms'] = data.groupby('market_ids')['firm_ids'].nunique()

prodsMarket['firm_1'] = data[data['firm_ids'] == 1].groupby('market_ids')['firm_ids'].count()
prodsMarket['share_firm_1'] = data[data['firm_ids'] == 1].groupby('market_ids')['shares'].sum()

prodsMarket['firm_2'] = data[data['firm_ids'] == 2].groupby('market_ids')['firm_ids'].count()
prodsMarket['share_firm_2'] = data[data['firm_ids'] == 2].groupby('market_ids')['shares'].sum()

prodsMarket['firm_3'] = data[data['firm_ids'] == 3].groupby('market_ids')['firm_ids'].count()
prodsMarket['share_firm_3'] = data[data['firm_ids'] == 3].groupby('market_ids')['shares'].sum()

prodsMarket['firm_4'] = data[data['firm_ids'] == 4].groupby('market_ids')['firm_ids'].count()
prodsMarket['share_firm_4'] = data[data['firm_ids'] == 4].groupby('market_ids')['shares'].sum()

prodsMarket['firm_5'] = data[data['firm_ids'] == 5].groupby('market_ids')['firm_ids'].count()
prodsMarket['share_firm_5'] = data[data['firm_ids'] == 5].groupby('market_ids')['shares'].sum()

prodsMarket['firm_6'] = data[data['firm_ids'] == 6].groupby('market_ids')['firm_ids'].count()
prodsMarket['share_firm_6'] = data[data['firm_ids'] == 6].groupby('market_ids')['shares'].sum()

prodsMarket['firm_7'] = data[data['firm_ids'] == 7].groupby('market_ids')['firm_ids'].count()
prodsMarket['share_firm_7'] = data[data['firm_ids'] == 7].groupby('market_ids')['shares'].sum()

prodsMarket['firm_8'] = data[data['firm_ids'] == 8].groupby('market_ids')['firm_ids'].count()
prodsMarket['share_firm_8'] = data[data['firm_ids'] == 8].groupby('market_ids')['shares'].sum()

prodsMarket['firm_9'] = data[data['firm_ids'] == 9].groupby('market_ids')['firm_ids'].count()
prodsMarket['share_firm_9'] = data[data['firm_ids'] == 9].groupby('market_ids')['shares'].sum()

prodsMarket['firm_10'] = data[data['firm_ids'] == 10].groupby('market_ids')['firm_ids'].count()
prodsMarket['share_firm_10'] = data[data['firm_ids'] == 10].groupby('market_ids')['shares'].sum()

prodsMarket['firm_11'] = data[data['firm_ids'] == 11].groupby('market_ids')['firm_ids'].count()
prodsMarket['share_firm_11'] = data[data['firm_ids'] == 11].groupby('market_ids')['shares'].sum()



statistics = pd.DataFrame({
    'mean': data.iloc[:, 2:].mean(),
    'median': data.iloc[:, 2:].median(),
    'minimum': data.iloc[:, 2:].min(),
    'maximum': data.iloc[:, 2:].max(),
    'standard deviation': data.iloc[:, 2:].std()
}).T

market_0 = pd.DataFrame(data[data['market_ids'] == 0])
market_1 = pd.DataFrame(data[data['market_ids'] == 1])

formulation = pyblp.Formulation('0 + prices + char1 + char2 + char3')
local_instruments = pyblp.build_differentiation_instruments(
formulation,
data
)
local_instruments

quadratic_instruments = pyblp.build_differentiation_instruments(
formulation,
data,
version='quadratic'
)
quadratic_instruments

for i, column in enumerate(local_instruments.T):
    data[f'demand_instruments{i}'] = column
data

##########################

# Especificar o modelo BLP
x1_formulation = pyblp.Formulation(
    '1 + prices + char1 + char2 + char3',  # Características e preço
)

x2_formulation = pyblp.Formulation(
    '1 + prices + costsh1 + costsh2',  # Custos marginais
)


problem = pyblp.Problem([x1_formulation, x2_formulation], data)

results = problem.solve()

delta = results.delta
print(delta)










