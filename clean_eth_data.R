rm(list=ls())
library(lubridate)
library(dplyr)
library(tidyverse)


data <- read.csv("eth.csv", skip = 1, header = T)
data <- data %>% select(Unix, Close)
colnames(data) <- c("Date","Close")

data <- data %>% 
  filter(nchar(as.character(Date)) != 10) %>% 
  mutate(Date = as_datetime(Date / 1000)) %>%
  filter(year(Date) <= 2025)

data <- data %>% map_df(rev)
write.csv(data, "eth_clean.csv", row.names = F)
