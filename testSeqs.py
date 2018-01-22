from CurveADT import CurveT
from SeqADT import *
from time import sleep


def main():
    newCurve = CurveT()

    #filename = raw_input("What is the name of the file?: ")
    filename = "linear.txt"
    newCurve.CurveT(filename)
    #xVal = input("What value of x would you like to find the y-value for?: ")
    xVal = newCurve.curveX.

    if (newCurve.degree == 1):
        linTest = newCurve.linVal(xVal)
        print("linval: %f" % linTest)
    elif (newCurve.degree == 2):
        polyTest = newCurve.quadVal(xVal)
        print("polyval: %f" % polyTest)

    yVal = newCurve.npolyval(xVal)

    print("The y value of %f is %f" % (xVal, yVal))


def test():
    print("Testing all functions...")

    testSeq = SeqT()
    testSeq.add(0, 0)
    testSeq.add(1, 1)
    testSeq.add(2, 2)
    testSeq.add(2, 3.2)
    if (testSeq.get(2) == 3.2):
        print("Add:\tpass")
    else:
        print("Add:\tfailed\nExiting...")
        sleep(2)
        exit()

    testSeq.rm(2)
    if testSeq.size() == 3:
        print("Rm:\tpass")
    else:
        print("Rm:\tfailed\nExiting...")
        sleep(2)
        exit()

    testSeq.set(1, 5)
    if (testSeq.get(1) == 5):
        print("Set:\tpass")
    else:
        print("Set:\tfailed\nExiting...")
        sleep(2)
        exit()

    print("SeqADT:\tAll Passed!")

    
if (input("test(1) or main(2): ") == 1):
    test()
else:
    main()