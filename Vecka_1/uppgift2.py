biljettpris = 100  # biljettpris
konto = 200  # pengar på fickan
print("Det blir " + str(konto - biljettpris) + " kronor över.")
z = 200 - 100 / 2
print("Hälften är: " + str(z))

# Kommentar: z är fristående från biljettpris och konto variabeln, dvs skulle biljettpris och konto ändras
# så skulle det inte påverka rad 4 och 5. Kanske är by design, kanske inte.
# z skulle kunna heta summa eller svar, då den återigen är frikopplad från de övriga variablerna.