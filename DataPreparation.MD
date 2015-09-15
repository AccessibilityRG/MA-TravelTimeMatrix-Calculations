# DATA PREPARATION 

### Origins and destinations for Reititin (public transportation)

1. Selected grid cells that cover the matrix extent
2. Generated a 1 km buffer zone around the matrix extent (excluding water areas) [see image: Matrix + Buffer zone] (Figures/MatrixExtentAndExtraCells_SeaExcluded.png)
3. Generated coordinate list for all analysis points [code for generating coordinate lists from YKR grid shapefile] (Codes/CreateCoordListFromYKRshp.py
4. Parsed the origin points into blocks, this step is embedded in the [code for generating batch-files] (Codes/Take_subsets_from_coordList_and_Create_batch_file.py)



### Origins and destinations for MetropAccess Digiroad Tool (car travel times)

1. Created a point shapefile from the Travel Time Matrix analysis grid cells [see image: Matrix + Buffer zone] (Figures/MatrixExtentAndExtraCells_SeaExcluded.png)
2. Split the point shapefile into blocks. [Code for splitting the shapefile] (Codes/Arcpy_SplitShapeFile.py)