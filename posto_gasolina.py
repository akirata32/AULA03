litros= float(input("digite quantos litros vc encheu o tanque"))
combustivel=input("DIGITE QUAL FOI O COMBUSTIVEL, E para etanol, e G para gasolina")
gasolina= float (5.80)
etanol= float( 4.90)

if combustivel== "E" or combustivel== "e": valor=litros*etanol


elif combustivel== "G" or combustivel== "g": valor=litros*gasolina

print(f"voce encheu {litros} litros e gastou {valor}" )





