# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:01:15 2024

@author: srsouza
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

data = pd.read_parquet("data/parsed_data_public.parquet")

# Explore Age
print("Age")
print(data['d_age'].describe())

# Histogram
data.d_age.plot.hist(bins=25, alpha=0.5)

# Another histogram
#This histogram is poorer, but uses Spyder's resources. After the age variable
#has been generated, just click the mouse context button in the variable
#explorer and click on histogram.
age = data.d_age.tolist()

# Best histogram with Seaborn
sns.histplot(data.d_age, kde=True, bins=25)
plt.xlabel('Age')
plt.axvline(data.d_age.mean(), color='k', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(data.d_age.mean()*1.1, max_ylim*0.9,
         'Mean: {:.2f}'.format(data.d_age.mean()))
plt.show()
 
# Religion seriosity
# List of demograph colums
demograph = [v for v in list(data.columns) if v.startswith("d_")]

# d_religion_seriosity.value_counts()
data.d_religion_seriosity.value_counts()


