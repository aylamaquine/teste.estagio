import json


faturamento_json = '''
{
    "faturamento_diario": [ 1500, 0, 0, 2586, 0, 900, 0, 2855, 1100, 0, 0]
}
'''

dados = json.loads(faturamento_json)
faturamento_diario = dados['faturamento_diario']

faturamento_valido = [f for f in faturamento_diario if f > 0]
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)
media_faturamento = sum(faturamento_valido) / len(faturamento_valido)
dias_acima_da_media = len([f for f in faturamento_valido if f > media_faturamento])

print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Média de faturamento: R$ {media_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
