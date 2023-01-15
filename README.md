# fetch_rewards_data_engineering
I have made the following assumptions about the data:
*Records that do have incorrect data (for example a field is missing) are ignored
*App version is of format X.Y.Z (for example 2.15.3). However, the field in the table is of type Integer and hence only first part, that is X, is considered (2 in the example given)
*create_date is retrieved from datetime as the date the code is executed

For masking, I have used SHA-256 encoding which will help data analysts to hide the data and at the same time able to detect duplicates
