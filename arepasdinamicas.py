harina = str(input("Ingrese la cantidad de harina (en gramos): "))

agua = str(input("Ingrese la cantidad de agua (en mililitros): "))

sal = str(input("Ingrese la cantidad de sal (en gramos): "))

harina = float(harina)
agua = float(agua)
sal = float(sal)

masa_total = harina + agua + sal

print("La cantidad total de masa para arepas es:", masa_total, "gramos.")
