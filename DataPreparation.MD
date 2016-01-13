# DATA PREPARATION 

#### MATRIX:
- Extracted Matix grid cells from the whole YKR grid (13231 250m x 250 grid cells, original file: T11_gre_e_250m)
- All grid cells have the following information content: YKR-ID, x-coordinate and y-coordinate 
- CRS of the original data is EPSG:3067 (ETRS-TM35FIN coordinates)
- Additional 1 km buffer was used in the runs, the extra cells have removed from the outputs 
- [Figure: Matrix + Buffer zone] (Figures/MatrixExtentAndExtraCells_SeaExcluded.png)


#### PUBLIC TRANSPORT (PT): 
###### SCHEDULES
- Public transport schedules from Helsinki Region transport (Helsingin Seudun Liikenne HSL): [Kalkati.net, XML database dump](http://developer.reittiopas.fi/pages/fi/kalkati.net-xml-database-dump.php?lang=FI) 
- Schedules for Monday 07.09.2015 that can be found in the Kalkati dataset between the dates 2015-08-19 and 2015-09-18 were used in the calculations. 
- The Kalkati data was processed ("builded") into a Reititin-compatible format. 
- Processed file can be downloaded from [this folder](http://www.helsinki.fi/science/accessibility/data/Kalkati-data/).
- Direct download link: [kalkati_2015-08-19_2015-09-18.tar.gz]	(www.helsinki.fi/science/accessibility/data/Kalkati-data/kalkati_2015-08-19_2015-09-18.tar.gz)

###### ORIGINS AND DESTINATIONS
- Retrieved Origin and destination points from the YKR grid data, 
- Outputs were stored as text files (293 subsets for origin points, destination points as one list) 
- Open streetmap -data in a reititin-compatibe format (same data set that was used with the first Travel Time Matrix)
- Squares were added around new train stations around the ring rail line to allow pedestrian movements: [bounding box definitions] (KehRataAukiot.md)


#### CAR: 
###### ROAD NETWORK
- Digiroad 2015 (K) for 01_Uusimaa_1 , 01_Uusimaa_2 and 20_ita-Uusimaa were downloaded from Paituli
- The three different parts (01_Uusimaa_1 , 01_Uusimaa_2, 20_ita-Uusimaa) were combined.
- The road network was clipped around the analysis extent ([Figure: Digiroad 2015 extent for the analysis] (Figures/Digiroad.png)).
- The network dataset was pre-processed using MetropAccess-Digiroad_ArcGIS_10.1. - step 3 (Vaihe3_AikasakkojenLaskenta.py in the Reititin-tool) before the actual travel-time calculations (step 4 in Reititin).

###### CAR ORIGINS AND DESTINATIONS
- origins and destinations were saved as shapefiles, (293 subsets for origin points, destination points as one shapefile)





