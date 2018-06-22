myfavoriteicecream = raw_input("What is your favorite ice cream?")
if myfavoriteicecream == "Chocolate" :
    print("That is my favorite too!")
    
elif myfavoriteicecream in["vanilla", "blackberry", "watermelon sherbert"]:            
    print("I like that flavor too :)") 

else:
    print("yuck, you have horrible taste")
    
myname = raw_input("What is your name?")
myinfo = ["Angela", "Fred", "Trudy"]
for name in myinfo:
     if myname == name:
      print("True")
     else:
         print("False")
         
x = int(raw_input("please imput a whole number:"))
if x > 0:
    print(x)
else:
    print(y)