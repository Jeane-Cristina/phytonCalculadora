def calcularTotalComDesconto(totalCompra):
    desconto = 0
    if totalCompra > 100:
        desconto = 0.10
    elif totalCompra > 50:
        desconto = 0.05
    
    valorDesconto = totalCompra * desconto
    totalFinal = totalCompra - valorDesconto
    
    return valorDesconto, totalFinal

def main():
    totalCompra = 0
    while True:
        valorItem = input("Digite o valor do item (ou 'fim' para encerrar): R$ ")
        if valorItem.lower() == 'fim':
            break
        valorItem = float(valorItem)
        if valorItem < 0:
            print("O valor do item não pode ser negativo. Tente novamente.")
        else:
            totalCompra += valorItem
    
    if totalCompra == 0:
        print("Nenhum item foi adicionado.")
        return
    
    valorDesconto, totalFinal = calcularTotalComDesconto(totalCompra)
    
    print(f"Valor total da compra: R$ {totalCompra:.2f}")
    print(f"Desconto aplicado: R$ {valorDesconto:.2f}")
    print(f"Valor final após desconto: R$ {totalFinal:.2f}")

main()
