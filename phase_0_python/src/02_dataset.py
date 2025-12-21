# 'Write a class Dataset with __init__, __repr__, __len__, __getitem__ that wraps a pandas DataFrame'.



import pandas as pd
class Dataset:
    def __init__(self, df):
        self.df = df

    def __len__(self):
        return self.df.shape[0]

    def __getitem__(self, idx):
        return self.df.iloc[idx]

    def __repr__(self):
        rows, cols = self.df.shape
        return f"Dataset(rows={rows}, cols={cols})"
    
df = pd.read_csv('2.csv')


dataset = Dataset(df)
print(dataset.df.head())
print(len(dataset))
print(dataset[2])
print(dataset)