# FarmTech Solutions --- Agricultura Digital (Python + R)

Projeto acadêmico desenvolvido para simular o trabalho de uma equipe de
desenvolvimento da **Startup FarmTech Solutions**, focada em soluções de
**Agricultura Digital**.

A aplicação permite:

-   Gerenciar dados de áreas agrícolas
-   Calcular área de plantio
-   Calcular uso de insumos
-   Exportar dados para análise
-   Realizar análise estatística em **R**
-   (Bônus) Consumir uma **API meteorológica pública**

------------------------------------------------------------------------

# Estrutura do Projeto

    farmtech-solutions
    │
    ├── python
    │   └── farmtech.py
    │
    ├── R
    │   ├── analise_estatistica.R
    │   └── analise_meteorologica.R
    │
    ├── relatorios
    │   ├── csv
    │   │   └── dados_fazenda.csv
    │   │
    │   └── txt
    │       └── relatorio_estatistico.txt
    │
    ├── link_video.txt
    └── README.md

------------------------------------------------------------------------

# Aplicação em Python

Arquivo:

    python/farmtech.py

Sistema em Python com **menu interativo no terminal** para gestão de
dados agrícolas.

Funcionalidades:

1.  Inserção de registros
2.  Listagem de dados
3.  Atualização de registros
4.  Remoção de registros
5.  Exportação para CSV

O sistema utiliza **listas (vetores)** para armazenar os dados.

## Culturas suportadas

### Cana-de-açúcar

-   Área em formato **retangular**
-   Cálculo de fertilizante em **kg por hectare**

### Café

-   Área em formato **circular**
-   Cálculo de pulverização em **mL por metro de rua**

------------------------------------------------------------------------

# Exportação de Dados

Os registros podem ser exportados para:

    relatorios/csv/dados_fazenda.csv

Estrutura do arquivo:

    idx;talhao;cultura;area_m2;area_ha;insumo_total;insumo_unidade

Esse arquivo é usado na análise estatística em R.

------------------------------------------------------------------------

# Análise Estatística em R

Arquivo:

    R/analise_estatistica.R

Este script:

-   lê o CSV exportado
-   converte colunas numéricas
-   calcula **média**
-   calcula **desvio padrão**
-   gera estatísticas por cultura

Também gera um relatório:

    relatorios/txt/relatorio_estatistico.txt

------------------------------------------------------------------------

# Bônus --- API Meteorológica

Arquivo:

    R/analise_meteorologica.R

Script em **R** que consulta a API pública **Open‑Meteo**.

Fluxo:

1.  Usuário informa uma cidade
2.  Script obtém latitude e longitude
3.  Consulta dados climáticos atuais
4.  Exibe no terminal

Dados exibidos:

-   temperatura atual
-   umidade
-   precipitação
-   vento
-   temperatura mínima e máxima do dia

------------------------------------------------------------------------

# Como Executar

## Executar aplicação Python

    python python/farmtech.py

------------------------------------------------------------------------

## Executar análise estatística em R

No terminal R:

    source("R/analise_estatistica.R")

------------------------------------------------------------------------

## Executar consulta meteorológica

    source("R/analise_meteorologica.R")

------------------------------------------------------------------------

# Tecnologias Utilizadas

Python: - math - csv - os

R: - dplyr - httr2 - jsonlite

------------------------------------------------------------------------

# Vídeo Demonstrativo

O vídeo com a demonstração do funcionamento do projeto está disponível
no arquivo:

    link_video.txt

------------------------------------------------------------------------

# Objetivo do Projeto

Aplicar conceitos de:

-   algoritmos
-   estruturas de decisão
-   estruturas de repetição
-   manipulação de vetores
-   análise estatística
-   integração com APIs

Simulando um ambiente de desenvolvimento voltado ao **agronegócio
digital**.
