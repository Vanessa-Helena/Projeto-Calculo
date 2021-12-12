# Pretende-se estender um cabo de uma usina de força `a margem de um rio de 900 m de largura até uma fábrica situada do outro lado do rio, 3000 m rio abaixo. O custo para estender um cabo pelo rio é de R$ 5, 00 o metro, enquanto que para estendê-lo por terra custa R$ 4, 00 o metro. Qual é o percurso mais econômico para o cabo?

# ALTURA = 900m (largura do rio)
# COMPRIMENTO = 3000 (altura do rio)
# CUSTORIO = 5,00 O METRO (estender no rio)
# CUSTOTERRA = 4,00 METRO (estender terra)

largura = float(input('Informe a largura do Rio: '));
comprimento = float(input('Informe o comprimento do Rio: '));
custoRio = float(input('Informe a largura do Rio: '));
custoTerra = float(input('Informe a largura do Rio: '));
dRio = float(input('Informe a largura do Rio: '));
custoOtimizado = 0;
custoTotal = 0;
x = None;


largura = input('')
    
    cout << "Informe a largura do rio: ";
    cin >> largura;

    cout << "Informe o comprimento do rio: ";
    cin >> comprimento;

    cout << "Informe o custo em Metros para estender o cabo pelo Rio: ";
    cin >> custoRio;

    cout << "Informe o custo em Metros para estender o cabo pela Terra: ";
    cin >> custoRio;


    dRio = sqrt(pow('x',2)+largura);

    custoOtimizado = ((custoTerra * -1) + (custoRio * 1/2) * (pow('x',2) + pow(largura,2)));

    return 0;
}
