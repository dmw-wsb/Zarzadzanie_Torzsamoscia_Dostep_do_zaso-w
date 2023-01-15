
        characters_number = int(user_input)

        if characters_number < 8:

            print("Twoje haslo powinno miec przynajmniej 8 znakow.")

            user_input = input("Wprowadz ponownie długość hasła: ")

        else:

            break

    except:

        print("Prosze podać tylko cyfry.")

        user_input = input("Z ilu znaków ma składać sie twoje hasło? ")

# mieszamy listy
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# obliczmy 20% & 30% munerów ze znaków tak aby hasło zawierało znaki specjalne i numery
part1 = round(characters_number * (30 / 100))
part2 = round(characters_number * (20 / 100))

# tworzenie hasła (60% liter and 40% cyfr & znaków specjalnych)
result = []

for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

# mieszamy wyniki
random.shuffle(result)

# wynik
password = "".join(result)
print("Twoje hasło to: ", password)
