agua= 1 # El agua se da en tazas
print("el agua es",agua)
harina= 1 # la harina se da en tazas
print("la harina es",harina)
sal= 1/16/3 # la sal se convierte de cdts a tazas, hay 3 cdts por cda y 16 cda por taza
print("la sal  es",sal)
aceite= 1/16 # la sal se convierte de cda a tazas

#comienza la preparacion
bol= agua + harina + sal 
budare = bol + aceite

#se imprime el resultado
print("La arepa final es",budare)

harina = str(input("Ingrese la cantidad de harina (en gramos): "))

agua = str(input("Ingrese la cantidad de agua (en mililitros): "))

sal = str(input("Ingrese la cantidad de sal (en gramos): "))

harina = float(harina)
agua = float(agua)
sal = float(sal)
masa_total = harina + agua + sal  

print("La cantidad total de masa para arepas es:", masa_total, "gramos.")
