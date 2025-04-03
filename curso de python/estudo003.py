temperatura=float(input("Digite uma temperatura para a água: "))
if temperatura >= 100:
    agua_ferve=True
    print(f"Se a água estiver acima dos 100 graus a água ferve? {agua_ferve}")
else:
    agua_ferve=False
    print(f"Se a água estiver abaixo dos 100 graus a água ferve? {agua_ferve}")
print(f"E se a água estiver abaixo de 0 grau ela congela.")