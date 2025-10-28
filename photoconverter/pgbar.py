"""
Legacy Progress Bar Module

This module is kept for backward compatibility.
New code should use tqdm instead of this module.

Deprecated: Use tqdm for modern progress bar functionality.
"""

import warnings
from typing import Union


def printProgressBar(
    iteration: int,
    total: int,
    prefix: str = '',
    suffix: str = '',
    decimals: int = 1,
    length: int = 100,
    fill: str = '█',
    printEnd: str = "\r"
) -> None:
    """
    Call in a loop to create terminal progress bar.
    
    DEPRECATED: Use tqdm instead for better functionality.
    
    Args:
        iteration: Current iteration (Int)
        total: Total iterations (Int)
        prefix: Prefix string (Str)
        suffix: Suffix string (Str)
        decimals: Positive number of decimals in percent complete (Int)
        length: Character length of bar (Int)
        fill: Bar fill character (Str)
        printEnd: End character (e.g. "\\r", "\\r\\n") (Str)
    """
    warnings.warn(
        "pgbar.printProgressBar is deprecated. Use tqdm instead.",
        DeprecationWarning,
        stacklevel=2
    )
    
    if total == 0:
        return
        
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)

    bar = fill * filledLength + '-' * (length - filledLength)

    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    
    # Print New Line on Complete
    if iteration == total:
        print()