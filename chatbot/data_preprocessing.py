import pandas as pd

def load_data(data):
    data = pd.read_csv('data.csv')
    return data

if __name__ == "__main__":
    data = load_data('data.csv')
    print(data.head())
