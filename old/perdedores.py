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

PERDEDORES = 3000;

# Setando o random seed
np.random.seed(seed=3);

# Gênero
generos_composicao_p = [
            (1,"Action",0.0333),
            (2,"Adventure",0.1000),
            (3,"Biography",0.2334),
            (4,"Comedy",0.0667),
            (5,"Crime",0.0334),
            (6,"Drama",0.1333),
            (7,"Fantasy",0.0000),
            (8,"History",0.1333),
            (9,"Horror",0.0333),
            (10,"Music",0.0333),
            (11,"Romance",0.1333),
            (12,"Thriller",0.0000),
            (13,"War",0.0000),
            (14,"Sci-Fi",0.0667)
]
prob_generos_p = [g[2] for g in generos_composicao_p];

generos_p = np.random.choice(len(prob_generos_p), PERDEDORES, p = prob_generos_p);

#Atributos - Distribuições Normal (P = perdedores, d = demais)
tomatometer_p   = np.random.normal(88,  9.3,   PERDEDORES);
tomatometer_p   = np.clip(tomatometer_p, 0, 100); # para nao termos valores acima de 100 ou abaixo de 0.

metacritics_p     = np.random.normal(81.56, 10.23, PERDEDORES);
metacritics_p    = np.clip(metacritics_p, 0, 100);

letterboxd_p    = np.random.normal(3.74, 0.28, PERDEDORES);
letterboxd_p    = np.clip(letterboxd_p, 0, 5);

orcamento_p     = np.random.normal(44.3,  49.5,   PERDEDORES);
orcamento_p     = np.clip(orcamento_p, 1, np.Infinity); 

bilheteria_p    = np.random.normal(267.5, 287.9, PERDEDORES);
bilheteria_p     = np.clip(bilheteria_p, 1, np.Infinity); 

lucro_p         = bilheteria_p - orcamento_p;


# Atributos - Sim/Não
# Probabilidades        [NAO,       SIM]
prob_atores_p =         [0.6774,     0.3226]
prob_diretores_p =      [0.4667,     0.5333]
prob_golden_globes_p =  [0.8966,     0.1034]
prob_bafta_p =          [0.8667,     0.1333]

# Gerando os dados
atores_p        = np.random.choice(2, PERDEDORES, p=prob_atores_p);
diretores_p     = np.random.choice(2, PERDEDORES, p=prob_diretores_p);
golden_globes_p = np.random.choice(2, PERDEDORES, p=prob_golden_globes_p); 
bafta_p         = np.random.choice(2, PERDEDORES, p=prob_bafta_p);


tabela = np.vstack([
        generos_p,
        tomatometer_p, metacritics_p, letterboxd_p,
        orcamento_p, bilheteria_p, lucro_p, 
        atores_p, diretores_p, golden_globes_p, bafta_p
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
df.to_csv("the_perdedores.csv")


print("Perdedores criados.");