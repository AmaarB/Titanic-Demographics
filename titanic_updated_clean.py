###   ###   ----------------------------------------------------------------
# Import library statements
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
###   ###   ----------------------------------------------------------------
# Loading the data feed using seaborn Technique
df =  sns.load_dataset('titanic')

#....#DRAWING OUT THE NULL VALUES FROM A HEAT MAP GRAPH TO GET OVERVIEW OF ACTUAL DATASET BEFORE CLEANING AND USE..
#Drawing a heatmap to check null values for cleaning the data set.
missing_values= sns.heatmap(df.isnull(), cbar=False)

#print(missing_values)

#..............USING DEFINED FUNCTIONS TO CLEAN OUT DATASET...........................
#Function replaces the blank values present in the embarked column with S
def fill_embarked(df, colname):
    
    return df[colname].fillna('S')
    
df['embarked'] = fill_embarked(df, 'embarked')

#print(df['embarked'])

#using a drop function to remove the column because it has more number of blank columns and inappropriate for use
df.drop('deck',axis=1,inplace=True)

# DEFINING THESE VARIABLES TO GET MEAN AND STD OF AGE COLUMN FOR FURTHER USE.
mean = df['age'].mean()
sd = df['age'].std()
print(mean,sd)

#Function replaces missing values in age with the MEAN and std bby choosing random number
#  between the range highest and lowest range of mean and sd
def age(df, colname):
    mean = df['age'].mean()
    sd = df['age'].std()
    def get_empty(x):
                         #Isnan function to check whether the value is number or not.   
                         # if it is not a number its generates random number using random.randomint function within the range.    
        if np.isnan(x):
            return np.random.randint(mean-sd, mean+sd, ())
        return x
    return df[colname].apply(get_empty).astype(int)
df['age'] = age(df, 'age')
#print('age in dataset is: \n',+df['age'])

#Function replaces the missing values from embark_town column as Southampton.
def fill_embark_town(df, colname):
    return df[colname].fillna('Southampton')
df['embark_town'] = fill_embark_town(df, 'embark_town')
                        
# using fillna() function above to fill desired values in place of missing or NA values.












