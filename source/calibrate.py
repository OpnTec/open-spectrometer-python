import io,sys
import matplotlib.image as img
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib import colors as mcolors

# ------ INSER HERE THE FILE NAMES ----------------

calibFile = "cfl.png"
saveFilename = "cfl_plot.png"

# ----------- END ---------------------------------

# ----------- Function ----------------------------

def getSpectrumPNG(filename):
	'''From a PNG file taken with spectralworkbench
	extracts a spectrum. Each channel's spectrum
	is calculated as column mean for the whole picture'''

	image = img.imread(filename)

	imageR = []
	imageG = []
	imageB = []
	imgWidth = len(image[0])
	imgHeight = len(image)

	# Preparing arrays
	for i in range(imgWidth):
		imageR.append(image[0][i][0])
		imageG.append(image[0][i][1])
		imageB.append(image[0][i][2])

	# Columns summatory
	for i in range(imgHeight):
		for j in range(imgWidth):
			imageR[j]=imageR[j]+image[i][j][0]
			imageG[j]=imageG[j]+image[i][j][1]
			imageB[j]=imageB[j]+image[i][j][2]

	# Calculating the mean for every column
	for i in range(imgWidth):
		imageR[i]=imageR[i]/640
		imageG[i]=imageG[i]/640
		imageB[i]=imageB[i]/640

	# Merging the RGB channels by addition
	spectrum = []
	for i in range(imgWidth):
		spectrum.append((imageR[i]+imageG[i]+imageB[i])/3)

	return spectrum

# -------------- Execution ----------------------

# Initialize and load spectra
spectrum = getSpectrumPNG(calibFile)

plt.plot(spectrum)

#plt.ylim(0,1)
plt.xlabel('Pixel ID')
plt.ylabel('Light intensity')

plt.savefig(saveFilename)
plt.show()


