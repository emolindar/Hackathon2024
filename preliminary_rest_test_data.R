setwd("C:/Users/Peter-Emil/OneDrive - aubg.edu/Courses/Freshman Second Semester/Hackathon")

library(caret)
library(ggplot2)


dat = read.csv("preliminary_rest_test_data.csv")
summary(dat)
head(dat)

set.seed(123)
row_nums <- createDataPartition(dat$Date, p = 0.7, list = FALSE )
trainData <- dat[row_nums,]
testData <- dat[-row_nums,]


lr1 <- train(Customers~., data = trainData, method = "lm")
lr1$finalModel
lr1


predictions <- predict(lr1, newdata = testData)


ggplot(testData, aes(x = testData$Profits, y=testData$Customers)) +
  geom_point() +
  geom_line(data = testData, aes(x = testData$Profits,y= predictions ), color = "red")
