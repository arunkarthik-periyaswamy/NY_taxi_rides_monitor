import random

import numpy as np
import pandas as pd
import streamlit as st

st.write(
    """
# My first app
Hello *world!* sdfsdfsdfsdf
"""
)


num_rows = 100
data = {
    "ID": range(1, num_rows + 1),
    "Name": ["Person_" + str(i) for i in range(1, num_rows + 1)],
    "Age": np.random.randint(18, 65, num_rows),
    "City": [
        random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])
        for _ in range(num_rows)
    ],
    "Salary": np.random.randint(30000, 150000, num_rows),
    "Department": [
        random.choice(["Sales", "Marketing", "IT", "HR", "Finance"])
        for _ in range(num_rows)
    ],
    "Join_Date": pd.date_range(
        start="2023-01-01", periods=num_rows, freq="D"
    ).to_list(),
}

df = pd.DataFrame(data)

st.dataframe(df)
