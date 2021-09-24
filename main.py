'''
import re

pattern = "[A-Z]{6}[0-9]{2}[ABCDEHLMPRST][0-9]{2}[A-Z][0-9]{3}[A-Z]"
'''
surname = ""
name = ""
birth_day = 0
birth_month = 0
birth_year = 0
is_male = True
city = ""

def find_letter(start_string: str, index: int) -> str:
    temp_index = 0
    letter = "";
    work_string = start_string.strip().upper()
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    for letter in work_string:
        if letter in consonants:
            temp_index += 1
            if temp_index == index:
                return letter
    for letter in work_string:
        if letter in vowels:
            temp_index += 1
            if temp_index == index:
                return letter
    return "X"

def surname_triplet(surname: str) -> str:
    return find_letter(surname, 1) + find_letter(surname, 2) + find_letter(surname, 3)

def name_triplet(name: str) -> str:
    if len(name) < 3:
        return find_letter(name, 1) + find_letter(name, 2) + find_letter(name, 3)
    else:
        return find_letter(name, 1) + find_letter(name, 3) + find_letter(name, 4)

def find_year(start_year: int) -> str:
    # Inserito l'anno a 4 cifre
    if start_year > 1000:
        return str(start_year)[2:]
    # Inserito l'anno a 2 cifre
    else:
        return str(start_year)

def find_month(start_month: int) -> str:
    month_codes = "ABCDEHLMPRST"
    return month_codes[start_month - 1]

def find_day(start_day: int, is_male: bool) -> str:
    return str(start_day) if is_male else str(start_day + 40)

def local_code(city: str) -> str:
    codes_dict = {}
    for line in open("comuni.txt", "r").readlines():
        pair = line.split("\t")
        codes_dict[pair[0]] = pair[1]
    try:
        return codes_dict[city.upper()][:-1]
    except Exception as e:
        print(f"An error occourred: {e}")
        return "NULL"

def control_character(fiscal_string: str) -> str:
    even_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12,
                    "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
                    "Y": 24, "Z": 25, "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    odd_dict = {"A": 1, "B": 0, "C": 5, "D": 7, "E": 9, "F": 13, "G": 15, "H": 17, "I": 19, "J": 21, "K": 2, "L": 4, "M": 18,
                    "N": 20, "O": 11, "P": 3, "Q": 6, "R": 8, "S": 12, "T": 14, "U": 16, "V": 10, "W": 22, "X": 25,
                    "Y": 24, "Z": 23, "0": 1, "1": 0, "2": 5, "3": 7, "4": 9, "5": 13, "6": 15, "7": 17, "8": 19, "9": 21}
    sum = 0
    for i in range(15):
        if (i + 1) % 2 == 0:
            sum += even_dict[fiscal_string[i]]
        else:
            sum += odd_dict[fiscal_string[i]]
    return chr(65 + (sum % 26))

if __name__ == "__main__":
    surname = input("Inserisci il cognome: ")
    name = input("Inserisci il nome: ")
    birth_day = int(input("Inserisci il giorno di nascita (1-31): "))
    birth_month = int(input("Inserisci il mese di nascita (1-12): "))
    birth_year = int(input("Inserisci l'anno di nascita (1900-ora): "))
    is_male = bool(input("Sei maschio (1) o femmina (0)? (Se sei non binario, rispondi in base a cosa avevi in mezzo alle gambe quando sei nato/a): "))
    city = input("Comune di nascita (si prega di mettere gli spazi laddove necessario es. Santeramo in Colle): ")
    fiscal_string = surname_triplet(surname) + name_triplet(name) + find_year(birth_year) + find_month(birth_month) + find_day(birth_day, is_male) + local_code(city)
    print(f"{fiscal_string}{control_character(fiscal_string)}")

