import numpy as np
import pandas as pd
from sklearn.model_selection import  train_test_split

def LoadData(filename, yclasscol, cols, delim=",", normalize=True):
    y_class = [cols[yclasscol]]
    print ("y_class col=", y_class)
    features = cols[0:yclasscol]
    features += cols[yclasscol+1:]
    print ("features col=", features)
    
    df = pd.read_csv(filename, cols, delimiter=delim, delim_whitespace=False)
    missingno.matrix(df, figsize = (30,10))
    df.fillna(value=0,inplace=True)
    x_df = df[features]
    y_df = df[y_class]
    x_data = np.array(pd.DataFrame(x_df, columns = features))
    y_data = np.array(pd.DataFrame(y_df, columns = y_class))
      

    x_data_train, x_data_test, y_data_train, y_data_test = train_test_split(x_data, y_data, test_size=0.2, shuffle=False)
    print (x_data_train.shape)
    return x_data_train, y_data_train, x_data_test, y_data_test
if (__name__ == "__main__"):
    print ("Executing", __name__)
else:
    print ("Importing", __name__)

   
