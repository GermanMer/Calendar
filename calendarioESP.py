from calendar import *
import locale
locale.setlocale(locale.LC_ALL, 'es_ES.utf-8')
year = int(input("Ingrese el año:"))
print(calendar(year))
