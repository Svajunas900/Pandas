"""2885. Rename Columns

Write a solution to rename the columns as follows:

id to student_id
first to first_name
last to last_name
age to age_in_years
The result format is in the following example.
"""

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={"id":"student_id","first": "first_name", "last": "last_name", "age": "age_in_years"}, inplace=True)
    return students