import json

with open('faturamento/faturamento.json', 'r') as file:
    faturamento_diario = json.load(file)["faturamento_diario"]

faturamento_valido = [valor for valor in faturamento_diario if valor > 0]

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_faturamento)

print(f"O menor faturamento registrado foi: R$ {menor_faturamento:.2f}")
print(f"O maior faturamento registrado foi: R$ {maior_faturamento:.2f}")
print(f"Em {dias_acima_da_media} dias, o faturamento ficou maior que a média mensal.")
