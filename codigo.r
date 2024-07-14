# Carregar os pacotes necessários
library(ggplot2)

# Função para calcular o volume de calda pulverizado
calcular_volume_calda <- function(absorbancias_amostras, absorbancias_calibracao, concentracoes_calibracao, area_folha_m2, 
                                  concentracao_mae=1000, volume_lavagem=20) {
  # Ajuste da curva de calibração usando regressão linear
  modelo <- lm(concentracoes_calibracao ~ absorbancias_calibracao)
  
  # Coeficientes da reta de calibração
  coeficiente_angular <- coef(modelo)[2]
  intercepto <- coef(modelo)[1]
  
  # Listas para armazenar os volumes de calda pulverizados
  volumes_calda_pulverizados_mL <- numeric(length(absorbancias_amostras))
  volumes_calda_pulverizados_L_ha <- numeric(length(absorbancias_amostras))
  
  for (i in 1:length(absorbancias_amostras)) {
    A <- absorbancias_amostras[i]
    
    # Calcular a concentração da amostra usando a reta de calibração
    concentracao_amostra <- coeficiente_angular * A + intercepto
    
    # Calcular o volume de calda pulverizado na folha (em mL)
    volume_calda_pulverizado_mL <- (concentracao_amostra * volume_lavagem) / concentracao_mae
    volumes_calda_pulverizados_mL[i] <- volume_calda_pulverizado_mL
    
    # Converter o volume de calda pulverizado para L/ha
    volume_calda_pulverizado_L_ha <- (volume_calda_pulverizado_mL * 10^(-3)) / area_folha_m2 * 10^4
    volumes_calda_pulverizados_L_ha[i] <- volume_calda_pulverizado_L_ha
  }
  
  return(list(volumes_mL = volumes_calda_pulverizados_mL, volumes_L_ha = volumes_calda_pulverizados_L_ha))
}

# Exemplo de uso:
absorbancias_calibracao <- c(2.7931, 1.3943, 0.6945, 0.3601, 0.1738, 0.0882, 0.0467, 0.0286, 0.0294, 0.0033)
concentracoes_calibracao <- c(19.60784314, 9.803921569, 4.901960784, 2.450980392, 1.225490196, 0.612745098, 
                              0.306372549, 0.153186275, 0.076593137, 0.038296569)

# Absorbâncias das novas amostras a serem analisadas
absorbancias_amostras <- c(0.0523, 0.1000, 0.2000)  # Exemplo de valores

# Área da folha em metros quadrados
area_folha_m2 <- 0.0003585  # Exemplo de área, substitua pelo valor real

# Calcular os volumes de calda pulverizados para as novas amostras
resultados <- calcular_volume_calda(absorbancias_amostras, absorbancias_calibracao, concentracoes_calibracao, area_folha_m2)
volumes_calda_mL <- resultados$volumes_mL
volumes_calda_L_ha <- resultados$volumes_L_ha

# Exibir os resultados
for (i in 1:length(volumes_calda_mL)) {
  cat(sprintf("Volume de calda pulverizado para a amostra %d: %.6f mL (%.6f L/ha)\n", 
              i, volumes_calda_mL[i], volumes_calda_L_ha[i]))
}

# Calcular o volume depositado em microlitros por cm²
volume_depositado_uL_cm2 <- volumes_calda_mL * 1000 / (area_folha_m2 * 10^4)

# Criar um data frame para a plotagem
df <- data.frame(Volume_uL_cm2 = volume_depositado_uL_cm2)

# Plotar o gráfico de frequência acumulada usando ggplot2
ggplot(df, aes(x = Volume_uL_cm2)) +
  stat_ecdf(geom = "step") +
  labs(title = "Frequência Acumulada por Volume Depositado",
       x = "Volume Depositado (µL/cm²)",
       y = "Frequência Acumulada") +
  theme_minimal()
