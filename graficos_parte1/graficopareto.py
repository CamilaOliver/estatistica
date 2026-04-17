import pandas as pd
import matplotlib.pyplot as plt

dados = pd.DataFrame({
    "Setor": ["Entrega", "Atendimento", "Produto", "Pagamento", "Site"],
    "Reclamacoes": [80, 50, 30, 20, 10]
})

# Ordenar do maior para o menor
dados = dados.sort_values(by="Reclamacoes", ascending=False)

# Calcular percentual e acumulado
dados["Percentual"] = dados["Reclamacoes"] / dados["Reclamacoes"].sum() * 100
dados["Acumulado"] = dados["Percentual"].cumsum()

# Criar gráfico
fig, ax1 = plt.subplots()

# Barras (reclamações)
ax1.bar(dados["Setor"], dados["Reclamacoes"])
ax1.set_ylabel("Reclamações")
ax1.set_title("Gráfico de Pareto - Reclamações por Setor")

# Linha acumulada (%)
ax2 = ax1.twinx()
ax2.plot(dados["Setor"], dados["Acumulado"], marker="o")
ax2.set_ylabel("% Acumulado")
ax2.set_ylim(0, 110)

plt.show()