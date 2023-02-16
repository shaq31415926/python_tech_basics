from datetime import datetime
import pandas as pd
import sqlite3

user_name = input("What is your name?:")
user_age = input("What is your age?:")

# create a timestamp and store in variable run_id
run_id = datetime.now().strftime("%Y%m%d%H%M%S")

user_data = pd.DataFrame([{"user_name": user_name,
             "user_age": user_age,
             "timestamp": run_id
             }])

# create a sqlite connection
db_connection = sqlite3.connect("../data/test_database.db")
cd
# write the data frame to your database
user_data.to_sql(
    name="test_table",
    if_exists="append",
    con=db_connection,
    index=False
)

print("The data is stored to table test_table in your database")
db_connection.close() # closes the sqlite connection
