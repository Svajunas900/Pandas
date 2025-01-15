"""2883. Drop Missing Data

There are some rows having missing values in the name column.

Write a solution to remove the rows with missing values.

The result format is in the following example.
"""

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])