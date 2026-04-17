import pandas as pd
import matplotlib.pyplot as plt

dados = pd.DataFrame({
    "Sexo": ["Masculino", "Feminino", "Outro"],
    "Quantidade": [55, 40, 5]
})

plt.pie(dados["Quantidade"], labels=dados["Sexo"], autopct="%1.1f%%")
plt.title("Distribuição por Sexo")
plt.show()