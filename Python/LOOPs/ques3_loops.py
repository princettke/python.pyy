# A spam comment is defined as a text containing following keywords:

# "Make a lot of money"
# "buy now"
# "subscribe this"
# "click this"
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
message = input("enter your message: ")
if(p1 in message)or ( p2 in message) or (p3 in message ):
  print("this is spam")
else:
  print("This is not scam")


#   Python mein in ek membership operator hai. Iska use check karne ke liye hota hai ki koi value kisi string, list, tuple, dictionary, set ke andar present hai ya nahi.

# Syntax:
# value in collection