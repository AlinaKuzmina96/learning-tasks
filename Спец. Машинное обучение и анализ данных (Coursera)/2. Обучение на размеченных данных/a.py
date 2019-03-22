import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('weights_heights.csv', index_col='Index')
#print(data[:10])
#data.plot(y='Height', kind='hist', 
           #color='red',  title='Height (inch.) distribution')
#plt.show()
#data.plot(y='Weight', kind='hist', 
           #color='green',  title='Weight (inch.) distribution')
#plt.show()

def make_bmi(height_inch, weight_pound):   #индекс массы тела
    METER_TO_INCH, KILO_TO_POUND = 39.37, 2.20462
    return (weight_pound / KILO_TO_POUND) / \
           (height_inch / METER_TO_INCH) ** 2

data['BMI'] = data.apply(lambda row: make_bmi(row['Height'], 
                                              row['Weight']), axis=1)
#sns.pairplot(data)
#plt.show()

def weight_category(weight):
    if weight < 120:
    	return 1
    elif weight >= 150:
    	return 3
    else:
    	return 2

data['weight_cat'] = data['Weight'].apply(weight_category)
#sns.boxplot(x="weight_cat", y="Height", data=data)
#plt.show()
data.plot(y='Height', x='Weight', kind='scatter')
plt.show()