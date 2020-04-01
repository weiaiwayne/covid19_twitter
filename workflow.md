- Raw data: https://zenodo.org/record/3723940 (for data accumulated before 3/22) and https://github.com/thepanacealab/covid19_twitter/tree/master/dailies (for data on and after 3/22)
- Use _dissect_df.R_ (in R) to dissect raw dataset into chunks by months, weeks, or days (depending on the size of data) and standardize tweet_id. Make sure tweet ids are correct.
- Download the SMMT repo:  https://github.com/weiaiwayne/SMMT and move the dissected datasets under data_acquisition 
- (optional) adjust sleep time in _get_metadata.py_
```sh
python get_metadata.py -i INPUTFILE -o OUTPUTFILE
```
