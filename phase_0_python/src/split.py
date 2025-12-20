import pandas as pd 
import random
random.seed(42)
def train_test_split(df):
    N = df.shape[0]
    idx = random.sample(range(0, N), N)
    split =  int(0.8 * N)
    train_indices = idx[:split]
    test_indices = idx[split:]
    df_train = df.iloc[train_indices]
    df_test = df.iloc[test_indices]

    return df_train,df_test

df = pd.read_csv('2.csv')

df_train, df_test = train_test_split(df)

print((df_train.shape[0]) + (df_test.shape[0]) == (df.shape[0]), set(df_train.index).isdisjoint(df_test.index), df_test,df_train)

