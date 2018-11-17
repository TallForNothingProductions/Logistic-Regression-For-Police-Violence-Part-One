library(descr)
#Read Data 
result <- read.csv(file = file.choose())
#Refactor Data
result$Incident.of.Violence <- as.integer(result$Incident.of.Violence)
result$Incident.of.Violence <- result$Incident.of.Violence - 1

#Cross Tab 
logistic_regression <- glm(Incident.of.Violence ~ Day.of.Week + Time.of.Day + Nature.of.Incident, data = result, family = binomial())
summary(logistic_regression)