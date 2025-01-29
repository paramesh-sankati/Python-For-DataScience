#Filtering can be by three ways 
''' 
    1.using bool ndarray
        --create a boolean array with condition
        --pass bool array to original ndarray
    2.using where function
        --syntax: 
                index=np.where(conditon)
                ind=np.where(a>10)
                gives indices of satisfied condition elements
                using loop and indices get the required elements 
        --where is also used to replace missinig values with any other values
    3.using extract function
        --syntax:
                res=numpy.extract(condition,array)

'''