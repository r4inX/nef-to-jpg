import glob
import os
from pathlib import Path
from random import random
import subprocess
import rawpy
import imageio
from tkinter import Tk
from tkinter.filedialog import askdirectory
import pgbar
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')


def main():
    print('================================')
    print('STARTING NEF-to-JPG Converter V1')
    print('================================')
    print('\n')

    # let the user select the directory
    directory = askdirectory(title='Select Folder with .NEF / .nef Files to')
    exportDir = directory + '/export_' + str(random()).replace('.','') + '/'

    if not directory:
        print('No Directory selected\nExiting...')
        exit()

    # create the export folder
    print('Creating Export Directory (' + exportDir +')...')
    os.mkdir(exportDir)

    # rename .nef to .NEF 
    nefFiles = glob.glob(f"{directory}/*.nef")

    for selectedFile in nefFiles:
        p = Path(selectedFile)
        p.rename(p.with_suffix('.NEF'))

    # sometimes the file ending can be .nef or .NEF, therefore I included both possibilities to save extra work.
    pathNEF = glob.glob(f"{directory}/*.NEF")
    count   = 0

    # check the total number of images to begin with
    number_files = len(pathNEF)
    print("Total Number of Images: ", number_files)

    # A List of Items
    items   = list(range(0, 57))
    l       = len(items)

    # Initial call to print 0% progress
    pgbar.printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 100)
        
    # loop trough the .nef files
    for path in pathNEF:
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite(exportDir + Path(path).name.replace('.NEF','.jpg'), rgb)
            count = count + 1
            
            pgbar.printProgressBar(count, number_files, prefix = 'Progress:', suffix = 'Complete', length = 100)

    subprocess.run([FILEBROWSER_PATH, os.path.normpath(exportDir)])

    print('\n')
    print('Finished all .NEF/.nef processing\nExiting...')        

if __name__ == '__main__':
    main()
