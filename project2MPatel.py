import hashlib
from turtle import *
import timeit
total_time = 0
def p1(userInput,userInput2=None):
    def get_num_of_characters(str):
        return len(str)
    def output_without_whitespace(s):
        msg = s.replace(" ","")
        return msg
    def get_acronym(st):
        tpl = st.split(" ")
        msg = ""
        for i in tpl:
            msg+=i[0]
        return msg
    def get_safe(sg):
        return str(hashlib.sha256(sg.encode('utf8')).hexdigest())
    if userInput2 == None and userInput != None:
        print("The number of characters in the string is",str(get_num_of_characters(userInput)) 
          + "\nThe output without whitespace is",output_without_whitespace(userInput))
    elif userInput2 != None and userInput == None:
        print("The acronym is",get_acronym(userInput2) 
          + "\nThe sha256 output is",get_safe(userInput2))

'''
Enter a sentence or phrase: The only thing we have to fear is fear itself.
you entered: The only thing we have to fear is fear itself.
The number of characters in the string is 46
The output without whitespace is Theonlythingwehavetofearisfearitself.
Enter a phrase to generate anacronym: random access memory
The acronym is ram
The sha256 output is ba66fc77ac168995d4a461f694418842c81be9664dcf142f509d3a728e74a66b
'''
def generatePrimes(n,start_val=0):
    count = 0
    #lst will be manipulated at the end but will hold the primes 
    lst = list()
    #temp will first be filled with all True values up to n+1, later on some will be turned to false which will tell which nums are prime
    temp = [True] * (1340000)
    #loop through n starting at the lowest prime number which is 2, we need it to start at 2 because temp is true at first 
    for i in range(2,1340000):
        #when temp is true it adds it to the list 
        if temp[i]:
            lst.append(i)
            count+=1
            #This loops from the current number to n+1 with a step of the current number
            #This removes any multiples of the number which greatly saves time and ram 
            for j in range(i,1340000,i):
                temp[j] = False
        
        
        if count == n:
            break
    final = [x for x in lst if x>start_val]
    global total_time
    
    yield final
def barcodes(barcode):
    try:

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
        skk = Turtle()
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


    except:
        print("Invalid input")
# barcodes("55555-1237")
def main():
    while True:
        choice = input("Which program do you want to run:\nA:Part 1\nB:Prime Number Generator\nC:Barcodes\nD:quit\n")
        match choice.upper():
            case "A":
                s = input("Enter a sentence or phrase: ")
                print("you entered:",s)
                p1(userInput=s,userInput2=None)
                str = input("Enter a phrase to generate anacronym: ")
                p1(userInput=None,userInput2=str)
            case "B":
                start = 0
                while True:
                    userI = input("A:Enter the number you want primes to: \nB:quit\n")
                    match userI.upper():
                        case "A":
                            # FIX THIS, NUMBER OR PRIMES NOT PRIMES TO A NUMBER
                            ui = input("To what number do you want to go to?: ")
                            if ui.isnumeric():
                                startTime = timeit.default_timer()
                                print(next(generatePrimes(int(ui),start)))
                                endTime = timeit.default_timer()
                                total_time = endTime - startTime
                                print(total_time)
                                start = int(ui)
                        case "B":
                            break
                        case _:
                            print("Enter A or B")
            case "C":
                g = input("Enter the barcode, you can use - to seperate digits\n")
                barcodes(g)
                continue
            case "D":
                break
            case _:
                print("Enter a proper value")
    #part 1
    #primes
    #barcodes

    
main()