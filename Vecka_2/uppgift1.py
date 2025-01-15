# GRUNDKOD
# is_member = False
# level1 = 100
# level2 = 300
# discount = 0
#
# price = input("Välkommen, köp något dyrt:")
# price = float(price)
# if price > level1:
#   print("Grattis Du har avancerat till nivå 1 och får 10% rabatt!")
#   discount = discount + 10
# if price >= level2:
#   print(("Grattis! Du har avancvcerat till nivå2 och får 25 procent rabatt!"))
#   discount = discount + 25
#
# final_price = price * (100 - discount) / 100
# print("Efter rabatter blir priset..." + final_price)


is_member = False  # Denna rad säger att man inte är medlem alls, vilket kanske gör all kod nedan oviktig.
level1 = 100
level2 = 300
discount = 0

price = input("Välkommen, köp något dyrt:")
price = float(price)
if price > level1:
    print("Grattis Du har avancerat till nivå 1 och får 10% rabatt!")
    discount = discount + 10
if price >= level2:
    print(("Grattis! Du har avancvcerat till nivå2 och får 25 procent rabatt!"))
    discount = discount + 25
    # Anger vi ett pris på tex 305 så får vi först 10% discount för level1, sedan även discount 25. Totalt 35% rabatt.
final_price = price * (100 - discount) / 100
print("Efter rabatter blir priset..." + str(final_price))  # final_price är float, behöver convert to string
