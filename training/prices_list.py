# if prices in ILS add 18% TAX
#     if prices in $ add 20% tax
#     the results in 2 lists
prices = ["25$","50$","48ILS","34$","25$","100ILS"]
prices_ils = []
prices_usd = []
for price in prices:
    if "ILS" in price:
        price.removesuffix("ILS")
#        price = int(price)
#        prices_ils.append(price)
    elif "$" in price:
        price.removesuffix("$")
#        price = int(price)
#        prices_usd.append(price)



