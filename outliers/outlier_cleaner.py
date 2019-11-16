#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    ### your code goes here
    errors = []
    for (key, pred) in enumerate(predictions):
        # the abs different counts
        err = abs(pred - net_worths[key])
        cleaned_data.append((ages[key], net_worths[key], err))

    from operator import itemgetter
    # sort by the error
    sorted_data = sorted(cleaned_data, key=itemgetter(2))

    # remove the highest 10%
    num_to_remove = int(len(cleaned_data) * 0.1)
    cleaned_data = sorted_data[0:len(sorted_data)-num_to_remove]

    return cleaned_data

