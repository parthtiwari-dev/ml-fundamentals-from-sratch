# Write a generator batch_generator(X, y, batch_size) that yields mini-batches

import pandas as pd
import numpy as np
import random

def batch_generator (X, y, batch_size):
    N = len(X)
    idx = np.arange(N)
    np.random.shuffle(idx)    
    for s_i in range(0, N, batch_size):
        e_i = s_i + batch_size
        batch_idx = idx[s_i:e_i]
        X_batch = X.iloc[batch_idx]
        y_batch = y.iloc[batch_idx]
        yield X_batch, y_batch

X = pd.DataFrame({
    "a": [10, 20, 30, 40, 50, 60, 70]
})

y = pd.Series([0, 1, 0, 1, 0, 1, 0])

batch_size = 3

gen = batch_generator(X, y, batch_size)


total = 0

for i, (Xb, yb) in enumerate(gen):
    print(f"\nBatch {i}")
    print("X_batch:")
    print(Xb)
    print("y_batch:")
    print(yb)

    total += len(Xb)

print("\nTotal samples seen:", total)
