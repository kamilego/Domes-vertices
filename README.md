# Domes-vertices
Script that generates domes vertices with set radius and height.  
Used library pandas, math, numpy, xlsxwriter  
Used draft program AutoCAD 2D, Excel and SOFiSTiK Teddy.  
I was working on it since October 2020. Have put some changes during the time.   

This is a big part of my masters thisis where I had to compare domes including their forces and displacements under the influence of external force
First thing is to generate vertices in AutoCAD. I set units as meters and wanted to create vertices for domes which height and radius equals 1.0 meter. It is like a half of sphere R = 1.0m.  
In AutoCAD due dataextraction command I exported only vertices to xls file.
Using python I have created script that imports vertices from xls file, rotates them clockwise. 
User can also decide about domes dimentions like height, radius because default dimentions are 1.0m. Also material, profile section and value of force can be set too.  
The output program is SOFiSTiK Teddy which is script method to create constructions.  
Python creates new excel with prepared three teddy scripts which are ready to be copy and paste to odb file (default teddy extension file).

The biggest adventage? You can create certain dome with specific height and radius. It saves a lot of time.  
In my opinion script is more stable than other FEM programs like Autodesk ROBOT.  

# To use sript
Download script and xlsx files and paste to script excel paths

# Lamells dome gif
![Domes-vertices.gif](https://github.com/kamilego/Domes-vertices/blob/main/demo/Domes-vertices.gif)
