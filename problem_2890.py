"""2890. Reshape Data: Melt

Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.

The result format is in the following example.
"""

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
  return pd.melt(report, id_vars=['product'], 
                 value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], 
                 value_name = 'sales', 
                 var_name = 'quarter')