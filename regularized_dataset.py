from scipy.interpolate import interp1d
import numpy as np
import pandas as pd

def regularize_dataset(filepath, out_file, interp_kind='linear'):
    df = pd.read_csv(filepath)
    
    columns = df.columns

    x = df[columns[0]].values
    y = df[columns[1]].values
    
    x_interp_min = x.min() - (x.min() % 0.5) + 0.5
    x_interp_max = x.max() - (x.max() % 0.5)
    
    f = interp1d(x, y, kind=interp_kind)
    
    x_interp = np.arange(x_interp_min, x_interp_max, 0.5)
    y_interp = f(x_interp)
    
    interp_column = {
        columns[0]: x_interp,
        columns[1]: y_interp
    }
    
    interpolate = pd.DataFrame(interp_column)
    interpolate.to_csv(out_file)

if __name__ == '__main__':
    regularize_dataset(r'in\dataset.csv',
                       r'out\dataset.csv')