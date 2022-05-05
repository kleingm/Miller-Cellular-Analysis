# Cellular Analysis Research
> The purpose of this project is to aid in the processing
> of cell data for Dr. Callie Miller's research. Included
> in this repo are programs that parse through raw data
> given from ImageJ, which can then be used to compare the
> mean area and mean perimeter of two different samples.
<hr>

# <a name="team-members"></a>Team Members:
* Patrick Foreman <foremapr@dukes.jmu.edu>
* Grace Klein <kleingm@dukes.jmu.edu>
* Ritavash Chowdhury <chowd2rx@dukes.jmu.edu>

# <a name="required-plugins"></a>Required Plugins:
* MatPlotLib
* SciPy
* NumPy

# <a name="how-to-use:"></a>How To Use:
<p> Step #1: Load Data you want to process in the Raw CSV
folder located in the data folder. </p>

<p> Step #2: Load the 'Cell_Area_Perimeter.py' file, go to
lines 82 and 85, and edit the input file name and what you
would like to name the outgoing file.</p>

<p> Step #3: Run the 'Cell_Area_Perimeter' code. This will
automatically write a CSV containing statistics about the
input sample to the Processed Data folder. </p>

<p> Step #4: Verify that the file was written. You can open
up the file to make sure that it has relevant data about the
samples mean area and mean perimeter.</p>

<p> Step #5: Open up 't_testing.py' and go to lines 79 and
80. Select the two samples you would like to compare against
each other. Make sure that the samples have been processed,
and use the exact filename without the .csv at the end.</p>

<p> Step #6: Run the file. This will generate two plots 
comparing the area mean and perimeter means of the two 
samples, and denote if their means are different or not.
Plots without an asterisk are statistically insignificant,
while those with asterisks are statistically significant.</p>

<p> Optional Step #7: Save the plots as they are 
generated using the Save icon on the plot popup.</p>

