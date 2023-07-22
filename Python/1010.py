peca1  = input().split(" ")
peca2  = input().split(" ")
id_p1, qtd_p1, valor_p1 = peca1
id_p2, qtd_p2, valor_p2 = peca2
total = (int(qtd_p1) * float(valor_p1)) + (int(qtd_p2) * float(valor_p2))

print(f'VALOR A PAGAR: R$ {total:.2f}')