import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from math import pi

file_path = '_Avaliação 360 - Outubro (respostas) - Respostas ao formulário 1.csv'  # Substitua pelo caminho correto do arquivo CSV
df = pd.read_csv(file_path)

# Mapeamento de colunas (mesmo do anterior para consistência)
col_map = {
    'Como você avalia seu nível de comprometimento nas atividades da liga?': 'Comprometimento',
    'Você se sente produtivo e engajado nas tarefas propostas?': 'Produtividade',
    'Quão confortável você se sente para propor ideias e colaborar com a equipe?': 'Seguranca_Psicologica',
    'RH: A diretoria contribui para um ambiente organizacional saudável e proporciona suporte adequado aos membros?': 'RH',
    'Pesquisa: A diretoria contribui para o desenvolvimento de conteúdo científico no âmbito acadêmico?': 'Pesquisa',
    'Projetos: A diretoria realiza a gestão eficiente das atividades e entrega resultados esperados?': 'Projetos',
    'Marketing: As estratégias de comunicação e divulgação têm gerado impacto positivo na liga?': 'Marketing',
    'Administrativo: A diretoria fornece o suporte necessário para o bom funcionamento das atividades?': 'Administrativo',
    'Secretaria: Tem garantido a organização e o fluxo eficiente das informações dentro da liga?  ': 'Secretaria',
    'Presidência: A Presidência tem demonstrado liderança eficaz e proporcionado a visão estratégica necessária para o crescimento da liga?  ': 'Presidencia'
}
df.rename(columns=col_map, inplace=True)

# Converter colunas de notas para numérico
diretorias = ['RH', 'Pesquisa', 'Projetos', 'Marketing', 'Administrativo', 'Secretaria', 'Presidencia']
for col in diretorias:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# --- GRÁFICO 1: RADAR CHART (PERFORMANCE DIRETORIAS) ---
# Preparar dados
medias = df[diretorias].mean()
categorias = list(medias.index)
valores = medias.values.flatten().tolist()
valores += valores[:1] # Fechar o ciclo
angulos = [n / float(len(categorias)) * 2 * pi for n in range(len(categorias))]
angulos += angulos[:1]

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
plt.xticks(angulos[:-1], categorias, color='grey', size=10)
ax.set_rlabel_position(0)
plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=7)
plt.ylim(0, 5.5)

# Plotar
ax.plot(angulos, valores, linewidth=2, linestyle='solid', color='#4A90E2') # Azul Tech
ax.fill(angulos, valores, '#4A90E2', alpha=0.25)
plt.title('Performance 360º das Diretorias', size=15, y=1.1)
plt.tight_layout()
plt.savefig('grafico_radar_diretorias.png')
plt.close()

# --- GRÁFICO 2: PAINEL DE ENGAJAMENTO (SUBPLOTS) ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Comprometimento
sns.countplot(x='Comprometimento', data=df, ax=axes[0], palette='viridis', order=['Muito Alto', 'Alto', 'Moderado', 'Baixo'])
axes[0].set_title('Nível de Comprometimento Declarado')
axes[0].set_ylabel('Quantidade de Membros')
axes[0].set_xlabel('')

# Produtividade
sns.countplot(x='Produtividade', data=df, ax=axes[1], palette='magma', order=['Sempre', 'Algumas vezes', 'Raramente'])
axes[1].set_title('Percepção de Produtividade')
axes[1].set_ylabel('')
axes[1].set_xlabel('')

plt.tight_layout()
plt.savefig('grafico_engajamento.png')
plt.close()

# --- GRÁFICO 3: SEGURANÇA PSICOLÓGICA ---
plt.figure(figsize=(8, 5))
sns.histplot(df['Seguranca_Psicologica'], bins=5, kde=True, color='#50E3C2') # Verde Startup
plt.title('Distribuição da Segurança Psicológica (Conforto em propor ideias)')
plt.xlabel('Nota (1-5)')
plt.ylabel('Frequência')
plt.xlim(1, 5.5)
plt.tight_layout()
plt.savefig('grafico_seguranca.png')
plt.close()

print("Gráficos gerados com sucesso: Radar, Engajamento e Segurança Psicológica.")