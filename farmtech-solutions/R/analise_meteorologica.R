# ============================
# BÔNUS: Clima via API (Open-Meteo) em R
# - Busca coordenadas por cidade (Geocoding API)
# - Busca previsão/tempo atual (Forecast API)
# - Exibe via texto no terminal
# ============================

# install.packages(c("httr2", "jsonlite"))  # rode 1x se não tiver
library(httr2)
library(jsonlite)

# 1) Busca coordenadas (lat/lon) a partir do nome de uma cidade
buscar_coordenadas <- function(cidade, pais = NULL) {
  req <- request(
    "https://geocoding-api.open-meteo.com/v1/search"
  ) |>
    req_url_query(
      name = cidade,
      count = 1,
      language = "pt",
      format = "json"
    )

  if (!is.null(pais) && nzchar(pais)) {
    req <- req |> req_url_query(country_code = pais)
  }

  resp <- req |> req_perform()
  txt <- resp |> resp_body_string()
  j <- fromJSON(txt)

  if (is.null(j$results) || length(j$results) == 0) {
    stop("Cidade não encontrada no geocoding.")
  }

  list(
    name = j$results$name[1],
    admin1 = j$results$admin1[1],
    country = j$results$country[1],
    latitude = j$results$latitude[1],
    longitude = j$results$longitude[1],
    timezone = j$results$timezone[1]
  )
}

# 2) Busca clima (tempo atual + daily simples)
buscar_clima <- function(lat, lon, timezone = "auto") {
  req <- request("https://api.open-meteo.com/v1/forecast") |>
    req_url_query(
      latitude = lat,
      longitude = lon,
      current = paste(
        "temperature_2m,relative_humidity_2m,precipitation,",
        "wind_speed_10m",
        sep = ""
      ),
      daily = paste(
        "temperature_2m_max,temperature_2m_min,precipitation_sum,",
        "wind_speed_10m_max",
        sep = ""
      ),
      timezone = timezone
    )

  resp <- req |> req_perform()
  txt <- resp |> resp_body_string()
  fromJSON(txt)
}

imprimir_resumo <- function(local, clima) {
  cat("\n=== FarmTech - Clima (API Open-Meteo) ===\n")
  cat(
    "Local:", local$name, "-", local$admin1, "-",
    local$country, "\n"
  )
  cat("Coordenadas:", local$latitude, ",", local$longitude, "\n")
  cat("Timezone:", local$timezone, "\n")

  # current
  cur <- clima$current
  cat("\n--- Agora ---\n")
  cat("Temperatura (°C):", cur$temperature_2m, "\n")
  cat("Umidade (%):", cur$relative_humidity_2m, "\n")
  cat("Precipitação (mm):", cur$precipitation, "\n")
  cat("Vento (km/h):", cur$wind_speed_10m, "\n")

  # daily (hoje)
  d <- clima$daily
  cat("\n--- Hoje (daily) ---\n")
  cat("Data:", d$time[1], "\n")
  cat("Temp. mínima (°C):", d$temperature_2m_min[1], "\n")
  cat("Temp. máxima (°C):", d$temperature_2m_max[1], "\n")
  cat("Chuva total (mm):", d$precipitation_sum[1], "\n")
  cat("Vento máx (km/h):", d$wind_speed_10m_max[1], "\n")
}

# ===== Execução =====
cidade <- readline("Digite a cidade (ex: Sao Paulo): ")
if (!nzchar(cidade)) cidade <- "Sao Paulo"

pais <- readline("Country code (enter p/ ignorar, ex: BR): ")
if (!nzchar(pais)) pais <- NULL

local <- buscar_coordenadas(cidade, pais)
clima <- buscar_clima(
  local$latitude, local$longitude,
  timezone = local$timezone
)
imprimir_resumo(local, clima)
