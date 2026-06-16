import matplotlib.pyplot as plt
import os

# Esta parte adicionada verifica se a pasta 'assets' existe.
# Se não existir, o script a cria automaticamente para você.
if not os.path.exists('assets'):
    os.makedirs('assets')

# Dados
anos = ['2024', '2025']
vendas = [177358, 223912]

# Estilo
plt.figure(figsize=(8, 5))
plt.bar(anos, vendas, color=['#4F46E5', '#312E81'])
plt.title('Evolução de Vendas de Veículos Eletrificados (ABVE)')
plt.ylabel('Unidades Vendidas')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Agora ele vai salvar na pasta que ele mesmo acabou de criar
plt.savefig('assets/evolucao_frota.png', dpi=300)
print("Gráfico gerado com sucesso na pasta 'assets'!")


