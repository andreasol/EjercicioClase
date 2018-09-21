"""
    Ingrese la fecha
"""
from datetime import datetime

print(datetime.now())
today= datetime.now()
anio = int(input("Ingrese el anio de nacimiento \n"))
month_nac = int(input("Ingrese el mes de nacimiento \n"))
day_nac = int(input("Ingrese el dia de nacimiento \n"))

print(today, f"Anio: {today.year}-Mes: {today.month}-Dia: {today.day}")
print(type(today.day))

restaDia = today.day - day_nac
restaMes = today.month - month_nac
restaAnio = today.year - anio

if restaMes < 0:
    restaAnio -=1