#!/usr/bin/env python
# coding: utf-8

# # Filmes Vencedores
# * Orçamento: Média de 100 milhões, com desvio padrão de 80 milhões.
# * Bilheteria: Média de 5 vezes o orçamento. Com desvio padrão de 3. 
# * Tempo em Cartaz: Média de 3 semanas, com desvio padrão de 1 semana e mínimo de 1.
# * Diretor: 50 diretores já venceram o oscar. Total 200.
# * Roteirista: 50 roteiristas já venceram o oscar. Total 500.
# * Ator Principal: 100 atores principais já venceram o oscar. Total 1000.
# * Número de Outras Indicações da Awards Season. 40 com desvio padrão de 10. 
# 
# # Filmes Não Vencedores
# * Orçamento: Distribuição uniforme de 2 milhões a 500 milhões.
# * Bilheteria: Distribuição uniforme de 2 a 500 milhões.
# * Tempo em Cartaz: Distribuição uniforme de 1 a 8 semanas.
# * Diretor, Roteirista, Ator: Distribuição uniforme. (cada um participou de, aproximadamente a mesma quantidade de filmes).
# * Número de Outras Indicações da Award Season. Média 10 com desvio padrão 40.

# In[30]:


import numpy as np;
import pandas as pd;

VENCEDORES = 50;
DEMAIS = 100;

orcamento_vencedores = np.random.normal(100, 80, VENCEDORES);
bilheteria_vencedores = np.random.normal(5,2, VENCEDORES)*orcamento_vencedores;
tempo_cartaz_vencedores = np.random.gamma(2, 2, VENCEDORES);
outras_indicacoes = np.random.gamma(40, 2, VENCEDORES);

diretores = range(0, 200);
roteiristas = range(0, 500);
atores = range(0,1000);


diretores_vencedores = np.random.choice(50, VENCEDORES);
roteiristas_vencedores = np.random.choice(50, VENCEDORES);
atores_vencedores = np.random.choice(100, VENCEDORES);


# In[31]:


tabela = np.vstack([orcamento_vencedores, 
                   bilheteria_vencedores,
                  tempo_cartaz_vencedores,
                  outras_indicacoes,
                  diretores_vencedores,
                  roteiristas_vencedores,
                  atores_vencedores]).T


# In[32]:


colunas = ["orcamento_vencedores", 
                   "bilheteria_vencedores",
                  "tempo_cartaz_vencedores",
                  "outras_indicacoes",
                  "diretores_vencedores",
                  "roteiristas_vencedores",
                  "atores_vencedores"]
df = pd.DataFrame(tabela, columns = colunas)
df.index.name = "Filme"
df.head()


# In[33]:


df.to_csv("vencedores.csv")


# In[ ]:




