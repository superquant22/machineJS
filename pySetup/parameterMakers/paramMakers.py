# ok, unfortunately, this is how it probably has to work:
# 1. we manually (hard code the names in here) import all the individual parameterMaker files here
# 2. we have a master calculateParams function

# 3. into that function we will pass X and y
# 4. that function will then go off and invoke all the individual parameterMaker functions, saving their results into a dictionary with keys that mirror 'clRandomForest'
# 5. that function will then return the dictionary
# 6. then back in training.py we can look up the classifierName within that dictionary to get the parameters

import rfGiniParamMaker
import rfEntropyParamMaker
import svcFirstParameterMaker
import svcFirstParameterMaker
import svcShrinking
import clnnSknn
import clnnSknn3Layer
import clKnn
import clLogisticRegression
import clAdaBoost
import clXGBoost
from sendMessages import printParent

def makeAll(X,y,globalArgs, dev):
    returnDict = {
        'clRfGini':rfGiniParamMaker.makeParams(X,y,globalArgs, dev),
        'clRfEntropy':rfEntropyParamMaker.makeParams(X,y,globalArgs, dev),
        'clSVCFirst':svcFirstParameterMaker.makeParams(X,y,globalArgs, dev),
        'clSVCFirst':svcFirstParameterMaker.makeParams(X,y,globalArgs, dev),
        'clSVCShrinking':svcShrinking.makeParams(X,y,globalArgs, dev),
        'clKnn':clKnn.makeParams(X,y,globalArgs, dev),
        'clLogisticRegression':clLogisticRegression.makeParams(X,y,globalArgs, dev),
        'clnnSknn3Layer':clnnSknn3Layer.makeParams(X,y,globalArgs, dev),
        'clnnSknn':clnnSknn.makeParams(X,y,globalArgs, dev),
        'clAdaBoost':clAdaBoost.makeParams(X,y,globalArgs, dev),
        'clXGBoost':clXGBoost.makeParams(X,y,globalArgs, dev)
    }
    return returnDict
