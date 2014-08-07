"""
Parallel processing tools.
"""

import copy
import itertools
import numpy as np

def job_generator(parameters):
    """
    Create jobs out of parameters.
    
    Yields jobs.
    """   

    ranges = {} # Dict containing the iterables that are used for the parametric study.
    
    if parameters['iterable']:
        ranges.update(parameters['iterable'])
    
    if parameters['arange']:
        ranges.update( {key: np.arange(*value) for key, value in parameters['arange'].items()} )
    
    if parameters['linspace']:
        ranges.update( {key: np.linspace(*value) for key, value in parameters['linspace'].items()} )
    
    if parameters['logspace']:
        ranges.update( {key: np.logspace(*value) for key, value in parameters['logspace'].items()} )
       
    
    # Evaluate the product of the iterables. Yield a job in the form of a dictionary.
    for job in (dict(zip(ranges, x)) for x in itertools.product(*ranges.values())):
        job.update(copy.deepcopy(parameters['constant'])) # Add constant parameters.
        yield job
