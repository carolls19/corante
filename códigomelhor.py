import numpy as np
from sklearn.linear_model import LinearRegression

def calcular_volume_calda(absorbancias_amostras, absorbcao_calibracao, concentracoes_calibracao, concentracao_mae=1000, volume_lavagem=20):
    # Ajuste da curva de calibração
    X = absorbcao_calibracao.reshape(-1, 1)
    y = concentracoes_calibracao

    # Criar e treinar o modelo de regressão linear
    model = LinearRegression()
    model.fit(X, y)

    # Coeficientes da reta de calibração
    coeficiente_angular = model.coef_[0]
    intercepto = model.intercept_

    # Lista para armazenar os volumes de calda pulverizados
    volumes_calda_pulverizados = []

    for A in absorbancias_amostras:
        # Calcular a concentração da amostra usando a reta de calibração
        concentracao_amostra = coeficiente_angular * A + intercepto

        # Calcular o volume de calda pulverizado na folha (em ml)
        volume_calda_pulverizado = (concentracao_amostra * volume_lavagem) / concentracao_mae
        volumes_calda_pulverizados.append(volume_calda_pulverizado)

    return volumes_calda_pulverizados

# Exemplo de uso:
absorbancias_calibracao = np.array([2.7931, 1.3943, 0.6945, 0.3601, 0.1738, 0.0882, 0.0467, 0.0286, 0.0294, 0.0033])
concentracoes_calibracao = np.array([19.60784314, 9.803921569, 4.901960784, 2.450980392, 1.225490196, 0.612745098, 0.306372549, 0.153186275, 0.076593137, 0.038296569])

# Absorbâncias das novas amostras a serem analisadas
absorbancias_amostras = [0.0523, 0.1000, 0.2000]  # Exemplo de valores

# Calcular os volumes de calda pulverizados para as novas amostras
volumes_calda = calcular_volume_calda(absorbancias_amostras, absorbancias_calibracao, concentracoes_calibracao)

# Exibir os resultados
for i, volume in enumerate(volumes_calda):
    print(f"Volume de calda pulverizado para a amostra {i+1}: {volume:.6f} mL")

import numpy as np
from sklearn.linear_model import LinearRegression

def calcular_volume_calda(absorbancias_amostras, absorbcao_calibracao, concentracoes_calibracao, area_folha_m2, concentracao_mae=1000, volume_lavagem=20):
    # Ajuste da curva de calibração
    X = absorbcao_calibracao.reshape(-1, 1)
    y = concentracoes_calibracao

    # Criar e treinar o modelo de regressão linear
    model = LinearRegression()
    model.fit(X, y)

    # Coeficientes da reta de calibração
    coeficiente_angular = model.coef_[0]
    intercepto = model.intercept_

    # Lista para armazenar os volumes de calda pulverizados
    volumes_calda_pulverizados_mL = []
    volumes_calda_pulverizados_L_ha = []

    for A in absorbancias_amostras:
        # Calcular a concentração da amostra usando a reta de calibração
        concentracao_amostra = coeficiente_angular * A + intercepto

        # Calcular o volume de calda pulverizado na folha (em ml)
        volume_calda_pulverizado_mL = (concentracao_amostra * volume_lavagem) / concentracao_mae
        volumes_calda_pulverizados_mL.append(volume_calda_pulverizado_mL)

        # Converter o volume de calda pulverizado para L/ha
        volume_calda_pulverizado_L_ha = (volume_calda_pulverizado_mL * 10**-3) / area_folha_m2 * 10**4
        volumes_calda_pulverizados_L_ha.append(volume_calda_pulverizado_L_ha)

    return volumes_calda_pulverizados_mL, volumes_calda_pulverizados_L_ha

# Exemplo de uso:
absorbancias_calibracao = np.array([2.7931, 1.3943, 0.6945, 0.3601, 0.1738, 0.0882, 0.0467, 0.0286, 0.0294, 0.0033])
concentracoes_calibracao = np.array([19.60784314, 9.803921569, 4.901960784, 2.450980392, 1.225490196, 0.612745098, 0.306372549, 0.153186275, 0.076593137, 0.038296569])

# Absorbâncias das novas amostras a serem analisadas
absorbancias_amostras = [0.0523, 0.1000, 0.2000]  # Exemplo de valores

# Área da folha em metros quadrados
area_folha_m2 = 0.0003585  # Exemplo de área, substitua pelo valor real

# Calcular os volumes de calda pulverizados para as novas amostras
volumes_calda_mL, volumes_calda_L_ha = calcular_volume_calda(absorbancias_amostras, absorbancias_calibracao, concentracoes_calibracao, area_folha_m2)

# Exibir os resultados
for i, (volume_mL, volume_L_ha) in enumerate(zip(volumes_calda_mL, volumes_calda_L_ha)):
    print(f"Volume de calda pulverizado para a amostra {i+1}: {volume_mL:.6f} mL ({volume_L_ha:.6f} L/ha)")
