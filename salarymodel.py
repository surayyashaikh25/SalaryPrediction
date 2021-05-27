import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
dataset=pd.read_csv("SalaryData.csv")
x=ds['YearsExperience'].values.reshape(30,1)
y=ds['Salary']
model=LinearRegression()
model.fit(x,y)
joblib.dump(model,"salary.h5")
print("\n Salary prediction model successfully stored in salary.h5 !!!")
