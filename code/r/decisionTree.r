#Property of VR3 @ vr3.io
#Patrick Moss
#Oscar Chavez

#R code Data B Cup
#Load 
install.packages("randomForest")
install.packages("ggplot2")
install.packages("ggpairs")
library(ggplot2)
library(randomForest)
library(rpart)
library(ggpairs)


#Set Working DR
setwd("C:/Users/J_Pat/Desktop/brewingdatacup-comercial-master/brewingdatacup-comercial-master/data/")
#Load Dataset
DataComercial <- read.csv("AgenciasDist.csv", sep=",")
#See what data set we have
summary(DataComercial)

#Set Proper Dates
DataComercialDates <- as.Date(DataComercial$Mes, origin="1900-01-01")
DataComercial$Mes <-DataComercialDates

#Load Plots to understand what we have
hist(DataComercial$Hectolitros)
hist(DataComercial$Subagencia)
hist(DataComercial$SKU)
hist(DataComercial$Mes)

#AEsthetic Check
ggplot(DataComercial, aes(x = Hectolitros)) +geom_histogram()
ggplot(DataComercial,aes(y = Mes, x = Subagencia)) +geom_point()


ggplot(DataComercial, aes(DataComercial$Mes, fill = DataComercial$Hectolitros)) + geom_bar(position = "dodge")

#Split Data
train_data <- DataComercial[DataComercial$Mes >= "1970-01-01" & DataComercial$Mes <= "2015-01-01",]
test_data <- DataComercial[DataComercial$Mes >= "2015-01-02" & DataComercial$Mes <= "2018-01-01",]
min_test_data <- DataComercial[DataComercial$Mes >= "2017-01-02" & DataComercial$Mes <= "2018-02-02",]

#WriteDataset for Azure
write.csv(min_test_data, "DC_Train_Data.csv")

#Matrix
DC_matrix <- data.matrix(DataComercial)
DC_heatmap <- heatmap(DC_matrix, Rowv=NA, Colv=NA, col = heat.colors(256), scale="column", margins=c(5,10))

regressor = randomForest(x = DataComercial[1], y = DataComercial$Hectolitros,nTree = 10)
y_predict = predict(regressor, data.frame(Level = 6.5))

#Model
fit <- rpart(DC_matrix~. DataComercial)
linearMod <- lm(DC_matrix ~., data=DataComercial)  # build linear regression model on full data
print(linearMod)
summary(linearMod)

#Test Model
set.seed(123)  
trainingRowIndex <- sample(1:nrow(DataComercial), 0.8*nrow(DataComercial))  #80/20
trainingData <- DataComercial[trainingRowIndex, ] 
testData  <- DataComercial[-trainingRowIndex, ]
