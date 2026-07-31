# %%
import pandas as pd

df = pd.read_csv("data/dados.csv", sep=',')
df.head()



# %%

minimo = df["qtdPontos"].min()

media = df["qtdPontos"].mean()

q1 = df["qtdPontos"].quantile(0.25)

mediana = df["qtdPontos"].quantile(0.50)

q3 = df["qtdPontos"].quantile(0.75)

maximo = df["qtdPontos"].max()

varianca = df["qtdPontos"].var()

desvio = df["qtdPontos"].std()

print(f"minimo: {minimo} \nmedia: {media} \n\
      1q: {q1} \nmediana: {mediana} \n 3q: {q3} \nmax:{maximo} \nvarianca: {varianca} \ndesvio:{desvio}")


# %%

usuarios = df.groupby("idUsuario").agg({"qtdPontos": "sum", "idTransacao":"count"})

# %%
usuarios.head()

# %%

usuarios[["idTransacao", "qtdPontos"]].describe()
# %%
