# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar<br>
    @params:<br>
        iteration   - Required  : current iteration (Int)<br>
        total       - Required  : total iterations (Int)<br>
        prefix      - Optional  : prefix string (Str)<br>
        suffix      - Optional  : suffix string (Str)<br>
        decimals    - Optional  : positive number of decimals in percent complete (Int)<br>
        length      - Optional  : character length of bar (Int)<br>
        fill        - Optional  : bar fill character (Str)<br>
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent         = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength    = int(length * iteration // total)

    bar = fill * filledLength + '-' * (length - filledLength)

    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    
    # Print New Line on Complete
    if iteration == total: 
        print()