# Naam: Giorgos Giannoglou, Opdracht: Pizza Calculator
SmallPizza = int (input ("Hoeveel small pizzas wil je hebben? "))
MediumPizza = int (input ("Hoeveel medium pizzas wil je hebben? "))
LargePizza = int (input ("Hoeveel large pizzas wil je hebben? "))

SmallPizzaPrijs = 8
MediumPizzaPrijs = 10
LargePizzaPrijs = 13

SmallPizzaBedrag = SmallPizza * SmallPizzaPrijs
MediumPizzaBedrag = MediumPizza * MediumPizzaPrijs
LargePizzaBedrag = LargePizza * LargePizzaPrijs

TotaalBedrag = SmallPizza * SmallPizzaPrijs + MediumPizza * MediumPizzaPrijs + LargePizza * LargePizzaPrijs

print ("----------------------------------------------------")
print ("| Small pizza prijs  : " + str(SmallPizzaBedrag) + "€")
print ("| Medium pizza prijs : " + str(MediumPizzaBedrag) + "€")
print ("| Large pizza prijs  : " + str(LargePizzaBedrag) + "€")
print ("| Totaal prijs       : " + str(TotaalBedrag) + "€")
print ("----------------------------------------------------")