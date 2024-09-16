def calcular_imposto(renda):
    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return (renda - 2000) * 0.10
    else:
        imposto_parcial = (5000 - 2000) * 0.10
        imposto_adicional = (renda - 5000) * 0.20
        return imposto_parcial + imposto_adicional

def main():
    renda = float(input("Digite a sua renda: R$ "))
    if renda < 0:
        print("A renda não pode ser negativa.")
        return
    
    imposto = calcular_imposto(renda)
    print(f"Imposto de renda devido: R$ {imposto:.2f}")


main()
