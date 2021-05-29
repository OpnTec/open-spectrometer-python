# Spetrometer Python

[![Build Status](https://travis-ci.com/OpnTec/spectrometer-python.svg?branch=master)](https://travis-ci.com/OpnTec/spectrometer-python)
[![Gitter](https://badges.gitter.im/fossasia/pslab.svg)](https://gitter.im/fossasia/pslab?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

This repository provides scripts for the open spectrometer project to enable practitioners, students and citizen scientists to collect data with their spectrometer and have a good and fun learning experience. Enjoy!

The open spectrometer project consists of a web cam, simple lasercut parts, battery casing and a suitable LED lightning component. The spectrometer connects to a computer via USB, where the user can run the scripts provided in this repository to run experiments and take measurements. The two main components of this repository are analyse.py and calibrate.py. The analyse.py script is used to plot the absorbance spectra of measurements taken with a webcam spectrometer. The calibrate.py is useful for advanced users who want to understand the mechanics of scientific measurements and understand how to assess the quality of the data generated.

## Open Science and Background

By definition science should be open and reproducible. So, the outcome of an experiment can be verified by anyone. Unfortunately today this is not always the case. In order to be able to verify experiments all components used should be openly accessible. This includes the software and hardware of scientific instruments. Our spectrometer project follows this path. By giving access to all layers of the device used in a scientific experiment users can develop a deep understanding how scientific measurements are taken and practitioners are able to critically understand the limitations of one particular instrument.

## Communication

The spectrometer community is still small. There are overlaps with the Pocket Science Lab team. To stay connected with different community members we continue to use the PSLab Gitter channel for the beginning. We will set up a dedicated channel once the project is more established. Please join us here:
* [Pocket Science Channel](https://gitter.im/fossasia/pslab)

## Features and Implementation Status

|   **Feature**        | **Description**                                                      | **Status**            |
|----------------------|----------------------------------------------------------------------|-----------------------|
| USB Connection       | Transmit data using USB from a compatible spectrometer to a computer | :heavy_check_mark:    |
| Generate PNG         | Run the software on www.spectralworkbench.org with samples           | :heavy_check_mark:    |
| Calibration          | Calibrate using calibrate.py and report in analyse.py                | :heavy_check_mark:    |
| Scripts in Browers   | Scripts can be executed in the browser using repl.it                 | :heavy_check_mark:    |
| Scripts Locally      | Scripts can be executed on the computer without Internet             | :negative_squared_cross_mark: |
| Generate PNG Locally | Generate png images from collected data without Internet service     | :negative_squared_cross_mark: |

## Services used

* We use repl.it to run the Python script in the browser [repl.it/@DIYanalytics/analysepy](https://repl.it/@DIYanalytics/analysepy) to facilitate the use of the spectrometers to non programmers
* The script takes the png file from the experiment data from the web service of [spectralworkbench.org](https://spectralworkbench.org) and plots the analysis of those data

## How to use analyse.py to do experiments and collect data

1. Connect the spectrometer via USB to your computer
2. Transfer the liquid sample in the cuvette (liquid container for spectroscopy) and locate it in the spectrometer. Incase of chlorophyll A and B, you might do your own extraction and separation.
3. Take measurements with the webcam spectrometer using the spectral workbench mentioned above.
4. Insert the filename of your reference into the referenceFile slot, and all the filenames of the samples into the samples slot, separated by a comma.
5. Insert the desired title of the plot below and headers for the legend.
6. View the outcome of your measurements and the script and compare the plot obtained with the spectral absorbance of chlorophyll A and B found in literature (Search online for absorbance of chlorophyll).

## How to calibrate your device with calibrate.py

Calibrating a spectrometer means referencing the values that otherwise would represent pixels, and turning them into wavelengths, which is what the spectrometer is meant to measure. In order to create a correlation between pixels and wavelengths, a mercury light bulb is used, a compact fluorescent light (CFL). Because of its sharp emission peaks, it is possible to assign to some pixels some specific wavelength values and infer all the others.

As a reference you can use Wikipedia to view an image for the fluorescent lightning spectrum [here](https://commons.wikimedia.org/wiki/File:Fluorescent_lighting_spectrum_peaks_labelled.png) .

Steps to use calibrate.py:

1. Run the script calibrate.py with the file produced with the compact fluorescent light (CFL).
2. Use the magnification lens to note at which pixel corresponds which peak in the plot of the wikipedia reference.
3. Take at least 3 correlations, but the more, the better.
4. Open the main script, and insert (replace) in increasing order the pixel and wavelenghts previously noted in the respective slots.

## Contribution

This project was started by Alessandro Volpato. We welcome new contributors and feedback of users from around the world. Thank you!


## License

This projects is licensed under Apache v.2.0.

