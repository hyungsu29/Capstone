library(arulesSequences)
df <- read_baskets("R2.csv", sep = ",", info = c("sequenceID", "eventID", "size"))
as(df, "data.frame")
seq_rule_1 <- cspade(df, parameter = list(), control= list(verbose = TRUE))
summary(seq_rule_1)

write.table(as(seq_rule_1, "data.frame"),'result.txt')

