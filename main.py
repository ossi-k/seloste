def tee_seloste(data):
    #alustetaan muuttujia
    tulostus = ""
    toimialat_sarakkeille = {}

    #luetaan data
    data = open(data, encoding="latin-1")
    lines = data.readlines()
    y = 0
    while(y < len(lines)):
        lines[y] = lines[y].strip()
        if not lines[y] or lines[y] == ";":
            lines.remove(lines[y])
            y = y - 1
        y += 1

    # päätellään muuttuja ja poistetaan otsikkorivi
    eka_rivi = lines[0].split(" ")
    muuttuja = eka_rivi[3][:11]
    lines.pop(0)

    #muodostetaan seloste
    rivi = 0
    for line in lines:
        sarakkeet = line.split(";")

        if rivi == 0:
            for i in range(1, len(sarakkeet)):
                sisalto = sarakkeet[i].replace('"', '').split(" ")
                toimiala = ""
                #for y in range(len(sarakkeet[i])):
                #    if sisalto[y] == " ":
                #       break
                for sana in sisalto:
                    if sana.lower() == muuttuja.lower():
                        break
                    toimiala += sana + " "
                toimialat_sarakkeille[i] = toimiala.lstrip()

        #sarakkeiden lukumäärän päättely
        sarakkeet_lkm = len(sarakkeet)

        #muutetaan pilkut pisteiksi, jotta muuntaminen floatiksi onnistuu
        for i in range(1, sarakkeet_lkm):
            sarakkeet[i] = sarakkeet[i].replace(",", ".")

        if rivi > 0:
            #päätellään, onko kasvua vai laskua ja lisätään selosteeseen oikea tulostus
            for i in range(1, sarakkeet_lkm):
                if float(sarakkeet[i]) > 0:
                    tulostus += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " kasvoi " + str(sarakkeet[0]) + " neljänneksellä " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                elif float(sarakkeet[i]) < 0:
                    tulostus += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " supistui " + str(sarakkeet[0]) + " neljänneksellä " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                else:
                    tulostus += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " ei kasvanut eikä supistunut " + str(sarakkeet[0]) + " neljänneksellä." + "\n"
        rivi += 1

    with open("seloste.txt", "x") as f:
        f.write(tulostus)

    return tulostus


print(tee_seloste("C:\\Users\\ossik\\Downloads\\004_111y_2020m01.csv"))