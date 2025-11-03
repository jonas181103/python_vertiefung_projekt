# Passwort-Generator

# 1. Passwort-Generierung mit verschiedenen Auswahlmöglichkeiten (Caps, Zahlen, Sonderzeichen)

import random
import string

password_name = input(
    "Unter welchem Namen soll das Passwort gespeichert werden? \n")
password_information = list(map(int, input(
    "Welche Anforderungen hat dein Passwort: \n 1. Nur Großbuchstaben \n 2. Sonderzeichen \n Es werden nur Zahlen als Eingabe akzeptiert \n ")))
password_length = int(
    input("Wieviele Zeichen lang soll dein Passwort sein? \n"))

password_requirements = [password_name, password_length, password_information]
print(password_requirements)

if password_information[0] == True:
    grossbuchstaben = True

# def password_generator(
#        leange = password_length;
#        grossbuchstaben =


# 2. Speicherung des Passwortes in einer Datei
# 3. Anzeigen der Passwortstärke, vom eingefügten Passwort
