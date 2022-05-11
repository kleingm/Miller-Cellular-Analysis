# <center> <ins> Cellular Analysis Research </ins> </center>

<center> <figure> 
    <img src="./Saved Images/cell_image.PNG"
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

# <a name="main-programs"></a>Main Programs:
* Cell_Area_Perimeter.py
* t_testing.py
* write_stats.py

# <a name="how-to-use:"></a>How To Use:
<p> <strong> Step #1: </strong> Run ImageJ to get data from a cell movie.
The ImageJ Process is listed [here.](ReadMeImageJ.pdf) </p>

<p> <strong> Step #2: </strong> Load the "Cell_Area_Perimeter.py" program
and run it. Two prompts will pop up. The first will ask you to choose a file
to use for analysis. The second will be to save the new generated file. Save 
the file as whatever name you would like. For example: processed_data.
No need to add .csv to the end of it, as the program will do that for you.</p>

<p> <strong> Step #3: </strong> Check to see that your generated file exists,
and has the format of the first row being labels, second row being data. Make
sure these values seem reasonable.</p>

<p> <strong> Step #4: </strong> After generating two new files from 
Cell_Area_Perimeter program, open up "t_testing.py".</p>

<p> <strong> Step #5: </strong> Run "t_testing.py". Each prompt will be 
for the processed data you generated. Select one on the first pop-up, and
the second on the second pop-up. The code will then execute.</p>

<p> <strong> Step #6: </strong> The program will generate two plots 
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

<p> <strong> How to recreate this image: </strong> <br>
Run the Cell_Area_Perimeter Program and select "miller_results.csv"
from the Raw CSV folder. Save the output as Miller_Processed
to wherever you'd like. Run the same program again, choose the same 
file, but name it Miller_Copy. </p>

<p>Next, load up the t_testing program and run that. When 
prompted, select first the "Miller_Processed.csv" file, and 
on the next prompt select the "Miller_Copy.csv" file. That
will generate the image as depicted above.</p>


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

<p> For quality of life, the team could look into command-line
arguments to make the entire process run through with one click.
Possible updates to come with this. </p>