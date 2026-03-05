# =========================================
# FarmTech Solutions - Análise Estatística (R)
# Média e desvio padrão a partir do CSV exportado
# =========================================

# (Opcional) instalar pacote caso não tenha
# install.packages("dplyr")

library(dplyr)

# --- 1) Caminho do arquivo ---
# Ajuste o nome do arquivo conforme o que você exportou no Python.
arquivo <- "farmtech-solutions/relatorios/csv/dados_fazenda.csv"

# --- 2) Leitura do CSV (separador ;) ---
dados <- read.csv(arquivo, sep = ";", stringsAsFactors = FALSE)

# --- 3) Garantir tipos numéricos ---
dados$area_m2 <- as.numeric(dados$area_m2)
dados$area_ha <- as.numeric(dados$area_ha)
dados$insumo_total <- as.numeric(dados$insumo_total)

# --- 4) Estatística geral ---
stats_geral <- dados |>
  summarize(
    n_registros = n(),
    media_area_ha = mean(area_ha, na.rm = TRUE),
    desvio_area_ha = sd(area_ha, na.rm = TRUE),
    media_insumo_total = mean(insumo_total, na.rm = TRUE),
    desvio_insumo_total = sd(insumo_total, na.rm = TRUE)
  )

cat("\n=== Estatística Geral ===\n")
print(stats_geral)

# --- 5) Estatística por cultura ---
stats_por_cultura <- dados |>
  group_by(cultura) |>
  summarize(
    n = n(),
    media_area_ha = mean(area_ha, na.rm = TRUE),
    desvio_area_ha = sd(area_ha, na.rm = TRUE),
    media_insumo_total = mean(insumo_total, na.rm = TRUE),
    desvio_insumo_total = sd(insumo_total, na.rm = TRUE),
    .groups = "drop"
  )

cat("\n=== Estatística por Cultura ===\n")
print(stats_por_cultura)

# --- 6) salvar relatório ---
relatorio_path <- "farmtech-solutions/relatorios/txt/relatorio_estatistico.txt"

sink(relatorio_path)
cat("FarmTech Solutions - Relatório Estatístico\n")
cat("Arquivo analisado:", arquivo, "\n\n")

cat("=== Estatística Geral ===\n")
print(stats_geral)

cat("\n=== Estatística por Cultura ===\n")
print(stats_por_cultura)
sink()

cat("\nRelatório salvo em:", relatorio_path, "\n")
