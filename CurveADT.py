## @file CurveADT.py
#  @author Connor Czarnuch
#  @date 01/21/2018

from SeqADT import SeqT
from numpy import polyfit, poly1d
from time import sleep


## @brief CurveT contains several methods that can interpolate and extrapolate values from mathematical functions read from a file.
class CurveT:
    ## @brief The init class constructs a list within the class.
    def __init__(self):
        ## @brief A variable of type SeqT to store the values of x of a mathematical function
        self.curveX = SeqT()
        ## @brief A variable of type SeqT to store the values of y of a mathematical function
        self.curveY = SeqT()
        ## @brief A variable of type int to store the degree of a polynomial
        self.degree = int()

    ## @brief The CurveT method reads input from a user supplied txt file and stores the values in a SeqT list.
    #  @details The user supplied file should have an initial line containing the degree of that function as an integer. The following lines should be in the format "x,y", excluding the quotation marks, for each point. Each point should be stored on its own line. The program prints the x and y values to check with the user or exits if a file is unable to be found.
    #  @param s is the name of the file that you wish to be examined.
    #  @return There is no returned value, however the values are printed and stored in the object.
    def CurveT(self, s):
            try:
                inFile = open(s, 'r')
                self.degree = int(inFile.readline())
                line = inFile.readline()
                while(line):
                    row = line.split(',')
                    self.curveX.add(self.curveX.size(), float(row[0]))
                    self.curveY.add(self.curveY.size(), float(row[1]))
                    line = inFile.readline()
                inFile.close()
                print(self.curveX.lst)
                print(self.curveY.lst)

            except IOError:
                print("Are you sure that that file is in the directory?\nExiting...")
                sleep(2)
                exit()

            except:
                print("Is the file in the right format?\nExiting...")
                sleep(2)
                exit()

    ## @brief linVal is a method that takes in an x-value and interpolates the supplied data to find its correesponding y-value for a linear function.
    #  @param x is an x-value for which the user wishes to find its corresponding y-value.
    #  @return The method returns the y-value of the supplied x-value or exits the program if an error is encountered.
    def linVal(self, x):
        try:
            index = int(self.curveX.indexInSeq(x))
            x1 = self.curveX.lst[index]
            y1 = self.curveY.lst[index]
            x2 = self.curveX.lst[index + 1]
            y2 = self.curveY.lst[index + 1]

            y = ((y2 - y1) / (x2 - x1)) * (x - x1) + y1
            return y
        except TypeError:
            print("Please make sure that your x-value is within the data of the given file, please revise.\nExiting...")
            sleep(2)
            exit()

    ## @brief quadVal is a method that takes in an x-value and interpolates the supplied data to find its corresponding y-value for a quadratic function.
    #  @param x is an x-value for which the user wishes to find its corresponding y-value.
    #  @return The method returns the y-value of the supplied x-value or exits the program if an error is encountered.
    def quadVal(self, x):
        try:
            index = int(self.curveX.indexInSeq(x))
            x0 = self.curveX.lst[index - 1]
            y0 = self.curveY.lst[index - 1]
            x1 = self.curveX.lst[index]
            y1 = self.curveY.lst[index]
            x2 = self.curveX.lst[index + 1]
            y2 = self.curveY.lst[index + 1]

            ytop = y1 + (y2 - y0) / (x2 - x0) * (x - x1) + (y2 - 2 * y1 + y0)
            ybot = (2 * (x2 - x1) ** 2) * ((x - x1) ** 2)
            y = ytop / ybot
            return y
        except TypeError:
            print("Please make sure that your x-value is within the data of the given file, please revise.\nExiting...")
            sleep(2)
            exit()

    ## @brief npolyval is a method that takes in and can find any y-value for a supplied x-value. This method can extrapolate polynomials rather than just linear or quadratic mathematical functions.
    #  @param x is an x-value for which the user wishes to find its corresponding y-value.
    #  @return The method returns the y-value of the supplied x-value or exits the program if an error is encountered.
    def npolyval(self, n, x):
        if self.curveX.size() <= 1:
            print("There are not enough data points in the given file, please revise.\nExiting...")
            sleep(2)
            exit()
        else:
            coefs = polyfit(self.curveX.lst, self.curveY.lst, n)
            y = poly1d(coefs)
            return y(x)


print("Warning: If the answer is incorrect, please try adding more data points\ninto your input file, or check for correct polynomial degree.\n")
