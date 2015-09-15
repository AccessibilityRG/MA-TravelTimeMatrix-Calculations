# -*- coding: iso-8859-1 -*-

import arcpy
from arcpy import env
import sys, os, math

# This code reads a shapefile and splits it into smaller blocks. Block size is defined by the user.
# Each block is saved as a new shapefile.
# This code is setup for running via  ArcToolbox (4 input parameters). Compatible with ArcMap 10.2. (using python 2.7.5)

# Original Code by H. Tenkanen.

# Edits
#       Date:               Editor:                  Edits:
#-----------------      ---------------         --------------
#    2015-09-15         Vuokko Heikinheimo      Modified the code for Travel Time Matrix 2015 - purposes (filenames)
#                                               Documetation: Translated comments from Finnish to English. Refactored variables into English.


def ExDel(file): #overwrite-method
    if arcpy.Exists(file):
        arcpy.Delete_management(file)
def msg(Message): # message-method
    arcpy.AddMessage(Message)

#Pameters:
Data = arcpy.GetParameterAsText(0) #Input .shp-file
BlockSize = int(arcpy.GetParameterAsText(1)) #block size
OutputFolder = arcpy.GetParameterAsText(2) # output location (folder)
AsText = arcpy.GetParameterAsText(3) #True/False check box: option for creating text file (separator = ;)

temp = arcpy.GetSystemEnvironment("TEMP") #Define temp-folder for ArcGIS operations.
if AsText =='true':
    try:
        import dbfpy
        from dbfpy import dbf
    except:
        msg("You need to install 'dbfpy' -modul to write attribute-data to textfile!")
        msg("Download and install the module from: https://pypi.python.org/pypi/dbfpy/2.0.2")
        sys.exit()

i = 1
i3digit = "%03d" %i # 3-digit output

rows = float(arcpy.GetCount_management(Data).getOutput(0)) #number of rows; convert into floating point number!
Blocks = int(math.ceil(rows/BlockSize)) #Amount of Blocks, round up
FeatureName = "DataFeature" #Temp filename for feature layer
arcpy.MakeFeatureLayer_management(Data, FeatureName, "", temp, "")   #Creating a feature layer of the input records
FileName = OutputFolder + "\\" + i3digit + "_" + os.path.basename(Data)[:-4] + "_BlockSize" + str(BlockSize) + ".shp"  #Filename
ExDel(FileName)
LowerLimit=0
UpperLimit=BlockSize


for row in range(Blocks):

        
    RuleSyntax = "FID >=" + str(LowerLimit) + " AND " + "FID <" + str(UpperLimit)#Creating the rule
    arcpy.Select_analysis(FeatureName, FileName, RuleSyntax) # Select each row (record) one by one
    
    LowerLimit = LowerLimit + BlockSize # increasing the start index (alaraja) by the size of the block (lohkokoko)
    UpperLimit = UpperLimit + BlockSize #increasing the end index (Ylaraja) by the size of the block (lohkokoko)
    
    #If we wish to generate a text output..
    try:
        
        if AsText =='true':
            TekstiTulos = FileName[:-4] + ".txt"
            dbfData = FileName[:-4] + ".dbf"

            wf = open(TekstiTulos, 'w')
            db = dbf.Dbf(dbfData)

            wf.write("ID;x;y\n")
            text = ""

            #Creating a string variable
            for rec in db:
                text += "%s;%s;%s\n" % (rec['id'], rec['resolved_x'], rec['resolved_y'])

            #Write the string variable into the text file
            wf.write(text)

            #Closing the files
            db.close()
            wf.close()
    except:
        msg("Oops..Something wrong happened. TextFile was not produced.")
        pass
        
    
    text="Block " + str(i) + " finished"
    msg(text) #Message is printed after each block is finished.
    i += 1
    i3digit = "%03d" %i #3-digit number
    FileName = OutputFolder + "\\" + i3digit + "_" + os.path.basename(Data)[:-4]  + "_BlockSize" + str(BlockSize) + ".shp"
    ExDel(FileName)
    
