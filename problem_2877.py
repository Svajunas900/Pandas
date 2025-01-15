"""2877. Create a DataFrame from List

Write a solution to create a DataFrame from a 2D list called student_data. 
This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, student_id and age, 
and be in the same order as the original 2D list.

The result format is in the following example.
"""

import pandas as pd

def createDataframe(student_data: list) -> pd.DataFrame:
    ids = [x[0] for x in student_data]
    age = [x[1] for x in student_data]
    return pd.DataFrame({"student_id": ids, "age": age})