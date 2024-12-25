import scipy.io
import numpy as np
import pandas as pd

file_path = "/home/hspassos/mestrado/industrial/demand_data.mat"

# Carregar o arquivo .mat
mat_data = scipy.io.loadmat(file_path)
print(mat_data)
print(mat_data.keys())

prodsMarket = pd.DataFrame({'prodsMarket': mat_data['prodsMarket'].flatten()})

data = pd.DataFrame({
    'share': mat_data['share'].flatten(),
    'firm': mat_data['f'].flatten(),
    'price': mat_data['pr'].flatten(),
    'char1': mat_data['ch'][:, 0],
    'char2': mat_data['ch'][:, 1],
    'char3': mat_data['ch'][:, 2],
    'char4': mat_data['ch'][:, 3],
    'costsh1': mat_data['costShifters'][:, 0],
    'costsh2': mat_data['costShifters'][:, 1],
})


display(data)
display(prodsMarket)

print(len(data))






















