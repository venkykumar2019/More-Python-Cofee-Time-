# hello Let's build a robot barista!!
print('Welcome to Ava coffee!!!!!!!!!!!!!')
name = input("What is your name?\n\n\n")

specials = ("flat white,americano,expresso,latte")

if name =="Ben":
  print("you are not welcome here evil ben!!Get Out!!")
  exit("")

else:
  print("hello " + name + " thank you for coming in today, our menu today is " + specials)



order =input("what is your order for today?\n\n\n")

print("Oh that is a great choice, " + name)

many = input("How many do you want?\n")
sum = 5 * int(many)
print("Ok, I will get your " + order + " very soon, meanwhile enjoy your time here at Ava Coffee")
  
print ("here is your " + order + " hope you enjoy it ")

print ("hello " + name + " here is the bill for your " + order +  " it is $" + str(sum) + " pounds please")