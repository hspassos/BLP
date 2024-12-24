import scipy.io
import numpy as np
import pandas as pd

file_path = "/home/hspassos/mestrado/industrial/demand_data.mat"

# Carregar o arquivo .mat
mat_data = scipy.io.loadmat(file_path)
print(mat_data)
print(mat_data.keys())

prodsMarket = pd.DataFrame(mat_data['prodsMarket'])
prodsMarket.columns = ['prodsMarket']

share = pd.DataFrame(mat_data['share'])
share.columns = ['share']

f = pd.DataFrame(mat_data['f'])
f.columns = ['firm']

ch = pd.DataFrame(mat_data['ch'])
ch.columns = ['char1', 'char2', 'char3', 'char4']

pr = pd.DataFrame(mat_data['pr'])
pr.columns = ['price']

costShifters = pd.DataFrame(mat_data['costShifters'])
costShifters.columns = ['costsh1', 'costsh2']

data = share.join([f, ch, pr, costShifters])

display(data)
display(prodsMarket)

print(len(data))






















