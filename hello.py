class hotelfarecal:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=1001):

        print ("\nWelcome TO Abstract Hotel\n")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("Your room no.:",self.rno,"\n")
        
    def roomrent(self):#sel1353

        print ("We have the following rooms for you:-")

        print ("1.  type A---->$ 90 PN\-")

        print ("2.  type B---->$ 80 PN\-")

        print ("3.  type C---->$ 70 PN\-")

        print ("4.  type D---->$ 60 PN\-")

        x=int(input("Enter Your Choice Please->"))

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("you have opted room type A")

            self.s=90*n

        elif (x==2):

            print ("you have opted room type B")

            self.s=80*n

        elif (x==3):

            print ("you have opted room type C")

            self.s=70*n

        elif (x==4):
            print ("you have opted room type D")

            self.s=60*n

        else:

            print ("please choose a room")

        print ("your room rent is =",self.s,"\n")

    def restaurentbill(self):

        print("RESTAURANT MENU###")

        print("1.water----->$5","2.tea----->$4","3.breakfast combo--->$50","4.lunch---->$ 80","5.dinner--->$80","6.Exit")


        while (1):

            c=int(input("Enter your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+5*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+4*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+50*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+80*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+80*d

            elif (c==6):
                break;
            else:
                print("Invalid option")

        print ("Total food Cost=Rs",self.r,"\n")

    def	laundrybill(self):
        print ("LAUNDRY MENU##")

        print ("1.Shorts----->$3","2.Trousers----->$4","3.Shirt--->$5","4.Jeans---->$6","5.Girlsuit--->$8","6.Exit")

        while (1):
            #brought to you by code-projects.org

            e=int(input("Enter your choice:"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+3*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+4*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+5*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+6*f

            elif (e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+8*f
            elif (e==6):
                break;
            else:

                print ("Invalid option")


        print ("Total Laundary Cost=Rs",self.t,"\n")

    def gamebill(self):
        print ("GAME MENU##")

        print ("1.Table tennis----->$60","2.Bowling----->$80","3.Snooker--->$70","4.Video games---->$90","5.Pool--->$50==6","6.Exit")



        while (1):

            
            g=int(input("Enter your choice:"))


            if (g==1):
                h=int(input("No. of hours:"))
                self.p=self.p+60*h

            elif (g==2):
                h=int(input("No. of hours:"))
                self.p=self.p+80*h

            elif (g==3):
                h=int(input("No. of hours:"))
                self.p=self.p+70*h

            elif (g==4):
                h=int(input("No. of hours:"))
                self.p=self.p+90*h

            elif (g==5):
                h=int(input("No. of hours:"))
                self.p=self.p+50*h
            elif (g==6):
                break;

            else:

                print ("Invalid option")



        print ("Total Game Bill=Rs",self.p,"\n")

    def display(self):
        print ("HOTEL BILL###")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)
        print ("Your laundary bill is:",self.t)
        print ("Your Game bill is:",self.p)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.rt+self.a,"\n")
        self.rno+=1

            

        

        

def main():

    a=hotelfarecal()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate rommrent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate gamebill")

        print("6.Show total cost")

        print("7.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurentbill()

        if (b==4):

            a.laundrybill()

        if (b==5):

            a.gamebill()

        if (b==6):

            a.display()

        if (b==7):

            quit()



main()

