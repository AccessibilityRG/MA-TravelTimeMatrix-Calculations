### 3.9.2015
VH:
- Planning session for the Travel Time Matrix runs, autumn 2015 [See the Planning document] (Planning.md)


- Downloaded Digiroad 2015 (K) for 01_Uusimaa_1 , 01_Uusimaa_2 and 20_ita-Uusimaa from Paituli


- Extracted Matix grid cells from the whole YKR grid (T11_gre_e_250m that was found under Aineistot\YKR\ETRS_TM35FIN_koordinaatisto\Ruudut\250m) --> 2014 version??? Should be the same as always..
- generated 1km buffer zone around the matrix extent and selected extra grid cells for the analysis: [see image] (Figures/MatrixExtentAndExtraCells.png)
- Merged the matrix grid cells and the extra cells (total number of grid cells=16085)
- Generated a list of YKR ID's (for the matrix, for the extra cells, and all together)



### 3.9.2015

Still to do with the grid: 


-remove water areas from the buffer zone
- create list files

### 7.9.2015

- Created the final buffer zone (1414 extra grids): Excluded buffer cells that overlap with water areas.
- See final extent for the analysis grid [Matrix + Buffer zone] (Figures/MatrixExtentAndExtraCells_SeaExcluded.png)
- Genetarting list files with the fields YKR_ID; X; Y. [See code] (Codes/CreateCoordListFromYKRshp.py)
- CRS of the original data is EPSG:3067 (ETRS-TM35FIN coordinates)
- Worked with the code that generates batch files [see code] (Codes/Take_subsets_from_coordList_and_Create_batch_file.py)
- The batch file generator code requires still some adjustments!



### 11.9.2015

- Quick check with Henkka & Vuokko on the status
- Note: no need for basepath-command in the syntax, the correct kalkati will be used as the default.


### 15.9.2015


- Fixed the [Batchfilemaker-Code] so that each file begins with a 3-digit running number (Codes/Take_subsets_from_coordList_and_Create_batch_file.py)
- Parsing the orig/dest points for car runs (shapefile into blocks) modified [existing python + arcpy code](Codes/Arcpy_SplitShapeFile.py)
- With current settings (BlockSize=120) there are 123 output shapefiles, last of them has only 5 records (edge of the buffer).


### 16.9.2015

- Checking the files
- Henkka updated the Kalkati distribution http://www.helsinki.fi/science/accessibility/data/Kalkati-data/


### 22.9.
- Henkka has been testint the runs on taito
- still reconsidering to change the kalkati new ones available for the gorup: P:\h510\metropaccess\Aineistot\Kalkati-data\Kalkati-Buildatut



### 23.9.

-Testing the routing results. 
- Fixed squares around Kivistö and Vehkala train stations
- Modified enter mode cost so that the process favors trains over buses

        // Cost of entering different modes of transit, in minutes.
        enterModeCost:  {
                                1:      3,
                                6:      1,
                                12:     3,
                                dummy:0
                        }, 
                        
                        
####tests and fixes for the reititin - runs
1. Test runs were made for a subset of origins and destinations. 
2. Coparison of new results against Travel Time Matrix 2013 --> big differences?
3. Further inspection was done for areas where there is a transition from but to train on the ring rail (Travel times in seutula were significantly slower than before)
4. Added Squares around railway stations along the ring rail line, using http://boundingbox.klokantech.com/ -tool.
Fix 1: Checked Reititin settings for transport mode prioritization: how different modes of transport are prioritized? --> prioritzing train over bus resulted in more realistic routes and travel times.
Fix 2: Adding the Squares to the area list in task.js -file resulted in more realistic routes