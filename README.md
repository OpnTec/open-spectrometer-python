# Spetrometer Python

This repository provides scripts for the open spectrometer project to enable practitioners, students and citizen scientists to collect data with their spectrometer and have a good and fun learning experience. Enjoy!

The open spectrometer project consists of a web cam, simple lasercut parts, battery casing and a suitable LED lightning component. The spectrometer connects to a computer via USB, where the user can run the scripts provided in this repository to run experiments and take measurements. The two main components of this repository are analyse.py and calibrate.py. The analyse.py script is used to plot the absorbance spectra of measurements taken with a webcam spectrometer. The calibrate.py is useful for advanced users who want to calibrate their device setup to provide measurements and data in a very high quality.

## Open Science and Background

By definition science should be open and reproducible. So, the outcome of an experiment can be verified by anyone. Unfortunately today this is not always the case. In order to be able to verify experiments all components used in an experiment should be openly accessible. This includes the software and hardware of scientific instruments. Our spectrometer project follows this path. By giving access to all layers of the device used in a scientific experiment user can develop a deep understanding how scientific measurements are taken and practicioners are able to critically understand the limitations of the particular instrument.

## Features

* Transmit data using USB from a compatible spectrometer to a computer
* Run analyse.py script and generate png file
* Calibrate using calibrate.py

## Services used

* We use repl.it to run the Python script in the browser https://repl.it/@DIYanalytics/SpectrometryScript
* The script generates the png file from the experiment data using the web service of https://spectralworkbench.org

## How to use analyse.py to do experiments and collect data

1. Connect the spetrometer via USB to your computer
2. Add the fluid into the containers and locate them in the spectrometer. This could include executing your chemical extraction and isolating pigments.
3. Take measurements with the webcam spectrometer using the spectral workbench mentioned above.
4. Insert the filename of your reference into the referenceFile slot, and all the filenames of the samples into the samples slot, separated by a comma.
5. Insert the desired title of the plot below.
6. View the outcome of your measurements and the script and compare the plot obtained with the spectral absorbance of chlorophyll A and B found in literature (Search online for absorbance of chlorophyll).

## How to calibrate your device with calibrate.py

Calibrating a spectrometer means graduating the values that otherwise would represent pixel, and turning them into wavelength, which is what the spectrometer is meant to measure. In order to create a correlation between pixels and wavelengths, a mercury light is used, a compact fluorescent light (CFL). Because of its sharp emission peaks, it is possible to assign to some pixels a specific wavelength value.

As a reference you can use Wikipedia to view an image for the fluorescent lightning spectrum [here](https://commons.wikimedia.org/wiki/File:Fluorescent_lighting_spectrum_peaks_labelled.png) .

Steps to use calibrate.py:

1. Run the script calibrate.py with the file produced with the compact fluoreschent light (CFL).
2. Use the magnification lens to note at which pixel corresponds which peak in the plot of the wikipedia reference.
3. Take at least 3 correlations, but the more, the better.
4. Open the main script, and insert (replace) in increasing order the pixel and waveleghts previously noted in the respetive slots.

## Contribution

This project was started by Alessandro Volpato. We welcome new contributors and feedback of users from around the world. Thank you!


## License

This projects is licensed under Apache v.2.0.
