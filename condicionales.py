dui=False
poli=False
carne=False
tipo=input("Si es médico presione 1, de lo contrario presione 2: ")
if tipo=="1":
    med=True
else:
    med=False
respuesta=input("¿Ha presentado DUI? (si/no): ")
if respuesta.lower()=="si":
    dui=True
respuesta=input("¿Ha presentado antecedentes penales? (si/no): ")
if respuesta.lower()=="si":
    poli=True
if med==True:
    respuesta=input("¿Ha presentado carnet de certificación médica? (si/no): ")
    if respuesta.lower()=="si":
        carne=True
if med:
        print(f"""El estado de sus documentos es:
DUI: {dui}
Antecedentes penales: {poli}
Carnet médico: {carne}""")
        if dui==False and poli==False and carne==False:
            print("Estado global: Ningún documento adjuntado")
        elif dui==True and poli==True and carne==True:
            print("Estado global: Completo")
        else:
            print("Estado global: Incompleto")
elif med==False:
        print(f"""El estado de sus documentos es:
DUI: {dui}
Antecedentes penales: {poli}""")
        if dui==False and poli==False:
            print("Estado global: Ningún documento adjuntado")
        elif dui==True and poli==True:
            print("Estado global: Completo")
        else:
            print("Estado global: Incompleto")