from sklearn.preprocessing import normalize
import numpy as np
import torch

def weighted_average(df, context_columns, value_column):
    keys = df[context_columns].values.astype(float)
    w = np.matmul(keys,keys.T)
    w_norm = normalize(w, axis=1, norm='l1')
    y_hat = w_norm @ df[value_column]
    return y_hat


def get_sinusoidal_encoding(num_patches, embedding_dim):
    assert embedding_dim % 2 == 0, "Embedding dimension must be even."
    position = torch.arange(num_patches).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, embedding_dim, 2) * -(np.log(10000.0) / embedding_dim))
    positional_embedding = torch.zeros((num_patches, embedding_dim))
    positional_embedding[:, 0::2] = torch.sin(position * div_term)
    positional_embedding[:, 1::2] = torch.cos(position * div_term)
    return positional_embedding