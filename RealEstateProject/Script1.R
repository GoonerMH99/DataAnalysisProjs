#Removing all the rows that contains NA values

df<-na.omit(Dataset)

write.csv(df, "E:\\DataAnalysis\\RealEsateProject\\dataset_noNA", row.names=FALSE)

#--------------------------------------#
#Getting the Pearson correlation coefficient for each state

states<-unique(df$state)
i<-1
while (i < 8)
{
  state_df<-subset(df, state == states[i])
  r<-cor(state_df$house_size, state_df$price)
  cat("The Pearson correlation coefficient between the houses sizes and price in
      the state of", states[i], "is:", r, "\n")
  i<-i+1
}

#--------------------------------------#
#Getting the maximum, minimum and average selling prices in each state

library(dplyr)

#Group by "State"
grp_tbl <- df %>% group_by(state)
grp_tbl

#Usin the max(), min() and mean() aggreagate functions
agg_tbl <- grp_tbl %>% summarise(max(price),mean(price),min(price))
agg_tbl

#--------------------------------------#
#A simple Linear Regression model where we can predict the house price aacording to the data of the houses sizes

model <- lm(df$price ~ df$house_size, data=df)
summary(model)