# Spetrometer Python

The goal of this repository is to provide a script for the open spectrometer project to enable practitioners, students and citizen scientists to have a good and fun learning experience. Enjoy!

The analyse.py script is used to plot the absorbance spectra of measurements taken with a webcam spectrometer.
Additionally, it is extremely useful to deeply understand how scientific measurements are taken and to critically understand limitations of a particular instrument.

# Current Status

The script is already set for being tried. Run the script and compare the plot obtained with the spectral absorbance of chlorophyll A and B found in literature (Search online for absorbance of chlorophyll).

# How to use analyse.py

The script takes .png files generated from the website https://www.spectralworkbench.org
Execute your chemical extraction, isolate pigments, and take measurements with a webcam spectrometer using the spectral workbench mentioned above.
After calibrating the spectrometer (see calibration below) insert the filename of your reference into the referenceFile slot, and all the filenames of the samples into the samples slot, separated by a comma.
Insert the desired title of the plot below.

# How to Calibrate Your Device with calibrate.py

(In this example, the device is already calibrated and this part can be skipped)
Calibrating a spectrometer means graduating the values that otherwise would represent pixel, and turning them into wavelength, which is what the spectrometer is meant to measure.
In order to create a correlation between pixels and wavelengths, a mercury light is used, a compact fluorescent light (CFL). Because of it's sharp emission peaks, it is possible to assign to some pixels a specific wavelength value.
Open the wikipedia webpage for the reference https://commons.wikimedia.org/wiki/File:Fluorescent_lighting_spectrum_peaks_labelled.png
Run the script ShowSpectrum_ForCalibratingPeaks.py with the file produced with the CFL.
Use the magnification lens to note at which pixel corresponds which peak in the plot of the wikipedia reference.
Take at least 3 correlations, but the more, the better.
Open the main script, and insert(replace) in increasing order the pixel and waveleghts previously noted in the respetive slots.

# Contribution

This project was started by Alessandro Volpato. We welcome new contributors and feedback of users from around the world. Thank you!


# License

This projects is licensed under Apache v.2.0.
