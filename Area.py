import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit
import textwrap
import tkinter as tk

#-----------------Import Data-----------------#

def ImportData():
    global filePath

    x = []; y = []

    with open(filePath, 'r') as file:

        reader = csv.reader(file)
        next(reader)
        next(reader)

        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))

    x = np.array(x)
    y = np.array(y)

    return x, y

#-----------------Find Closest Data Point-----------------#


def findPoint(xValue):

    minIndex = np.argmin(np.abs(x-xValue))

    return minIndex

#-----------------Calculate Area-----------------#

def Background(horizontal, m, b):

    return m * (horizontal) + b

def FindArea():

    #create line of best fit for background and ensure points can be chosen in any order
    LBG1 = int(chosenPoints[0]); LBG2 = int(chosenPoints[1]); RBG1 = int(chosenPoints[2]); RBG2 = int(chosenPoints[3])

    if LBG2 < LBG1:
        temp = LBG2
        LBG2 = LBG1
        LBG1 = temp

    if RBG2 < RBG1:
        temp = RBG2
        RBG2 = RBG1
        RBG1 = temp

    #display line of best fit
    horizontal = np.concatenate((x[LBG1:(LBG2+1)], x[RBG1:(RBG2+1)]))
    vertical = np.concatenate((y[LBG1:(LBG2+1)], y[RBG1:(RBG2+1)]))

    params, covariance = curve_fit(Background, horizontal, vertical)
    
    vertical = Background(horizontal, *params)
    horizontalLim = plt.xlim()
    verticalLim = plt.ylim()
    plt.clf()
    plt.xlim(horizontalLim)
    plt.ylim(verticalLim)
    plt.plot(x,y,color="steelblue")
    plt.xlabel("Wave Number $\mathrm{cm^{-1}}$")
    plt.ylabel("Absorbance")
    plt.show()
    plt.plot(horizontal,vertical,color="red")
    plt.show()

    #display shaded area
    leftBound = int(chosenPoints[4])
    rightBound = int(chosenPoints[5])

    if rightBound < leftBound:
        temp = rightBound
        rightBound = leftBound
        leftBound = temp

    spectrumX = x[leftBound:(rightBound+1)]
    spectrumY = y[leftBound:(rightBound+1)]
    backgroundY = Background(spectrumX, *params)
    plt.fill_between(spectrumX, backgroundY, spectrumY, color="gray")
    plt.show()

    Area = 0
    for i in range(np.size(spectrumX)):

        if i+1 > np.size(spectrumX)-1:
            break
        else:
            width = np.abs(spectrumX[i+1]-spectrumX[i])
            Area += (spectrumY[i]-backgroundY[i]) * width

    return Area

#-----------------SCROLL EVENT-----------------#

def on_scroll(event):

    #zoom in vs. zoom out when scroll wheel is used

    if stage != "Instructions":
        xlim1 = plt.xlim()[0]
        xlim2 = plt.xlim()[1]
        ylim1 = plt.ylim()[0]
        ylim2 = plt.ylim()[1]

        if event.step < 0:
            plt.xlim([xlim1+np.abs(xlim2-xlim1)/100, xlim2-np.abs(xlim2-xlim1)/100])
            plt.ylim([ylim1+np.abs(ylim2-ylim1)/100, ylim2-np.abs(ylim2-ylim1)/100])
        else:
            plt.xlim([xlim1-np.abs(xlim2-xlim1)/100, xlim2+np.abs(xlim2-xlim1)/100])
            plt.ylim([ylim1-np.abs(ylim2-ylim1)/100, ylim2+np.abs(ylim2-ylim1)/100])
   

#-----------------CLICK EVENT-----------------#

def on_click(event):
    if event.inaxes is not None:

        x_chosen, y_chosen = event.inaxes.transData.inverted().transform([event.x, event.y])
        global stage
        global chosenPoints

        if stage == "Instructions" and event.inaxes.get_navigate_mode() is None:

            instructions1.remove(); instructions2.remove()
            LBackground1()

        elif stage == "LBackground1" and event.inaxes.get_navigate_mode() is None:

            pointIndex = findPoint(x_chosen)
            chosenPoints[0] = pointIndex

            y_range = plt.gca().get_ylim()[1] - plt.gca().get_ylim()[0]
            vertical = np.arange(ylim[0], ylim[1]+0.1,0.1)
            horizontal = x_chosen * np.ones(np.size(vertical))
            plt.plot(horizontal,vertical, color="blue")
            plt.show()

            LBackground2()

        elif stage == "LBackground2" and event.inaxes.get_navigate_mode() is None:

            pointIndex = findPoint(x_chosen)
            chosenPoints[1] = pointIndex

            y_range = plt.gca().get_ylim()[1] - plt.gca().get_ylim()[0]
            vertical = np.arange(ylim[0], ylim[1]+0.1,0.1)
            horizontal = x_chosen * np.ones(np.size(vertical))
            plt.plot(horizontal,vertical, color="blue")
            plt.show()

            RBackground1()

        elif stage == "RBackground1" and event.inaxes.get_navigate_mode() is None:

            pointIndex = findPoint(x_chosen)
            chosenPoints[2] = pointIndex

            y_range = plt.gca().get_ylim()[1] - plt.gca().get_ylim()[0]
            vertical = np.arange(ylim[0], ylim[1]+0.1,0.1)
            horizontal = x_chosen * np.ones(np.size(vertical))
            plt.plot(horizontal,vertical, color="blue")
            plt.show()

            RBackground2()

        elif stage == "RBackground2" and event.inaxes.get_navigate_mode() is None:

            pointIndex = findPoint(x_chosen)
            chosenPoints[3] = pointIndex

            y_range = plt.gca().get_ylim()[1] - plt.gca().get_ylim()[0]
            vertical = np.arange(ylim[0], ylim[1]+0.1,0.1)
            horizontal = x_chosen * np.ones(np.size(vertical))
            plt.plot(horizontal,vertical, color="blue")
            plt.show()

            Area1()

        elif stage == "Area1" and event.inaxes.get_navigate_mode() is None:

            pointIndex = findPoint(x_chosen)
            chosenPoints[4] = pointIndex

            y_range = plt.gca().get_ylim()[1] - plt.gca().get_ylim()[0]
            vertical = np.arange(ylim[0], ylim[1]+0.1,0.1)
            horizontal = x_chosen * np.ones(np.size(vertical))
            plt.plot(horizontal,vertical, color="green")
            plt.show()

            Area2()

        elif stage == "Area2" and event.inaxes.get_navigate_mode() is None:

            pointIndex = findPoint(x_chosen)
            chosenPoints[5] = pointIndex

            y_range = plt.gca().get_ylim()[1] - plt.gca().get_ylim()[0]
            vertical = np.arange(ylim[0], ylim[1]+0.1,0.1)
            horizontal = x_chosen * np.ones(np.size(vertical))
            plt.plot(horizontal,vertical, color="green")
            plt.show()

            Waiting()

        elif stage == "Waiting" and event.inaxes.get_navigate_mode() is None:

            button.remove()
            horizontalLim = plt.xlim()
            verticalLim = plt.ylim()
            plt.clf()
            plt.xlim(horizontalLim)
            plt.ylim(verticalLim)

            LBackground1()

#-----------------STAGES-----------------#

def Instructions():

    global stage
    stage = "Instructions"

    plt.ion()

    infoTitle = "QUICK GUIDE (click on the screen to continue)"
    info1 = "You will want to zoom in on the peak of interest. Notice that peaks come in pairs called doublets. First, a background scan will use an interval to the left of the doublet and to the right of it to provide a line of best fit for the background. Then, you are free to choose the interval that you want to find the area of."
    info2 = "You will choose a point by left clicking the graph. The program automatically knows which point you are referring to even if you are not clicking exactly on the curve. Also, an interval is determined by 2 points and the order in which you select them does not matter (choosing the right bound first or left bound first is fine either way)."

    plt.title(infoTitle, fontweight="bold")

    wrap = textwrap.fill(info1, width=50)
    global instructions1 
    instructions1 = plt.text(0.5,0.65, wrap, fontsize=12, ha="center", va="center", transform=plt.gcf().transFigure, clip_on=True)

    wrap = textwrap.fill(info2, width=50)
    global instructions2
    instructions2 = plt.text(0.5,0.32, wrap, fontsize=12, ha="center", va="center", transform=plt.gcf().transFigure, clip_on=True)

    plt.gcf().canvas.mpl_connect('button_press_event', on_click)
    plt.gcf().canvas.mpl_connect('scroll_event', on_scroll)
    plt.show(block=True)

def LBackground1():

    #Note: THIS DISPLAYS THE VERY FIRST PLOT IN THE PROGRAM
    global stage
    stage = "LBackground1"

    plt.plot(x,y, color="black")
    plt.xlabel("Wave Number $\mathrm{cm^{-1}}$")
    plt.ylabel("Absorbance")
    plt.title("Background Scan: Choose 2 Points to the Left of the Doublet")
    plt.show()

    global xlim
    global ylim
    xlim = plt.xlim()
    ylim = plt.ylim()

def LBackground2():

    global stage
    stage = "LBackground2"

    plt.title("Background Scan: Choose 1 More to the Left of the Doublet")
    plt.show()

def RBackground1():

    global stage
    stage = "RBackground1"

    plt.title("Background Scan: Choose 2 Points to the Right of the Doublet")
    plt.show()

def RBackground2():

    global stage
    stage = "RBackground2"

    plt.title("Background Scan: Choose 1 More to the Right of the Doublet")
    plt.show()

def Area1():

    global stage
    stage = "Area1"

    plt.title("Area Selection: Choose 2 Points to Find the Area Between")
    plt.show()

def Area2():

    global stage
    stage = "Area2"

    plt.title("Area Selection: Choose 1 More Point")
    plt.show()

def Waiting():

    global stage
    stage = "Waiting"
    
    area = FindArea()
    plt.title("Area: " + str(area))

    global button
    button = plt.text(0.5,0.5, "Continue", bbox=dict(boxstyle="round", facecolor="gray", alpha = 0.5) , fontsize=12, ha="center", va="center", transform=plt.gcf().transFigure, clip_on=True)
    plt.show()

#-----------------MAIN CODE-----------------#

#Stages: Instructions->LBackground1->LBackground2->RBackground1->RBackground2->Area1->Area2->Waiting
stage = "" 
#Index of Chosen Points: LBackground1, LBackground2, RBackground1, RBackground2, Area1, Area2
chosenPoints = np.zeros(6)

#Ask user to input file path where data is
filePath = ""
def getInput():
    global filePath
    filePath = entry.get()
    root.destroy()

root = tk.Tk()
root.title("Area Program")
label = tk.Label(root, text="Enter the absolute path of the file:\nNote: It must be a .csv file with 2 columns (x, y). x-values must be in ascending or descending order.")
label.pack(pady=10, padx=10)
entry = tk.Entry(root, width = 60)
entry.pack(pady=10, padx=10)
button = tk.Button(root, text="Confirm", command=getInput)
button.pack(pady=10, padx=10)

root.mainloop()

#Import the data from the file and start the main program
x, y = ImportData()

Instructions()