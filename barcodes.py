from turtle import *
a = 0
def barcodes(barcode):
    
    # try:
        skk = Turtle()
        #barcode part       
        barcode = barcode.replace("-","")
        #grabbing the extra digit
        extraDigit = (10 - (sum([int(d) for d in str(barcode)])%10))
        barcode = int(str(barcode) + str(extraDigit))
        print(barcode,"Before loop")
        #setting up turtle
        wn = Screen()
        wn.bgcolor("white")
        wn.title("Turtle")
        
        skk.hideturtle()
        skk.pensize(10)
        skk.up()
        skk.setpos(-400,-350)
        skk.right(270) 
        def long():
            x = skk.xcor()
            y = skk.ycor()
            skk.up()
            skk.setpos(x+20,-350)
            skk.down()
            skk.forward(100)
        def short():
            x = skk.xcor()
            y = skk.ycor()
            skk.up()
            skk.setpos(x+20,-350)
            skk.down()
            skk.forward(50)
        long()
        for i in str(barcode):
            print(barcode)
            print(i)
            match i:
                case "0":
                    long()
                    long()
                    short()
                    short()
                    short()
                case "1":
                    short()
                    short()
                    short()
                    long()
                    long()
                case "2":
                    short()
                    short()
                    long()
                    short()
                    long()
                case "3":
                    short()
                    short()
                    long()
                    long()
                    short()
                case "4":
                    short()
                    long()
                    short()
                    short()
                    long()
                case "5":
                    short()
                    long()
                    short()
                    long()
                    short()
                case "6":
                    short()
                    long()
                    long()
                    short()
                    short()
                case "7":
                    long()
                    short()
                    short()
                    short()
                    long()
                case "8":
                    long()
                    short()
                    short()
                    long()
                    short()
                case "9":
                    long()
                    short()
                    long()
                    short()
                    short()
                case _:
                    print("hi")
        long()
        print("Click the window to exit")
        exitonclick()


    # except:
    #     print("Invalid input")