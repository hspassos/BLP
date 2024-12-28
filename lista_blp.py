import scipy.io
import numpy as np
import pandas as pd
import pyblp

# Carregar o arquivo .mat
mat_data = scipy.io.loadmat("/home/hspassos/mestrado/industrial/demand_data.mat")

prodsMarket = {'market': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
prodsMarket = pd.DataFrame(prodsMarket)
prodsMarket['prodsMarket'] = mat_data['prodsMarket'].flatten()

# Criar tabela com os dados por produto
data = pd.DataFrame({
    'market': np.repeat(np.arange(len(prodsMarket)), prodsMarket['prodsMarket']),
    'firm': mat_data['f'].flatten(),
    'share': mat_data['share'].flatten(),
    'price': mat_data['pr'].flatten(),
    'char1': mat_data['ch'][:, 0],
    'char2': mat_data['ch'][:, 1],
    'char3': mat_data['ch'][:, 2],
    'char4': mat_data['ch'][:, 3],
    'costsh1': mat_data['costShifters'][:, 0],
    'costsh2': mat_data['costShifters'][:, 1],
})


# Tabela com os dados para cada mercado
prodsMarket['activefirms'] = data.groupby('market')['firm'].nunique()

prodsMarket['firm_1'] = data[data['firm'] == 1].groupby('market')['firm'].count()
prodsMarket['share_firm_1'] = data[data['firm'] == 1].groupby('market')['share'].sum()

prodsMarket['firm_2'] = data[data['firm'] == 2].groupby('market')['firm'].count()
prodsMarket['share_firm_2'] = data[data['firm'] == 2].groupby('market')['share'].sum()

prodsMarket['firm_3'] = data[data['firm'] == 3].groupby('market')['firm'].count()
prodsMarket['share_firm_3'] = data[data['firm'] == 3].groupby('market')['share'].sum()

prodsMarket['firm_4'] = data[data['firm'] == 4].groupby('market')['firm'].count()
prodsMarket['share_firm_4'] = data[data['firm'] == 4].groupby('market')['share'].sum()

prodsMarket['firm_5'] = data[data['firm'] == 5].groupby('market')['firm'].count()
prodsMarket['share_firm_5'] = data[data['firm'] == 5].groupby('market')['share'].sum()

prodsMarket['firm_6'] = data[data['firm'] == 6].groupby('market')['firm'].count()
prodsMarket['share_firm_6'] = data[data['firm'] == 6].groupby('market')['share'].sum()

prodsMarket['firm_7'] = data[data['firm'] == 7].groupby('market')['firm'].count()
prodsMarket['share_firm_7'] = data[data['firm'] == 7].groupby('market')['share'].sum()

prodsMarket['firm_8'] = data[data['firm'] == 8].groupby('market')['firm'].count()
prodsMarket['share_firm_8'] = data[data['firm'] == 8].groupby('market')['share'].sum()

prodsMarket['firm_9'] = data[data['firm'] == 9].groupby('market')['firm'].count()
prodsMarket['share_firm_9'] = data[data['firm'] == 9].groupby('market')['share'].sum()

prodsMarket['firm_10'] = data[data['firm'] == 10].groupby('market')['firm'].count()
prodsMarket['share_firm_10'] = data[data['firm'] == 10].groupby('market')['share'].sum()

prodsMarket['firm_11'] = data[data['firm'] == 11].groupby('market')['firm'].count()
prodsMarket['share_firm_11'] = data[data['firm'] == 11].groupby('market')['share'].sum()



display(prodsMarket)

print(data[data['market'] == 3]['share'].sum())

market_1 = pd.DataFrame(data[data['market'] == 0])

print(market_1[market_1['firm'] == 1]['share'].sum())

display(market_1)
















