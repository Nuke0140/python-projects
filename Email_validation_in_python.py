"""
     Email validation
        in python
(using String Function)
"""

email=input("Enter your Email : ") # g@g.in  nilshinde74@gamil.com
k,j,d = 0
if len(email)>= 6: # email charater should greater than 6
     if email[0].isalpha(): # your 1st character in email should be alpha
         if ("@" in email) and (email.count("@")==1):# cheacking @ mail sign in email sure it only one time

             if(email[-4]==".")^(email[-3]=="."):# cheacking . in 3rd and 4th position
                  for i in email:
                      if i == i.isspace():# cheaking space in string
                          k=1
                      elif i.isalpha():
                          if i==i.upper(): # cheakin uppercase in string 
                              j=1
                      elif i.isdigit():
                          continue
                      elif i =="_" or i =="." or i =="@":
                          continue
                      else:
                          d=1
                  if k == 1 or j == 1 or d ==1 :
                      print("Wrong Email 5")

             else:
                 print("Wrong email 4")
         else:
             print("Wrong email 3")


     else:
         print("wrong Email 2 ")



else:
     print(" Wrong Email 1")
