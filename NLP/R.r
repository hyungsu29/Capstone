
library(arules)
df<-read.csv("R.csv")

rioter.list<-split(df$keyword, df$date)
rioter.transaction<-as(rioter.list, "transactions")
rioter.transaction


rioter.rules = apriori(rioter.transaction, parameter = list(support = 0.5, confidence = 0.7))
summary(rioter.rules)

write.table(inspect(rioter.rules),'aaa.txt')
