# this file simply holds a list of all the classifiers we have enabled RandomizedSearchCV for. 
# if you would like to have more control over the process, and use GridSearchCV, please modify this file to say False for the algorithm you want to run GridSearchCV on.

def rsList():
    return {
        'clAdaBoost': True
    }
