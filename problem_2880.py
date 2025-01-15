"""2880. Select Data

Write a solution to select the name and age of the student with student_id = 101.

The result format is in the following example.
"""

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    student = students.loc[students["student_id"]==101]
    return student[['name', 'age']]