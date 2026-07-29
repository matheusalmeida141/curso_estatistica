# %%

import pandas as pd
import sqlalchemy

df = pd.read_csv("data/dados.csv")
df.head()


engine = sqlalchemy.create_engine("sqlite:///data/dados.db")

df.to_sql("points", engine, if_exists="replace", index=False)
# %%

freq_produto = df.groupby("descProduto")[["idTransacao"]].count()
freq_produto["FreqAA"] = freq_produto["idTransacao"].cumsum()
freq_produto["FreqR"] = freq_produto["idTransacao"]/freq_produto["idTransacao"].sum()
freq_produto["FreqRA"] = freq_produto["FreqR"].cumsum()
freq_produto


#%%


freq_CP = df.groupby("descCategoriaProduto")[["idTransacao"]].count()
freq_CP["FreqR"] = freq_CP["idTransacao"]/freq_CP["idTransacao"].sum()
freq_CP["FreqA"] = freq_CP["idTransacao"].cumsum()
freq_CP["FreqAR"] = freq_CP["FreqR"].cumsum()

freq_CP


# %%
