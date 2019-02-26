"""
====================================
Filename:           Explorer.py
Author:             Joseph Farah 
Description:        Parameter space explorer for ARTEMIS   
====================================
Notes
     
"""

#------------- imports -------------#                   
import numpy
from funcsigs import signature

#------------- classes -------------#
class bcolors:
    HEADER      = '\033[95m'
    OKBLUE      = '\033[94m'
    OKGREEN     = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'

    @staticmethod
    def warning(message):
        print bcolors.WARNING + "[" + message + "]" + bcolors.ENDC

    @staticmethod
    def success(message):
        print bcolors.OKGREEN + "[" + message + "]" + bcolors.ENDC

    @staticmethod
    def failure(message):
        print bcolors.FAIL + "[" + message + "]" + bcolors.ENDC


class Explore(object):
    """
        Class to store information on parameter space and perform
        exploration operations.
    
        Args:
            function    (Function):     function to explore
            order       (float):        10^order will define a rough limit on the parameter space (DEFAULT 10)
            resolution  (float/list):   resolution of each respective parameter space (DEFAULT 100)
            bounds      (bool/list):    optional list of bounds (DEFAULT FALSE)
            optimize    (function):     how the optimizationn will be identified
    
        Returns:
            none (none): none
    
    """

    def __init__(self, function, order=10, resolution=100, bounds=False, optimize=numpy.max):
        """
            Initializes the class
        
            Args:
                See class docstring for argument description
        
            Returns:
                See class docstring for return description      
        
        """

        #------------- reassign characteristic variables -------------#
        self.function   = function
        self.order      = order
        self.resolution = resolution
        self.bounds     = bounds

        ## conditionals ##
        self.boolIterateOverResolution  = False
        self.boolIterateOverBounds      = False

        if bounds is not False:
            self.boolIterateOverBounds = True
        if type(resolution) == type(range(10)):
            self.boolIterateOverResolution = True


        #------------- construct parameter space -------------#

        ## how many arguments does the function have? ##
        self.numOfArguments = len(signature(function).parameters)

        ## construct a simple uniform parameter space if bounds and resolution is not set ##
        if not self.boolIterateOverBounds and not self.boolIterateOverResolution:
            tempArgList = []
            for arg in range(self.numOfArguments):
                tempArgList.append(numpy.linspace(-10**order, 10**order, resolution))

            self.parameterSpace = numpy.meshgrid(*tempArgList, sparse=True)
            self.responseSpace  = function(*self.parameterSpace)

        ## allow user to specify bounds and/or resolution ##
        elif not self.boolIterateOverBounds and self.boolIterateOverResolution:
            tempArgList = []
            for arg in range(self.numOfArguments):
                tempArgList.append(numpy.linspace(-10**order, 10**order, resolution[arg]))

        elif self.boolIterateOverBounds and not self.boolIterateOverResolution:
            tempArgList = []
            for arg in range(self.numOfArguments):
                tempArgList.append(numpy.linspace(bounds[arg][0], bounds[arg][1], resolution))

            self.parameterSpace = numpy.meshgrid(*tempArgList, sparse=True)
            self.responseSpace  = function(*self.parameterSpace)

        elif self.boolIterateOverBounds and self.boolIterateOverResolution:
            tempArgList = []
            for arg in range(self.numOfArguments):
                tempArgList.append(numpy.linspace(bounds[arg][0], bounds[arg][1], resolution[arg]))

            self.parameterSpace = numpy.meshgrid(*tempArgList, sparse=True)
            self.responseSpace  = function(*self.parameterSpace)


        #------------- solve parameter space -------------#
        self.finalParameterList = [[] for basis in range(self.numOfArguments)]
        self.optimumLocations   = numpy.where(self.responseSpace == optimize(self.responseSpace))
        for b, basis in enumerate(tempArgList):
            basisOptimumLocation = self.optimumLocations[b]
            for loc in basisOptimumLocation:
                self.finalParameterList[b].append(self.parameterSpace[b].flatten()[loc])

        #------------- tranpose and clean the result -------------#
        self.finalParameterList = numpy.array(self.finalParameterList).T

    
    def forloop(self, array, index, function, newArray):
        """
            Recursive for loop definition to apply operations to an n-dimensional parameter space.
        
            Args:
                array (list): list of list of parameters
                index (integer): which parameter direction
                function (function): function to apply to each element
                newArray (list): array to add function output to 
        
            Returns:
                none (none): none
        
        """

        tmpList = []
        for p, parameter in enumerate(array[index]):
           tmpList.append(function(parameter)) 

         
        
     
    

#------------- intro message -------------#
intro = """
==================================================
==================================================
    ___    ____  ______________  ____________
   /   |  / __ \/_  __/ ____/  |/  /  _/ ___/
  / /| | / /_/ / / / / __/ / /|_/ // / \__ \ 
 / ___ |/ _, _/ / / / /___/ /  / // / ___/ / 
/_/  |_/_/ |_| /_/ /_____/_/  /_/___//____/  

==================================================
==================================================


v0.0.1 has begun.

"""
print intro

#------------- functions -------------#
def main():
    """
        Main function execution. Unit testing (if needed.)
    
        Args:
            none (none): none
    
        Returns:
            none (none): none
    
    """
    
    #------------- begin program -------------# 
    bcolors.success("Unit-testing has commenced with no compile-time errors.")



    #------------- terminate program -------------# 
    bcolors.success("Unit-testing has terminated with no run-time errors.")
    

#------------- switchboard -------------#
if __name__ == '__main__':
    main()