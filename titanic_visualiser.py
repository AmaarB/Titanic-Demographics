from titanic_updated_clean import *
# setting up color codes as true in order to make the data look attractive using set func
sns.set_color_codes('deep')

#created data frames to store both numeric and categorical data columns 
df_numerical = df[['age','sibsp','parch','fare']]
df_catogerical = df[['survived','pclass','sex','embarked','who']]

#plotting numerical columns Data
for i in df_numerical.columns:

    plt.hist(df_numerical[i])
    plt.title(i)
    plt.show()

#plotting categorical columns Data
for i in df_catogerical.columns:
 sns.barplot(df_catogerical[i].value_counts().index,df_catogerical[i].value_counts()).set_title(i)
 plt.show()

#shows gender and check how many male and female passengers are there from titanic dataset
sns.catplot(
    'sex',data=df,kind='count'
    )
#using catplot visual plot to show pclass amount
sns.catplot(
    'pclass',data=df,kind='count'
    )
#using catplot visual plot to show the amount of pclass and diffrent sex 
sns.catplot(
    'pclass',data=df,hue='sex',kind='count'
    )
#infer age ranges of passengers from titanic dataset
df['age'].hist(bins=70)

#infering survival number from the titanic dataset
#plotting the graph
sns.countplot('survived', data=df)
plt.title("Titanic Survived")
plt.show()

#using boxpot visual plot to show age
sns.boxplot(
    x='age',data=df,orient='h',palette='pastel'
    )

#using catplot  visual plot to show relation between age and sex and pclass.

sns.catplot(
    x='sex', y='age', data=df, kind='box', hue='pclass'
    )

#using barplot visual plot to show relation between pclass, fare and sex .
sns.barplot(
    x = 'pclass', y = 'fare', hue = 'sex', data = df  #ci =None
    ) 
plt.show()

#using barplot visual plot to show relation between class and fare .
sns.barplot(
    x = 'class', y = 'fare', data = df, ci = None,palette='pastel'
    )
plt.show()

#using Countplot to visulaize class Vs sex 
sns.countplot(
    x = 'class',hue = 'sex',data = df,color="blue"
    )
plt.show()

#using style to set the general style of plot
sns.set(style='whitegrid')
#df = sns.load_dataset('titanic')
#using boxplot visual to show relations btwn survived and who columns
sns.boxplot(
    x='survived', y='who', data=df,hue='sex'
    )
#using violin part to show relation btwn age and who
sns.violinplot(
    x ='age', y ='who', data = df, color = "pink"
    )

#using scatter visual plot to show relation between age and sex .
sns.scatterplot(
    x='age', y='sex', data=df, hue='who', palette='pastel',legend='full'
    )




