# %% [markdown]
# ## Applying the PPS to the Titanic dataset
# - This script shows you how to apply the PPS to the Titanic dataset
# - If you want to execute the script yourself, you need to have valid installations of the packages ppscore and seaborn. (Other packages like pandas will be installed together with ppscore.)

# %%
import pandas as pd
import seaborn as sns

import ppscore as pps


# %%
def heatmap(df):
    return sns.heatmap(df, vmin=0, vmax=1, cmap="Blues", linewidths=0.5, annot=True)


# %%
df = pd.read_csv("titanic.csv")

# %% [markdown]
# ## Preparation of the Titanic dataset
# - Selecting a subset of columns
# - Changing some data types
# - Renaming the column names to be more clear

# %%
df = df[["Survived", "Pclass", "Sex", "Age", "Ticket", "Fare", "Embarked"]]
df["Survived"] = df["Survived"].astype(bool, errors="raise")
df["Pclass"] = df["Pclass"].astype(str, errors="raise")
df = df.rename(columns={"Pclass": "Class"})
df = df.rename(columns={"Ticket": "TicketID"})
df = df.rename(columns={"Fare": "TicketPrice"})
df = df.rename(columns={"Embarked": "Port"})

# %% [markdown]
# ## Single Predictive Power Score
# - Answering the question: how well can Sex predict the Survival probability?

# %%
pps.score(df, "Sex", "Survived")

# %% [markdown]
# ## PPS matrix
# - Answering the question: which predictive patterns exist between the columns?

# %%
matrix = pps.matrix(df)

# %%
matrix

# %%
heatmap(matrix)

# %%