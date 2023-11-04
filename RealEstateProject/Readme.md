# Description
In This project I used R programming lanuage and Microsoft PowerBI tool to analyze and visualize a sample RealEstate data from selected states in the USA, the dataset was downloaded from kaggle here: https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset.
</br >This project demonstrates three components of the data analytics:
</br >-Data Cleaning.
</br >-Data Analysis.
</br >-Data Visualization.

## Data Cleaning.
In this process I used an R script to get rid of all the rows in the dataset that contained NA values.
![Code](https://github.com/GoonerMH99/DataAnalysisProjs/assets/101012808/267ea44a-a2a6-4471-8eb8-7b5f76e90e30)
For the purpose of getting realistic results i had to generate random dates in the prev_sold_date column using an Excel function.
![image](https://github.com/GoonerMH99/DataAnalysisProjs/assets/101012808/17e4215b-90ef-405c-991f-650b6c681a54)


## Data Analysis
Using R programming languages, i was able to get some useful insights from analyzing this dataset.
-Getting the Pearson Correlation Coeffecient between the house size the and the house price in each state.
![Corr](https://github.com/GoonerMH99/DataAnalysisProjs/assets/101012808/47dbb29d-38ba-4764-a618-393015d65cbc)
-Getting the average selling price for each state.
![GroupBy](https://github.com/GoonerMH99/DataAnalysisProjs/assets/101012808/46acbd92-5044-4897-86e3-692cb840fea0)
-Modelling a simple linear regression model that would predict the house prices acording to the house sizes.
![model](https://github.com/GoonerMH99/DataAnalysisProjs/assets/101012808/b7a13051-eff9-4957-a761-ff8b1b7969d8)


## Data Visualization
I used Microsoft PowerBI tool to visualize the insights that we got from the dataset and this is how the PowerBI looked like.
![Original Report](https://github.com/GoonerMH99/DataAnalysisProjs/assets/101012808/dede2125-74dd-43ed-9113-3dfff17e1db7)
The report consisted of a map showing the states and colouring them according to their average selling prices, a scatter plot that showed the average price and average house size for each city and a bar chart that showed the average price for each city, along with a time slider and a state dropdown that would help with filtering the results that we want to see.
</br >This is how the report looked like when using the time slider to select a time frame of 20 years starting from 1/1/2000 to 1/1/2020.
![Time Slider](https://github.com/GoonerMH99/DataAnalysisProjs/assets/101012808/db94f18d-3314-4e57-aad7-a8c9e0a51042)
</br >This is how the report looked like when selecting to see only the results of the New York state.
![Time and State Slider](https://github.com/GoonerMH99/DataAnalysisProjs/assets/101012808/326fcc04-862e-4438-a194-9276f4fa4812)
