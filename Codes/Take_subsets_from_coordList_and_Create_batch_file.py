import pandas as pd
import os

# Under construction...
# Code developed based on Henrikki's original.

# Insert version (year)
version = "2015"

#Read input points from text file:
origins = r"C:\HY-Data\VUOKKHEI\documents\MetropAccess\Matriisiajot\OrigDestPoints\origPoints.txt"
data = pd.read_csv(origins, sep=';')

#Set output folder and base for output filename for point list:
outFolder = r"C:\HY-Data\VUOKKHEI\documents\MetropAccess\Matriisiajot\MetropAccess-Reititin_1.2\MetropAccess-Reititin_1.2\MetropAccess-Reititin\bin\OrigDestPoints"
filename = "_TravelTimeMatrix2015_OriginPoints_ETRSTM35FIN.txt"

#Kalkati path:
#kalkati_folder = r"C:\HY-Data\VUOKKHEI\documents\MetropAccess\Reititin\Kalkatijemma\kalkati-2015-07-23"

#Output folder name for the Reititin-runs (the folder name is concatenated within the batch files).
result_folder = "TravelTimeMatrix%s_results" %version


#-----------------------------------------
# Dividing the origin points into blocks 
#-----------------------------------------

# Determine block size
block_size = 250
row_count = float(len(data))
iterations = int(row_count / block_size + 1)

i = 0
name_idx = 0

for block in range(iterations):
    try:
        block_data = data[i:i+block_size]
    except:
        block_data = data[i:]

    outName = os.path.join(outFolder, "%03d%s" % (name_idx, filename))
    block_data.to_csv(outName, sep=';', index=False)
    i+=block_size
    name_idx+=1

#-----------------------------
# Create Reititin commands
#------------------------------

file_paths = []
cmd_file = "run_batch_TravelTimeMatrix_%s.txt" %version
batch_folder = r"C:\HY-Data\VUOKKHEI\documents\MetropAccess\Matriisiajot\MetropAccess-Reititin_1.2\MetropAccess-Reititin_1.2\MetropAccess-Reititin\bin\BatchFiles"
f = open(os.path.join(batch_folder, cmd_file), 'w')

command1 = "route.bat"
command2 = "OrigDestPoints\destPoints.txt "
#command3 = "--base-path=%s" % kalkati_folder
out_command = ""
i = 1

for root, dirs, files in os.walk(outFolder):
    for filename in files:

        command3 = "--out-avg=%s/%03d_TravelTimeMatrix_%s_results.txt " % (result_folder,i, version)
                    # note! The "%03d" % (i)  -combination generates 3-gidit running numbers 

        out_command += "%s OrigDestPoints/%s %s %s \n" % (command1, filename, command2, command3)

        i+=1

f.write(out_command[:-2])
f.close()

#-------------------------------------
# Parse the commands into .bat files
#-------------------------------------

allCommands=open(os.path.join(batch_folder, cmd_file), 'r')

batch_file = "run_batch_TravelTimeMatrix_%s.bat" %version

batch = allCommands.readlines()

# Determine block size
block_size = 2
row_count = float(len(batch))
iterations = int(row_count / block_size + 1)

i = 0
name_idx = 0

for block in range(iterations):
    try:
        block_data = batch[i:i+block_size]
    except:
        block_data = batch[i:]

    syntax = "".join(block_data)
    syntax = syntax.replace("\n", "&&") # If we wish to separate the commands with "&&" in stead of "\n"

    outName = os.path.join(batch_folder, "%03d%s%s" % (name_idx,"_", batch_file))
    f=open(outName, "w")
    f.write(syntax)
    f.close
    
    i+=block_size
    name_idx+=1
    

