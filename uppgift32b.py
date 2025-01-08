pris = 2000

while True:
    try:
        rabatt_i_procent = int(input("Ange rabattprocent:"))
        if rabatt_i_procent >= 0 and rabatt_i_procent <= 100:
            break
    except ValueError:
        print("Du måste ange ett tal mellan 0 och 100 (utan procenttecken)")

rabatterat_pris = pris * (100 - rabatt_i_procent) / 100
print(f"Med en rabatt på {rabatt_i_procent}% så kostar jackan {rabatterat_pris:.2f} kr.")
