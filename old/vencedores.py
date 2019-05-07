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


VENCEDORES = 3000;

# Setando o random seed
np.random.seed(seed=3);
# Gênero
generos_composicao_v = [
    (1, 'Action' , 0),
    (2, 'Adventure' , 0),
    (3, 'Biography' , 0.1875),
    (4, 'Comedy' , 0.0625),
    (5, 'Crime' , 0),
    (6, 'Drama' , 0.25),
    (7, 'Fantasy' , 0.0625),
    (8, 'History' , 0.125),
    (9, 'Horror' , 0),
    (10, 'Music' , 0),
    (11, 'Romance' , 0.0625),
    (12, 'Thriller' , 0.1875),
    (13, 'War' , 0.0625),
    (14, 'Sci-Fi' , 0),
]
prob_generos_v = [g[2] for g in generos_composicao_v];

generos_v = np.random.choice(len(prob_generos_v), VENCEDORES, p = prob_generos_v);

# Atributos - Distribuições Normal (v = vencedores, d = demais)
tomatometer_v   = np.random.normal(91.53,  6.79,   VENCEDORES);
tomatometer_v   = np.clip(tomatometer_v, 0, 100); # para nao termos valores acima de 100 ou abaixo de 0.

metacritics_v     = np.random.normal(87.07, 8.4, VENCEDORES);
metacritics_v    = np.clip(metacritics_v, 0, 100);

letterboxd_v    = np.random.normal(3.84, 0.32, VENCEDORES);
letterboxd_v    = np.clip(letterboxd_v, 0, 5);

orcamento_v     = np.random.normal(23.86,  20.7,   VENCEDORES);
orcamento_v     = np.clip(orcamento_v, 1, np.Infinity); 

bilheteria_v    = np.random.normal(191.81, 108.35, VENCEDORES);
bilheteria_v     = np.clip(bilheteria_v, 1, np.Infinity); 

lucro_v         = bilheteria_v - orcamento_v;


# Atributos - Sim/Não
# Probabilidades        [NAO,       SIM]
prob_atores_v =         [0.4667,     0.5333]
prob_diretores_v =      [0.1333,     0.8667]
prob_golden_globes_v =  [0.6000,     0.4000]
prob_bafta_v =          [0.6000,     0.4000]

# Gerando os dados
atores_v        = np.random.choice(2, VENCEDORES, p=prob_atores_v);
diretores_v     = np.random.choice(2, VENCEDORES, p=prob_diretores_v);
golden_globes_v = np.random.choice(2, VENCEDORES, p=prob_golden_globes_v); 
bafta_v         = np.random.choice(2, VENCEDORES, p=prob_bafta_v);


tabela = np.vstack([
        generos_v,
        tomatometer_v, metacritics_v, letterboxd_v,
        orcamento_v, bilheteria_v, lucro_v, 
        atores_v, diretores_v, golden_globes_v, bafta_v
        ]).T



colunas = [
    "Gênero",
    "Tomatômetro - Rotten Tomatoes (%)",
    "Metacritics",
    "LetterBoXD",
    "Orçamento - Milhões ($)",
    "Bilheteria - Milhões ($)",
    "Lucro - Milhões ($)",
    "Ator/Atriz Indicado ao Oscar",
    "Diretor/Diretora Indicado ao Oscar",
    "Vencedor do Golden Globes",
    "Vencedor do Bafta",
    
]
df = pd.DataFrame(tabela, columns = colunas)
df.index.name = "Filme"
df.head()
df.to_csv("the_vencedores.csv")


print("Vencedores Criados.")