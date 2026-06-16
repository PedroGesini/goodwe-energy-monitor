import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from pathlib import Path

# ==================================
# CARREGAR DADOS
# ==================================

BASE_DIR = Path(__file__).resolve().parent.parent
caminho_csv = BASE_DIR / "data" / "dataset_ia_goodwe.csv"

print("Caminho do CSV:", caminho_csv)
print("Existe?", caminho_csv.exists())

#leitura dados CSV
df = pd.read_csv(
    caminho_csv,
    sep=",",
    encoding="utf-8",
    engine="c",
    skipinitialspace=True
)

# ==================================
# PREPARAÇÃO DOS DADOS (IA MELHORADA)
# ==================================

# remove possíveis linhas vazias
df.fillna(0)

X = df[[
    "uso_carga_kwh",
    "autoconsumo_kwh",
    "energia_injetada_kwh",
    "energia_comprada_kwh"
]]

y = df["geracao_kwh"]

# ==================================
# TREINAR IA
# ==================================

modelo = LinearRegression()
modelo.fit(X, y)

# ==================================
# PREVISÕES
# ==================================

previsoes = modelo.predict(X)

# ==================================
# PREVISÃO FUTURA (BASEADA NA MÉDIA)
# ==================================

proximo_input = X.mean().values.reshape(1, -1)
previsao_futura = modelo.predict(proximo_input)

print("\n====================================")
print("RESULTADOS DA IA")
print("====================================")

print(
    f"\nPrevisão de geração futura: {previsao_futura[0]:.2f} kWh"
)

# ==================================
# QUALIDADE DO MODELO
# ==================================

r2 = r2_score(y, previsoes)
print(f"\nPrecisão (R²): {r2:.2f}")

# ==================================
# EXIBIR PREVISÕES
# ==================================

print("\nComparação:")

for real, previsto in zip(y, previsoes):
    print(f"Real: {real:.2f} kWh | Previsto: {previsto:.2f} kWh")

# ==================================
# GRÁFICO
# ==================================

plt.figure(figsize=(10, 5))

plt.plot(df.index, y, marker="o", label="Dados Reais")
plt.plot(df.index, previsoes, label="Previsão IA")

plt.xlabel("Dia")
plt.ylabel("Geração (kWh)")
plt.title("Previsão de Geração de Energia - FIAP")
plt.legend()
plt.grid(True)

plt.show()