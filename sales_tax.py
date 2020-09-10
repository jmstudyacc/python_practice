import time

britainTax = 20
franceTax = 18
germanyTax = 10
italyTax = 6
spainTax = 2

for i in range(0,5):
  countries = "\nBritain\nFrance\nGermany\nItaly\nSpain"
  print(countries)

  countryChoice = input("\nType the name of a country from the list above to view the sales tax: \n")
  countryChoice = countryChoice.title()
  try:
    if countryChoice == "Britain":
        print(f"The sales tax in Britain is {britainTax}%.")
    elif countryChoice == "France":
        print(f"The sales tax in {countryChoice} is {franceTax}%.")
    elif countryChoice == "Germany":
        print(f"The sales tax in {countryChoice} is {germanyTax}%.")
    elif countryChoice == "Italy":
        print(f"The sales tax in {countryChoice} is {italyTax}%.")
    elif countryChoice == "Spain":
        print(f"The sales tax in {countryChoice} is {spainTax}%.")
    else:
        raise NameError(countryChoice)
    
  except NameError:
      print(f"{countryChoice} is not within the list, please try again")
      
  time.sleep(0.5)
