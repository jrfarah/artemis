"""
====================================
Filename:        testClient.py 
Author:            Joseph Farah 
Description:    Test client for the ARTEMIS program.        
====================================
Notes
     
"""

#------------- imports -------------#                   
import Explorer
import numpy as np
import matplotlib.pyplot as plt

#------------- classes -------------#
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def warning(message):
        print bcolors.WARNING + "[" + message + "]" + bcolors.ENDC

    @staticmethod
    def success(message):
        print bcolors.OKGREEN + "[" + message + "]" + bcolors.ENDC

    @staticmethod
    def failure(message):
        print bcolors.FAIL + "[" + message + "]" + bcolors.ENDC


#------------- functions -------------#
def testQuadratic():

    def quadratic(x):
        return -np.power(x - 3, 2)

    QuadraticExplorer = Explorer.Explore(
                        quadratic, 
                        order=1, 
                        resolution=50, 
                        bounds=False, 
                        optimize=np.max
                    )

    print "[QuadraticExplorer.finalParameterList: {0}]".format(QuadraticExplorer.finalParameterList)
    plt.plot(np.linspace(-10, 10, 50), quadratic(np.linspace(-10, 10, 50)))
    for vline in QuadraticExplorer.finalParameterList:
        plt.axvline(x=vline)
    plt.show()

def test2DQuadratic():

    def twoDimQuadratic(x, y):
        return np.power(x, 2) + np.power(y, 2)

    QuadraticExplorer = Explorer.Explore(
                    twoDimQuadratic, 
                    order=1, 
                    resolution=50, 
                    bounds=False, 
                    optimize=np.min
                )
    print "[QuadraticExplorer.finalParameterList: {0}]".format(QuadraticExplorer.finalParameterList)

def testQuasiQuadratic():

    def quasiQuadratic(x):
        return np.power(x, 4) + np.power(x, 3) + -4.4*np.power(x, 2) + -1.7*x + np.e

    QuadraticExplorer = Explorer.Explore(
                        quasiQuadratic, 
                        order=1, 
                        resolution=50, 
                        bounds=[(0, 2)], 
                        optimize=np.min
                    )

    print "[QuadraticExplorer.finalParameterList: {0}]".format(QuadraticExplorer.finalParameterList)
    plt.plot(np.linspace(-2, 2, 50), quasiQuadratic(np.linspace(-2, 2, 50)))
    for vline in QuadraticExplorer.finalParameterList:
        plt.axvline(x=vline)
    plt.show()



def main():
    """
        Main function execution.
    
        Args:
            none (none): none
    
        Returns:
            none (none): none
    
    """
    
    #------------- begin program -------------# 
    bcolors.success("Test client has commenced with no compile-time errors.")

    testQuadratic()
    test2DQuadratic()
    testQuasiQuadratic()

    #------------- terminate program -------------# 
    bcolors.success("Test client has terminated with no run-time errors.")
    

#------------- switchboard -------------#
if __name__ == '__main__':
    main()