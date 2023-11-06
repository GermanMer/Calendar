from calendar import *
import locale

idioma = input("Para idioma español, escriba español. For english, write english: ")

if idioma.lower() == "español":
    locale.setlocale(locale.LC_ALL, 'es_ES.utf-8')
    year = int(input("Ingrese el año:"))
    print(calendar(year))

elif idioma.lower() == "english":
    year = int(input("Enter year:"))
    print(calendar(year))

else:
    print("Opción de idioma no válida. Se establecerá el idioma en español por defecto.\nInvalid language option. The language will be set to Spanish by default.")
    locale.setlocale(locale.LC_ALL, 'es_ES.utf-8')
    year = int(input("Ingrese el año:"))
    print(calendar(year))
