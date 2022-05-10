# <center> <ins> Cellular Analysis Research </ins> </center>

<center> <figure> 
    <img src="./Saved Images/cell_image.png"
         alt="Comparison"
    width="500" height="300">
</figure> </center>

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
* MatPlotLib (3.5.1)
* SciPy (1.8.0)
* NumPy (1.22.1)
* Tkinter
* easygui (0.98.3)

# <a name="main-programs"></a>Main Programs:
* Cell Area Perimeter
* t_testing

# <a name="how-to-use:"></a>How To Use:
<p> <strong> Step #1: </strong> Load Data you want to process in the Raw CSV
folder located in the data folder. </p>

<p> <strong> Step #2: </strong> Load the 'Cell_Area_Perimeter.py' file, go to
lines 82 and 85, and edit the input file name and what you
would like to name the outgoing file.</p>

<p> <strong> Step #3: </strong> Run the 'Cell_Area_Perimeter' code. This will
automatically write a CSV containing statistics about the
input sample to the Processed Data folder. </p>

<p> <strong> Step #4: </strong> Verify that the file was written. You can open
up the file to make sure that it has relevant data about the
samples mean area and mean perimeter.</p>

<p> <strong> Step #5: </strong> Open up 't_testing.py' and go to lines 79 and
80. Select the two samples you would like to compare against
each other. Make sure that the samples have been processed,
and use the exact filename without the .csv at the end.</p>

<p> <strong> Step #6: </strong> Run the file. This will generate two plots 
comparing the area mean and perimeter means of the two 
samples, and denote if their means are different or not.
Plots without an asterisk are statistically insignificant,
while those with asterisks are statistically significant.</p>

<p> <strong> Step #7: </strong> Save the plots as they are 
generated using the Save icon on the plot popup.</p>

# <a name="sample-results:"></a>Sample Results:

<figure>
    <img src="./Saved Images/same_same.png"
         alt="Comparison">
    <figcaption> <center> <em> <strong> Figure 1: 
</strong> Comparison of two data sets with the same mean and
standard deviation. </em> </center> </figcaption>
</figure>

# <a name="limitations:"></a>Limitations:
In order for the programs to run effectively, the data
that is output from ImageJ must stay in the same form 
that it was delivered. Any alterations to the printed CSV
could result in the file not being able to be read by the
Cell_Area_Perimeter program. <br>

In addition to this, when choosing the files to be
compared in the t_testing program, the filenames are
case-sensitive, and work only if the file is present in
the "Processed Data" sub-folder. Otherwise, the program
will not have the correct filepath and will not run.

# <a name="for-the-future:"></a>For The Future:
<p> One addition that the team can see being valuable for the
future would be the ability to run multiple t-tests at
once, in the form of a Two-Way ANOVA test. That would 
allow the user to compare multiple samples all at the 
same time. </p>

<p> Another task the team could look into would be mapping out
an entire cell movie into a line graph with error bars to
be able to visualize how the areas or perimeters change 
over time. This would work as an entirely separate process
from the t-tests, and would need more time to fully flesh 
out.</p>
