import pandas as pd
from sklearn.linear_model import LinearRegression

mtcars_df = pd.read_csv('mtcars.csv')

X = mtcars_df.drop(columns=['mpg', 'model', 'carb'])
y = mtcars_df['mpg']

print(mtcars_df.columns) 

model = LinearRegression()
model.fit(X, y)

def predict(dict_values, model=model):
    input = pd.DataFrame([dict_values], columns=X.columns.tolist())
    y_pred = model.predict(input)

    return y_pred[0]