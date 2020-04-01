library(readr)
full_dataset_clean <- read_delim("full_dataset-clean.tsv", 
                                 "\t", escape_double = FALSE, col_types = cols(time = col_character(), 
                                                                               tweet_id = col_character()), trim_ws = TRUE)


full_dataset_clean$tweet_id <- as.numeric(full_dataset_clean$tweet_id)
full_dataset_clean$date <- as.Date(full_dataset_clean$date)

full_dataset_clean$tweet_id[4]
full_dataset_clean$date[4]

jan <- full_dataset_clean[full_dataset_clean$date <= "2020-01-31",c("tweet_id")]
feb <- full_dataset_clean[full_dataset_clean$date >= "2020-02-1" & full_dataset_clean$date <= "2020-02-29" ,c("tweet_id")]
marchw1 <- full_dataset_clean[full_dataset_clean$date >= "2020-03-1" & full_dataset_clean$date <=  "2020-03-7" ,c("tweet_id")]

marchw2pt1 <- full_dataset_clean[full_dataset_clean$date >= "2020-03-8" & full_dataset_clean$date <= "2020-03-10" ,c("tweet_id")]
marchw2pt2 <- full_dataset_clean[full_dataset_clean$date >= "2020-03-11" & full_dataset_clean$date <= "2020-03-13" ,c("tweet_id")]

marchw2 <- full_dataset_clean[full_dataset_clean$date >= "2020-03-8" & full_dataset_clean$date <= "2020-03-14" ,c("tweet_id")]
marchw3 <- full_dataset_clean[full_dataset_clean$date >= "2020-03-15" & full_dataset_clean$date <= "2020-03-21" ,c("tweet_id")]
marchw4 <- full_dataset_clean[full_dataset_clean$date >= "2020-03-22" & full_dataset_clean$date <= "2020-03-28" ,c("tweet_id")]

write_csv(jan,"jan_clean.csv")
write_csv(feb,"feb_clean.csv")
write_csv(marchw1,"marchw1_clean.csv")

write_csv(marchw2pt1,"marchw2pt1_clean.csv")
write_csv(marchw2pt2,"marchw2pt2_clean.csv")


write_csv(marchw3,"marchw3_clean.csv")
write_csv(marchw4,"marchw4_clean.csv")

