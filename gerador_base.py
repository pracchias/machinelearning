#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# In[1]:
import numpy as np;
import pandas as pd;



VENCEDORES = 3000;
PERDEDORES = 3000;
OUTPUT_FILE = "./the_base.csv"

# In[2]:
def gera_vencedores():
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
    print("Vencedores Criados.");
    return tabela;

def gera_perdedores():
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
    print("Perdedores criados.")
    return tabela

# In[3]:
vencedores = gera_vencedores();
perdedores = gera_perdedores();

# In[4]:
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

# In[]:
df_vencedores = pd.DataFrame(vencedores, columns=colunas);
df_perdedores = pd.DataFrame(perdedores, columns=colunas);
df_vencedores['Classe'] = 1 # VENCEDOR
df_perdedores['Classe'] = 0 # NÃO VENCEDOR
base = df_vencedores.append(df_perdedores);
base.index.name = "FilmeId"
base.head()

# In[5]
base.to_csv(OUTPUT_FILE, sep=";", decimal=",");

