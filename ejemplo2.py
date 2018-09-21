
lista = [
    "www.espol.edu.ec", "www.google.com", "www.sri.gob.ec", "www.fiec.espol.edu.ec", "www.uess.edu.ec",
    "www.FIEC.espol.edu.ec", "www.fict.espol.edu.ec", "www.fcnm.Espol.edu.ec", "www.ucsg.edu.ec",
    "www.Stanford.edu", "www.harvard.edu", "www.stanford.edu", "www.UCSG.edu.ec", "www.google.com.ec",
    "www.facebook.com", "www.opensource.org", "www.educacionbc.edu.mx", "www.elnoticiero.com.ec"
]
lista_v= [ ]
for a in lista:
    if 'edu.ec' in a:
        c = a.split(".")
        c = c[1].upper()
        if c not in lista_v:
            lista_v.append(c)

print(lista_v
      )