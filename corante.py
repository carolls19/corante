import numpy as np
from sklearn.linear_model import LinearRegression

# Dados fornecidos
absorbancias = np.array([2.7931, 1.3943, 0.6945, 0.3601, 0.1738, 0.0882, 0.0467, 0.0286, 0.0294, 0.0033])
concentracoes = np.array([19.60784314, 9.803921569, 4.901960784, 2.450980392, 1.225490196, 0.612745098, 0.306372549, 0.153186275, 0.076593137, 0.038296569])

# Reshape dos dados para o modelo de regressão linear
X = absorbancias.reshape(-1, 1)
y = concentracoes

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X, y)

# Coeficientes da reta de calibração
coeficiente_angular = model.coef_[0]
intercepto = model.intercept_

coeficiente_angular, intercepto

# Absorbância medida da amostra
A = 0.2662

# Calcular a concentração da amostra usando a reta de calibração
concentracao_amostra = coeficiente_angular * A + intercepto
concentracao_amostra

# Volume da água usada para lavar a folha (em ml)
volume_agua_lavagem = 20

# Concentração do corante na solução mãe (em ppm)
concentracao_calda = 1000

# Calcular o volume de calda pulverizado na folha (em ml)
volume_calda_pulverizado = (concentracao_amostra * volume_agua_lavagem) / concentracao_calda
volume_calda_pulverizado

import numpy as np
from sklearn.linear_model import LinearRegression

# Dados fornecidos
absorbancias = np.array([2.7931, 1.3943, 0.6945, 0.3601, 0.1738, 0.0882, 0.0467, 0.0286, 0.0294, 0.0033])
concentracoes = np.array([19.60784314, 9.803921569, 4.901960784, 2.450980392, 1.225490196, 0.612745098, 0.306372549, 0.153186275, 0.076593137, 0.038296569])

# Reshape dos dados para o modelo de regressão linear
X = absorbancias.reshape(-1, 1)
y = concentracoes

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X, y)

# Coeficientes da reta de calibração
coeficiente_angular = model.coef_[0]
intercepto = model.intercept_

# Absorbância medida da amostra
A = 0.2662

# Calcular a concentração da amostra usando a reta de calibração
concentracao_amostra = coeficiente_angular * A + intercepto

# Volume da água usada para lavar a folha (em ml)
volume_agua_lavagem = 20

# Concentração do corante na solução mãe (em ppm)
concentracao_calda = 1000

# Calcular o volume de calda pulverizado na folha (em ml)
volume_calda_pulverizado = (concentracao_amostra * volume_agua_lavagem) / concentracao_calda
volume_calda_pulverizado

import numpy as np
from sklearn.linear_model import LinearRegression

# Dados fornecidos
absorbancias = np.array([2.7931, 1.3943, 0.6945, 0.3601, 0.1738, 0.0882, 0.0467, 0.0286, 0.0294, 0.0033])
concentracoes = np.array([19.60784314, 9.803921569, 4.901960784, 2.450980392, 1.225490196, 0.612745098, 0.306372549, 0.153186275, 0.076593137, 0.038296569])

# Reshape dos dados para o modelo de regressão linear
X = absorbancias.reshape(-1, 1)
y = concentracoes

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X, y)

# Coeficientes da reta de calibração
coeficiente_angular = model.coef_[0]
intercepto = model.intercept_

# Absorbância medida da amostra
A = 0.2662

# Calcular a concentração da amostra usando a reta de calibração
concentracao_amostra = coeficiente_angular * A + intercepto

# Volume da água usada para lavar a folha (em ml)
volume_agua_lavagem = 20

# Concentração do corante na solução mãe (em ppm)
concentracao_calda = 1000

# Calcular o volume de calda pulverizado na folha (em ml)
volume_calda_pulverizado = (concentracao_amostra * volume_agua_lavagem) / concentracao_calda
volume_calda_pulverizado

print(volume_calda_pulverizado)