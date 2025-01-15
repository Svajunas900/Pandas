"""2878. Get the Size of a DataFrame

Write a solution to calculate and display the number of rows and columns of players.

Return the result as an array:

[number of rows, number of columns]

The result format is in the following example.
"""

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list:
    row, column = players.shape
    return [row, column]