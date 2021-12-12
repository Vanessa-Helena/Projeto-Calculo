# Pretende-se estender um cabo de uma usina de força `a margem de um rio de 900 m de largura até uma fábrica situada do outro lado do rio, 3000 m rio abaixo. O custo para estender um cabo pelo rio é de R$ 5, 00 o metro, enquanto que para estendê-lo por terra custa R$ 4, 00 o metro. Qual é o percurso mais econômico para o cabo?

# ALTURA = 900m (largura do rio)
# COMPRIMENTO = 3000 (altura do rio)
# CUSTORIO = 5,00 O METRO (estender no rio)
# CUSTOTERRA = 4,00 METRO (estender terra)

from sympy import *
import numpy as np

custoOtimizado = 0;
custoTotal = 0;
x = Symbol('x');

largura = float(input('Informe a largura do Rio: '));
comprimento = float(input('Informe o comprimento do Rio: '));
custoRio = float(input('Informe o custo em Metros para estender o cabo pelo Rio: '));
custoTerra = float(input('Informe a largura do Rio: '));
dRio = float(input('Informe o custo em Metros para estender o cabo pela Terra: '));

