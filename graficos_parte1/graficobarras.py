import pandas as pd
import matplotlib.pyplot as plt

# Dados categóricos
dados = pd.DataFrame({
    "Produto": ["A", "B", "C", "D", "E"],
    "Vendas": [120, 90, 150, 60, 110]
})

# Gráfico de barras
plt.bar(dados["Produto"], dados["Vendas"])
plt.title("Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade de Vendas")
plt.show()