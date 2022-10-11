from part1 import p1
from barcodes import barcodes
from barcodes import a
from primes import generatePrimes
import timeit
from os import pipe
from turtle import *


def main():
    print()
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
                    userI = input("A:Enter the number of primes you want: \nB:quit\n")
                    match userI.upper():
                        case "A":
                            # FIX THIS, NUMBER OR PRIMES NOT PRIMES TO A NUMBER
                            ui = input("To what number do you want to go to?: ")
                            if ui.isnumeric():
                                startTime = timeit.default_timer()
                                w = (next(generatePrimes(int(ui),start)))
                                print(w)
                                endTime = timeit.default_timer()
                                total_time = endTime - startTime
                                print(total_time)
                                # print(w[-1])
                                start = w[-1]
                        case "B":
                            break
                        case _:
                            print("Enter A or B")
            case "C":
                g = input("Enter the barcode, you can use - to seperate digits\n")
                barcodes(g)
            case "D":
                
                break
            case _:
                print("Enter a proper value")
if __name__ == '__main__':
     main()