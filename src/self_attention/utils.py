from sklearn.preprocessing import normalize
import numpy as np

def weighted_average(df, context_columns, value_column):
    keys = df[context_columns].values.astype(float)
    w = np.matmul(keys,keys.T)
    w_norm = normalize(w, axis=1, norm='l1')
    y_hat = w_norm @ df[value_column]
    return y_hat