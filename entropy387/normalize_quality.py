def normalize_quality(my_dict):
    """ 
    The function returns a dictionary with normalized qualities q1 and q2
    """
    max_q1 = max([d["q1"] for d in my_dict['nodes']]) # Find the maximum value of q1
    max_q2 = max([d["q2"] for d in my_dict['nodes']]) # Find the maximum value of q1
    
    my_dict_normalized = my_dict.copy() # Create a copy of the original dictionary
    for item in my_dict_normalized['nodes']:
        # Divide the values of 'q1' and 'q2' by their respective maximum values. This normalizes the quality metrics to a range between 0 and 1
        item["q1"] /= max_q1
        item["q2"] /= max_q2
        
    return my_dict_normalized
    