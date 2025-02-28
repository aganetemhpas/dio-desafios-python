from datetime import datetime, timedelta

tipo_carro = 'm' # p, m, g

tempo_p = 30
tempo_m = 45
tempo_g = 60

data_atual = datetime.now()

if tipo_carro == 'p':
    data_estimada = data_atual + timedelta(minutes=tempo_p)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}.')
elif tipo_carro == 'm':
    data_estimada = data_atual + timedelta(minutes=tempo_m)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}.')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_g)
    print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}.')


# Tirando dias
data_estimada = data_atual - timedelta(minutes=tempo_p)
print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}.')