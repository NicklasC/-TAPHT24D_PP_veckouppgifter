avstånd_i_km=470
avstånd_i_meter = avstånd_i_km * 1000

#hastighet = int(input("Ange hastighet i km/h:"))
hastighet = 60
hastighet_meter_per_sekund = hastighet / 3.6

tid_i_sekunder = avstånd_i_meter / hastighet_meter_per_sekund

print(f"Det tar {tid_i_sekunder} sekunder att köra")

# Uppgift 41b
print(f"Det tar {tid_i_sekunder/60} minuter att köra")

# Uppgift 41C
# Orkar ej ;)

