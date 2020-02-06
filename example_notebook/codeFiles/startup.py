#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
print('Base modules loaded')
print('Parameters loaded')

# import generic modules
import platform # to adjust automatically the read/write path to the machine being used (if the code is used on different computers)
import os
import numpy as np
from datetime import datetime

import pprint # to print readable dictionaries
pp = pprint.PrettyPrinter(indent=4)

# import self modules (import variables and functions defined in separate files)
#from dataImport.pathDef     import goodPath
#from spectrAnalysis.funclib import get_quality_threshold, extractBg_affine, extractBg_polynome, extractBg_cnst, extractNoBg
#from modelib                import gauss, lorentz, gaussMirror #, squaredGaussAsymetrical

#import date and time
date = datetime.today().strftime('%Y-%m-%d')


parameters = {
    # general path of all data
    'path':'/home/cam/Documents/WORK/Diffusion project/Diffusion_fiber_scan/',

    # specific subpath
    'subpath' : {
        '2D crystals'       : '{{path}}2D_crystals/',
        'single crystals'   : '{{path}}single_crystals/',
    },


    # parameters used to fitting spectrums
    'ordered type'          : 'linear',
    #'f_testQuality'         : get_quality_threshold(1000),# (bool) test the quality signal/noise of a spectrum
    #'f_extractBg'           : extractBg_cnst, # (funct) function that return a function ( return the background model )
    'validFitting'          : 5, #5              # max percent of discrepancy for a valid fit

    'search peak'           : True,
    'max_nb_of_peaks'       : 1,                # max number of peaks to research
    # the finesse value reflects the width of the expected peaks proportionally to the length of the spectrum, in percent.
    # For example a finesse of 5 will only detect peaks larger than 5% of the spectrum span.
    'search peak finesse'   : 40,
    'poly_order'            : 3,                # order of the polynomial regression
    'peaks min-height'      : 5,                # % of the max needed to be a peak
    'edge suppression'      : 10,               # % of span on each side
    'flat limit'            : 80,               # remove peaks found on a plateau ( > in % of π between peak and his span's limits )
    'hidden_peak_slope'     : [1, 33],          # (min, max) slope to find hidden peaks in % of the gradient

    #'get models'             : [ lambda x:gaussMirror ],#[ lambda x:squaredGaussAsymetrical], # liste des fonctions renvoyant le modèle à utiliser pour fiter. ( premier = premier ordre, deuxième = deuxième ordre etc...


    'testing'               : False,            # if not : dosent keep spectrum’s fit to save memory
    'maxDecory'             : 10,               # used to fit spectrum with model
}

# ---- multi-platform path style ---- #
# specific paths :
ordi = platform.node()

if ordi == 'CamDrive' :
    parameters['path'] = '/media/cam/Data/ANALYSIS/BERKELEY/Diffusion_fiber_scan/'
elif ordi == 'CamPad' :
    parameters['path'] = '/home/cam/Documents/WORK/Diffusion project/Diffusion_fiber_scan/'



# format subpath :
path = parameters['path']
for subpath_name, subpath in parameters['subpath'].items() :
    parameters['subpath'][subpath_name] = parameters['subpath'][subpath_name].replace('{{path}}', path)

# print for debug and info

print '\nYour custom settings:'
print '\ndesired repository for file read/write :\n'

pp.pprint({
    'path'   : parameters['path'],
    'subpath': parameters['subpath']
})

print '\nyour computer information :\n'

pp.pprint({
    'architecture': platform.architecture(),# returns information about the bit architecture
    'machine': platform.machine(),          # returns the machine type, e.g. 'i386'
    'node': platform.node(),                # returns the computer’s network name (may not be fully qualified!)
    'platform': platform.platform(),        # returns a single string identifying the underlying platform with as much useful information as possible.
    'processor':platform.processor(),       # returns the (real) processor name, e.g. 'amdk6'.
    'python_build': platform.python_build(),# returns a tuple (buildno, builddate) stating the Python build number and date as strings.
    'python_compiler':platform.python_compiler(), # returns a string identifying the compiler used for compiling Python.
    'python_version':platform.python_version(), # returns the Python version as string 'major.minor.patchlevel'
    'python_implementation':platform.python_implementation(), #returns a string identifying the Python implementation. Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.
    'release':platform.release(),           # returns the system’s release, e.g. '2.2.0' or 'NT'
    'system': platform.system(),            # returns the system/OS name, e.g. 'Linux', 'Windows', or 'Java'.
    'version': platform.version(),          # returns the system’s release version, e.g. '#3 on degas'
    'uname':platform.uname()                # returns a tuple (system, node, release, version, machine, processor)
})
