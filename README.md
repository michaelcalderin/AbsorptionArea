##ABOUT

This program allows the user to find the area under a curve. It is designed specifically for
finding the area under absorption spectra from Infrared Spectroscopy. It uses a left Riemann sum
to calculate area. It has been used to analyze HCl and DCl. 

##OPERATING SYSTEM

This program is intended for 64 bit macOS or 64 bit Windows. Area_Mac and Area_Mac being 
2 versions depending on your operating system.

##DISTRIBUTION

If you try downloading or sending the program, be aware that it might be marked as 
malware. This issue was seen when trying to share through Google Drive. Refer to "Malware Issue"
file to read more about opening the executable when your computer flags it as untrusted.

##BOOTING UP

The application (Area_Mac or Area_Windows) will be found in the same folder as _internal. 
_internal holds all the necessary libraries and files needed for the program to run. The application
and _internal must always remain in the same folder or else the application will not be able to
find/read the files it needs. However, if you wish, you can create a shortcut of the application
and place that shortcut in any directory that you wish. The program can then run from that shortcut.

When you launch the application, you will see a window requesting for a .csv file. The structure of the file
should have 2 columns (x, y) where x is the independent variable and y is the dependent variable to be graphed.
The first 2 lines will be ignored by the program because it assumes that those lines will be labels and not data points.
Refer to DCL_Sample.csv as an example.

The program will ask for the path of that file. On Windows this may look like C:/…/DCL_Sample.csv. You can usually
find the path on Windows by right clicking the csv file and clicking “copy path name” or something similar. On some
Windows devices this might not be an option and you could instead right click the file and go to Properties. Note that
Windows tends to add quotation marks to the path name: “C:/…/DCL_Sample.csv”. Make sure you remove these 
quotation marks. Also, make sure the path ends with the name of the file (/DCL_Sample.csv).

After you have entered the path into the program, click the Confirm button and you should see a new window open
with instructions on how to proceed. If you see error messages or nothing pops up, there is a high chance that you
did not put in the path correctly. It could be something as simple as .csv at the end was needed or .csv needed to be 
removed. It could also be that you provided a relative path instead of an absolute path. 

##SCROLLING FEATURE

When you get to a screen where you see a plot, you can use your scroll wheel or track pad to zoom in/out.
It might come in handy. 

##TESTING

Due to time constraints, the program has not been extensively tested so bugs are bound to occur. It is advised to
closely follow the instructions and suggestions provided.

##CONTRIBUTIONS

The source code is provided and named Area.py. Feel free to make improvements. A nice change would be to fit the
absorption peak to a gaussian curve and find the area under that curve using the integral instead of Riemann sum.

#CONTACT

This was developed by Michael Calderin on November 30, 2023. For questions, you may email michaelcalderin17@gmail.com.
