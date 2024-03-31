import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import statsmodels.formula.api as smf
from sklearn.metrics import mean_absolute_error
from sqlalchemy import create_engine

# Create a SQL Alchemy engine for the MySQL database
engine = create_engine('mysql+mysqlconnector://staff:admin@localhost:3306/dynamicstaffing')

# Assuming you have a table named 'your_table_name_here' in your database
# Replace 'your_table_name_here' with the actual table name you wish to load
table_name = 'restaurantdata'
query = f"SELECT * FROM {table_name}"
dat = pd.read_sql_query(query, engine)

# If your table includes a 'Date' column, and you want to parse it as datetime
dat['Date'] = pd.to_datetime(dat['Date'])

trainData, testData = train_test_split(dat, test_size=0.3, random_state=123)

# Model 1
formula = 'Customers ~ ' + ' + '.join([col for col in trainData.columns if col != 'Customers' and col != 'Date'])
lr1 = smf.ols(formula=formula, data=trainData).fit()

# Making predictions & plotting for model 1
predictions1 = lr1.predict(testData)
testData['Predictions1'] = predictions1

# Plot for Model 1
sns.scatterplot(x='Profits', y='Customers', data=testData)
sns.lineplot(x='Profits', y='Predictions1', data=testData, color='red')
plt.savefig('model1_plot.png')
plt.close()

# Calculate MAE for Model 1 and save coefficients and MAE to a text file
mae1 = mean_absolute_error(testData['Customers'], predictions1)
with open('model1_summary.txt', 'w') as file:
    file.write(f'Coefficients:\n{lr1.params}\n\n')
    file.write(f'Mean Absolute Error (MAE): {mae1}\n')

# Model 2
columns = ["Employees", "Satisfaction", "Profits", "Customers"]
trainData2 = trainData[columns]
testData2 = testData[columns]
formula2 = 'Profits ~ Employees + Satisfaction + Customers'
lr2 = smf.ols(formula=formula2, data=trainData2).fit()

# Making predictions for model 2
predictions2 = lr2.predict(testData2)
testData2['Predictions2'] = predictions2

# Plotting results for Model 2
fig, ax = plt.subplots()
sns.scatterplot(x='Employees', y='Profits', data=testData2, ax=ax)
sns.lineplot(x='Employees', y='Predictions2', data=testData2, color='red', ax=ax)
sns.regplot(x='Employees', y='Profits', data=testData2, scatter=False, color='blue', ax=ax)
plt.savefig('model2_plot.png')
plt.close()

# Calculate MAE for Model 2 and save coefficients and MAE to a text file
mae2 = mean_absolute_error(testData2['Profits'], predictions2)
with open('model2_summary.txt', 'w') as file:
    file.write(f'Coefficients:\n{lr2.params}\n\n')
    file.write(f'Mean Absolute Error (MAE): {mae2}\n')
