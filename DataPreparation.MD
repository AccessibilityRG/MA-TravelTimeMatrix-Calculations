# DATA PREPARATION 

#### MATRIX:
- 13231 grid cells with YKR-ID, x-coordinate and y-coordinate [Matrix + Buffer zone] (Figures/MatrixExtentAndExtraCells_SeaExcluded.png)
- Additional 1 km buffer was used in the runs, the extra cells have removed from the outputs 



#### PUBLIC TRANSPORT: 
- origin and destination points listed as text files (293 subsets for origin points, destination points as one list) 
- Open streetmap -data in a reititin-compatibe format
- Squares were added around new train stations around the ring rail line: [bounding box definitions] (KehRataAukiot.md)



#### CAR: 
- origins and destinations (YKR grid cells)as shapefiles, (293 subsets for origin points, destination points as one shapefile)
- Digiroad (K): the road network was combined from three different parts (01_Uusimaa_1 , 01_Uusimaa_2, 20_ita-Uusimaa and clipped around the analysis extent: [Digiroad 2015] (Figures/Digiroad.png)

