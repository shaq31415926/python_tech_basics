import os
import pandas as pd
import sqlite3
from datetime import datetime

os.system('clear')

print("This is a sample script that asks the user for inputs and stores the user input in a database")

user_name = input("What is your name?:")
age = input("What is your age?:")

# create a timestamp
run_id = datetime.now().strftime("%Y%m%d%H%M%S")

# store the user input data as a dictionary and then convert it to a Data Frame
user_data = pd.DataFrame([{"user_name": user_name,
                          "user_age": age,
                           "timestamp": run_id
                           }])

# create a connection to the sqlite database. This will work even if this is your first time creating it.
db_connection = sqlite3.connect("../data/test_database.db")

# write the data frame to sql. If the table exists, the data will be added to the existing table.
user_data.to_sql(
            name="test_table", # this is the table name
            if_exists="append",
            con=db_connection,
            index=False,
        )

db_connection.close() # close the sqlite connection

print("Thank you for the information. Check if this has been stored correctly =)")

