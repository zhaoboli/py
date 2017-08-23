import pandas as pd
import numpy as np

# mock raw data for data frame

raw_data = {
    'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks',
                 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons',
                 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
    'company': ['1st', '1st', '2nd', '2nd', '1st', '1st',
                '2nd', '2nd', '1st', '1st', '2nd', '2nd'],
    'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze',
             'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani',
             'Ali'],
    'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])

grouped = df.groupby(['company', 'regiment'])

#newgrouped = grouped['preTestScore'].agg({'C': np.sum})

#print list(newgrouped)

#print grouped

#use list to show grouped object
#print list(grouped)

#statistic data of grouped object
#print grouped.describe()

#show the actual type of grouped object
#print type(grouped)

# select
df[df.categor == 'category_a']

# merge two df
pd.merge(df, df2)

newdf = pd.DataFrame({'count': grouped.size()}).reset_index()
newdf.to_csv('out.csv', sep='\t', encoding='utf-8', index=False)
print newdf