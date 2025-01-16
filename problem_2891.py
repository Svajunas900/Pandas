"""2891. Method Chaining


Write a solution to list the names of animals that weigh strictly more than 100 kilograms.

Return the animals sorted by weight in descending order.

The result format is in the following example.
"""

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
  return pd.DataFrame(
      animals.sort_values(by='weight', ascending=False).where(animals["weight"] > 100).dropna().get('name'))