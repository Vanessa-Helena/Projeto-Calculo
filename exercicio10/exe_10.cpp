/*Pretende-se estender um cabo de uma usina de força `a margem de um rio de 900 m de largura até uma fábrica situada do outro lado do rio, 3000 m rio abaixo. O custo para estender um cabo pelo rio é de R$ 5, 00 o metro, enquanto que para estendê-lo por terra custa R$ 4, 00 o metro. Qual é o percurso mais econômico para o cabo?

ALTURA = 900m (largura do rio)
COMPRIMENTO = 3000 (altura do rio)
CUSTORIO = 5,00 O METRO (estender no rio)
CUSTOTERRA = 4,00 METRO (estender terra)
*/

#include <iostream>;
#include <numeric>;
#include <stdio.h>;
#include <stdlib.h>;
#include <cmath>;
#include <math.h>;

double largura, comprimento, custoRio, custoTerra, dRio;

using namespace std;

int main(int argc, char const *argv[])
{
    
    cout << "Informe a largura do rio: ";
    cin >> largura;

    cout << "Informe o comprimento do rio: ";
    cin >> comprimento;

    cout << "Informe o custo em Metros para estender o cabo pelo Rio: ";
    cin >> custoRio;

    cout << "Informe o custo em Metros para estender o cabo pela Terra: ";
    cin >> custoRio;


    dRio = sqrt(pow('x',2)+largura);


    return 0;
}
