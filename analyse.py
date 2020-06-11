#-------------------------------------------------------------------------------
# Name:        Plotting absorbance curves
# Purpose:     Analysing experiments's results
#
# Author:      Alessandro Volpato
#
# Created:     25/07/2018
# Copyright:   
# Licence:     CC BY-SA 4.0
#-------------------------------------------------------------------------------

#import io,sys
import math
import matplotlib.image as img
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


######## INSERT HERE THE FILE NAME ################
#						  #
# NOTE: Check the format!! png or csv             #
referenceFile = "IPA_Glass.png"

samples = ["1_IPA_Glass.png","2_IPA_Glass.png"]
plotDirectly = []

title = "Chlorophyll A and B in isopropilic alcohol"
plotColors = ["purple","darkgreen"]
patchLabels = ["Chlorophyll A","Chlorophyll B"]

saveFilename = "plot.png"
# Don't change them!!
#
###################################################

###### CALIBRATION HERE ###########################
###### INSERT HERE YOUR PIXEL CORRELATIONS ########
#
pixel =      [115,  146,  193,  250,  312,  329,  404]
wavelength = [405.4,436.6,487.7,546.5,611.6,631.1,708]
#
###################################################


####################################################################
#
# This is a function. Each time we call getSpectrum_PNG            #
# for the filename in brackets, we will execute these operations   #
#
def getSpectrum_PNG(filename):                                     #
    '''From a PNG file taken with spectralworkbench
        extracts a spectrum. Each channel's spectrum
        is calculated as column mean for the whole picture'''          #
    #
    # Reading the image                                            #
    print("Reading image")                                         #
    image = img.imread(filename)                                   #
    #
    # Preparing the variables                                      #
    imageR = []                                                    #
    imageG = []                                                    #
    imageB = []                                                    #
    imgWidth = len(image[0])                                       #
    imgHeight = len(image)                                         #
    #
    # Preparing the RGB arrays                                     #
    for i in range(imgWidth):                                      #
        imageR.append(image[0][i][0])                              #
        imageG.append(image[0][i][1])                              #
        imageB.append(image[0][i][2])                              #
    #
    # Columns summatory                                            #
    for i in range(imgHeight):                                     #
        for j in range(imgWidth):                                  #
            imageR[j]=imageR[j]+image[i][j][0]                     #
            imageG[j]=imageG[j]+image[i][j][1]                     #
            imageB[j]=imageB[j]+image[i][j][2]                     #
    #
    # Calculating the mean for every RGB column                    #
    for i in range(imgWidth):                                      #
        imageR[i]=imageR[i]/imgHeight                              #
        imageG[i]=imageG[i]/imgHeight                              #
        imageB[i]=imageB[i]/imgHeight                              #
    #
    # Merging the RGB channels by addition                         #
    spectrum = []                                                  #
    for i in range(imgWidth):                                      #
        spectrum.append((imageR[i]+imageG[i]+imageB[i])/3)         #
    #
    # returning the results of the operation                       #
    return spectrum                                                #
#
def getSpectrum_CSV(filename):                                     #
    '''From a CSV file containing the serie of measurements,
        splits the values and returns them as a list, the spectrum'''
    #
    # Reading the file                                             #
    print("Reading csv file")                                      #
    inFile = open(filename, "r")                                   #
    CSVline = inFile.read()                                        #
    #
    # Splitting the values                                         #
    spectrumSTR = CSVline.split(",")                               #
    #
    # Transforming the values from string to float type            #
    spectrum = []                                                  #
    for i in range(len(spectrumSTR)):                              #
        spectrum.append(float(spectrumSTR[i]))                     #
    #
    # Returning the results of the operation                       #
    return spectrum                                                #
#

# ----------- Function ----------------------------

def normalise(spectrumIn):
    
    spectrumOut = []
    
    maxPoint = max(spectrumIn)
    
    for value in spectrumIn:
        spectrumOut.append(value/maxPoint)
    
    return spectrumOut


def calcAbs(reference, sample):
    # Calculate transmittance and absorbance spectrum
    
    transmittance = []
    absorbance = []
    
    for i in range(len(reference)):
        if sample[i] == 0: # This 'if' part is to aqvoid math error due to 0/number
            transmittance.append(0)
            absorbance.append(0) # Conceptually wrong, if sample > reference, artificious data distortion has happened
        else:
            transmittance.append(sample[i]/reference[i])
            absorbance.append(-math.log(transmittance[i],10)/5)

    return absorbance



####################################################################

# A list of colors to use in python
colors = ['indigo' , 'gold' , 'hotpink' , 'firebrick' , 'indianred' , 'yellow' ,
          'mistyrose' , 'darkolivegreen' , 'olive' , 'darkseagreen' , 'pink' , 'tomato' ,
          'lightcoral' , 'orangered' , 'navajowhite' , 'lime' , 'palegreen' , 'darkslategrey' ,
          'greenyellow' , 'burlywood' , 'seashell' , 'mediumspringgreen' , 'fuchsia' ,
          'papayawhip' , 'blanchedalmond' , 'chartreuse' , 'dimgray' , 'black' , 'peachpuff' ,
          'springgreen' , 'aquamarine' , 'orange' , 'lightsalmon' , 'darkslategray' ,
          'brown' , 'ivory , dodgerblue' , 'peru' , 'lawngreen' , 'chocolate' , 'crimson' ,
          'forestgreen' , 'darkgrey' , 'lightseagreen' , 'cyan' , 'mintcream' , 'silver' ,
          'antiquewhite' , 'mediumorchid' , 'skyblue' , 'gray' , 'darkturquoise' , 'goldenrod' ,
          'darkgreen' , 'floralwhite' , 'darkviolet' , 'darkgray' , 'moccasin , saddlebrown' ,
          'grey' , 'darkslateblue' , 'lightskyblue' , 'lightpink , mediumvioletred' ,
          'slategrey' , 'red' , 'deeppink' , 'limegreen' , 'darkmagenta' , 'palegoldenrod' ,
          'plum' , 'turquoise' , 'lightgrey' , 'lightgoldenrodyellow' , 'darkgoldenrod' ,
          'lavender' , 'maroon' , 'yellowgreen' , 'sandybrown' , 'thistle' , 'violet' , 'navy' ,
          'magenta' , 'dimgrey' , 'tan' , 'rosybrown' , 'olivedrab' , 'blue' , 'lightblue' ,
          'ghostwhite' , 'honeydew' , 'cornflowerblue' , 'slateblue' , 'linen' , 'darkblue' ,
          'powderblue' , 'seagreen' , 'darkkhaki' , 'snow' , 'sienna' , 'mediumblue' , 'royalblue' ,
          'lightcyan' , 'green' , 'mediumpurple' , 'midnightblue' , 'cornsilk' , 'paleturquoise' ,
          'bisque' , 'slategray' , 'darkcyan' , 'khaki' , 'wheat' , 'teal' , 'darkorchid' , 'salmon' ,
          'deepskyblue' , 'rebeccapurple' , 'darkred' , 'steelblue' , 'palevioletred' ,
          'lightslategray' , 'aliceblue' , 'lightslategrey' , 'lightgreen' , 'orchid' ,
          'gainsboro' , 'mediumseagreen' , 'lightgray' , 'mediumturquoise' , 'lemonchiffon' ,
          'cadetblue , lightyellow , lavenderblush , coral , purple' , 'aqua' ,
          'mediumslateblue' , 'darkorange' , 'mediumaquamarine' , 'darksalmon' , 'beige' ,
          'blueviolet' , 'azure' , 'lightsteelblue' , 'oldlace']


# Preparing the plot

# Initialize and load spectra
reference = getSpectrum_PNG(referenceFile)

# Samples
samplesSpectra = []
for filenName in samples:
    samplesSpectra.append(getSpectrum_PNG(filenName))

absorbances = []
for spectrum in samplesSpectra:
    absorbances.append(normalise(calcAbs(reference, spectrum)))

# Plot without calculations
plotDirectlySpectra = []
for filenName in plotDirectly:
    plotDirectlySpectra.append((getSpectrum_PNG(filenName)))

PDirect = []
for spectrum in plotDirectlySpectra:
    PDirect.append(normalise(spectrum))

spectraToPlot = absorbances + PDirect

# Finding out the coefficients
params = np.polyfit(pixel,wavelength,3)
#return p = np.poly1d(range)

# Solving the equation for every pixel
# (Assigning to every pixel a wavelength)
nmAxis = []
for i in range(len(spectrum)):
    v1 = params[0]*float(i**3)
    v2 = params[1]*float(i**2)
    v3 = params[2]*float(i**1)
    v4 = params[3]*float(i**0)
    nmAxis.append(v1+v2+v3+v4)
# NOTE: This operation is quickly done with the later used:
# nmAxis = np.poly1d(len(spectrum))
# print(len(patchLabels), len(spectraToPlot))
if len(patchLabels) < len(spectraToPlot):
    patchLabels.append([""]*(len(spectraToPlot)-len(patchLabels)))

if len(plotColors) < len(spectraToPlot):
    plotColors = []
    for i in range(len(spectraToPlot)):
        plotColors.append(colors[i])

patches = []
for i in range(len(patchLabels)):
    patches.append(mpatches.Patch(color=plotColors[i], label=patchLabels[i]))

colorCounter = 0
for spectrum in spectraToPlot:
    plt.plot(nmAxis, spectrum, color = plotColors[colorCounter])
    colorCounter += 1

plt.title(title)
plt.legend(handles=patches)
plt.xlim(350, 950)
plt.ylim(-0.25,2)
plt.xlabel('Wavelegth (nm)')
plt.ylabel('Absorbance')

plt.savefig(saveFilename)
plt.show()


# END --------------------------------------------------------
