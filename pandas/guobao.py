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

#new example
l = [['jack', 'male', '2002-12-25 00:00:00-06:39', 'abded_010_20170820.txt',10,'car'],
 ['jack', 'male', '2002-12-25 00:00:00-06:39', 'abded_010_20170821.txt',18, 'car'],
 ['rose', 'female', '2002-12-25 00:00:00-06:39', 'abded_010_20170821.txt',9, 'shopping']]

 df = pd.DataFrame(l, columns = ['name', 'gender', 'birthdate', 'cert', 'score', 'hobit'])

def try_derive_time(value, start, end):
    try:
        startIndex = value.rindex(start) + len(start)
        endIndex = value.rindex(end)
        return value[startIndex : endIndex]
    except ValueError:
        return '19700101'

df.assign(cert_date = lambda x :(str(x['cert'])[str(x['cert']).rindex('_') : str(x['cert']).rindex('.')]))

Group By:
groupby output has the grouping columns as indicies, not columns,
po_grouped_df = poagg_df.groupby(['EID','PCODE'], as_index=False)
pd.merge(acc_df, pol_df, on=['EID','PCODE'], how='inner',suffixes=('_Acc','_Po'))
