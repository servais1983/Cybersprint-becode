milk_price = 2*0.45
cider_price = 3*3.85
flour_price = 0.90
butter_price = 0.77
nutella_price = 1.87
message = ""
orderPrice = round(milk_price+cider_price+flour_price+butter_price+nutella_price, 2)
print(orderPrice)
allowanceMoney = 20
calcul = round(allowanceMoney - orderPrice, 2)
print(orderPrice)
if calcul > 0:
    message = "you have spent {}, you have left {}".format(orderPrice, allowanceMoney)
elif calcul == 0:
    message = "you are broke"
else:
    amountMissing = (calcul)
    message = "Sorry you're missing {} euro".format(amountMissing)
    
print(message)