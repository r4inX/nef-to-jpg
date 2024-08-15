# nef-to-jpg
I forked this repo to add better user-experience and maybe make the process faster. Since it took ~10min for 1.9K files.

## Whats different from the original repo?

- added a folder-select dialog so the directory is easier accessible
- added a progressbar for better visualisation of the process
- .nef Files will get renamed to .NEF so that there is only 1 loop in the code
- bloated the shit out of this script lmao

## Original below

This Python script converts an entire directory containing nef images to jpg. 

To install the requirements using pip:
```shell
cd photoconverter
pip install -r requirements.txt
```

In the script, be sure to change '/path/to' to the absolute path of the folder where the images are located.  

## Time
Here are a few estimated times depending on your number of images.

<p align="center">
<img width="482" alt="Screen Shot 2022-07-29 at 8 28 30 AM" src="https://user-images.githubusercontent.com/98404383/181758584-65a31437-efaf-430d-9178-a8e57ebe11be.png">
</p>

If the program is interrupted, don't worry. While you'll have to run it from the beginning again, it will simply overwrite the new images already processed. It won't make any duplicates. 

Your original files will remain and the quality will not change. No previous data will be deleted or overwritten by using this program. 

I will try to include a few sample images that I find online here as well :) 
