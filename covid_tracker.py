import pandas as pd
import matplotlib.pyplot as plt

# Sample COVID-19 data
data = {
    'Country': ['USA','India','Brazil','UK','Germany'],
    'TotalCases': [105000000,45000000,37000000,24000000,38000000],
    'TotalDeaths': [1100000,530000,698000,190000,174000],
    'TotalRecovered': [102000000,44000000,36000000,23000000,37000000]
}

df = pd.DataFrame(data)

# Print data
print("✅ COVID-19 Data Loaded Successfully!")
print(df)

# Bar chart: Total Cases by Country
plt.bar(df['Country'], df['TotalCases'], color='skyblue')
plt.title('Total COVID-19 Cases by Country')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.show()

# Pie chart for USA
usa_data = df[df['Country']=='USA'].iloc[0]
plt.pie(
    [usa_data['TotalCases'], usa_data['TotalDeaths'], usa_data['TotalRecovered']],
    labels=['Cases','Deaths','Recovered'],
    autopct='%1.1f%%',
    colors=['skyblue','red','green']
)
plt.title('USA COVID-19 Distribution')
plt.show()
