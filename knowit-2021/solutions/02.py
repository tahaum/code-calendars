import pandas as pd
from haversine import haversine

def main():
    path = '../data/02-cities.csv'
    df = pd.read_csv(path)
    row_np = ['North Pole', 0.0, 90.0]
    df.loc[:, 'lon'] = (df.location.str.split(' ').str[0].str.split('(').str[1]).astype(float)
    df.loc[:, 'lat'] = (df.location.str.split(' ').str[1].str[:-1]).astype(float)
    dist = 0
    
    for i in range(len(df.index)):
        if i == 0:
            current_coords = [90.0, 0.0]
        
        dist += haversine(df.loc[i-1, ['lat', 'lon']], df.loc[i, ['lat', 'lon']])
    print('Total distance:', round(dist))
        
if __name__ == '__main__':
    main()   