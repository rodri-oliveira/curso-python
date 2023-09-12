velocidade = 4
local_carro_km = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passou_radar = velocidade > RADAR_1
carro_passou_no_radar_1 = local_carro_km >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro_km <= (LOCAL_1 + RADAR_RANGE) and \
            velocidade_carro_passou_radar
carro_multado_radar_1 = carro_passou_no_radar_1 and velocidade_carro_passou_radar

if velocidade_carro_passou_radar:
    print('Voce passou da velocidade do radar: ')

if carro_multado_radar_1:
    print('Carro multado')
else:
    print('Voce não foi multado: ')
    # if velocidade > RADAR_1:
    #     print('Voce foi multado: ')
    # else:
    #     print('Voce não foi multado: ')

