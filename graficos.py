#%%

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv("data/dados.csv")
df.head()


# %%


group_prod = df.groupby("descProduto")["idTransacao"].count().reset_index()
group_prod
# %%

sns.barplot(group_prod, y="descProduto", x="idTransacao")
plt.ylabel("Descrição Produto")
plt.xlabel("nº transação")

# %%


df["dtTransacao"] = pd.to_datetime(df["dtTransacao"]).dt.date

# %%

group_dt = df.groupby("dtTransacao").agg(
    {
        "qtdPontos" : "sum",
        "idTransacao" : "count"
    }
).reset_index()

group_dt.sort_values("dtTransacao", inplace=True)
# %%

plt.figure(figsize=(10,8))
plt.plot(group_dt["dtTransacao"], group_dt["idTransacao"])
# %%


plt.hist(group_dt["qtdPontos"], bins= 18, density=True)
# %%


plt.boxplot(group_dt["qtdPontos"])

# %%
