import geopandas as gdp
import fiona
from fiona.crs import from_epsg #currently useless!

# Generate coordinate lists from input shapefile (YKR GRID CELLS)
#   1. read shapefile
#   2. extract specified fields (ID; X; Y)
#   3. Rename columns
#   4. Save list file (.txt) sep=";"
#   5. Save shapefile [Under construction]

# Code was inspired by:
# http://gis.stackexchange.com/questions/129414/only-read-specific-attribute-columns-of-a-shapefile-with-geopandas-fiona

inputFile = "C:\HY-Data\VUOKKHEI\documents\MetropAccess\Matriisiajot\Matrix_13231cells_Buffer_1414cells.shp"
#MatrixShp = gdp.read_file(inputFile)

#---------------------------------------------------------------------------
# Extract fields (ID, x, y) from YKR grid shapefile
# and change column names (ID_orig, X_orig, Y_orig)
#---------------------------------------------------------------------------

# Method for reading ID, X and Y - information of the input YKR grid shapefile
# Give parameters in the same order( col1 = YKR ID, col2=x coordinate, col3 = y coordinate)!
def getRecords(filename,col1, col2, col3):
    Shp = fiona.open(inputFile)
    for feature in Shp:
        new = {}
        new['geometry'] = feature['geometry']  # not necessary for the coordinate list
        new['properties'] = {}
        new['properties']['ID'] = feature['properties'][col1]
        new['properties']['X'] = feature['properties'][col2]
        new['properties']['Y'] = feature['properties'][col3]
        
        yield new

# Execute method for input shapefile

OrigPoints = gdp.GeoDataFrame.from_features(getRecords(inputFile, "ID", "x", "y"))
OrigPoints = OrigPoints.rename(columns={'ID': 'ID_orig', 'X': 'X_orig', 'Y':'Y_orig'})

DestPoints = gdp.GeoDataFrame.from_features(getRecords(inputFile, "ID", "x", "y"))
DestPoints = DestPoints.rename(columns={'ID': 'ID_dest', 'X': 'X_dest', 'Y':'Y_dest'})

#----------------------------------------------------------------------------
# Generate coordinate list (and shapefile)
#-----------------------------------------------------------------------------

#Write output text file:
outTxt =r"C:\HY-Data\VUOKKHEI\documents\MetropAccess\Matriisiajot\OrigDestPoints\origPoints.txt"
header = ['ID_orig', 'X_orig', 'Y_orig']
OrigPoints.to_csv(outTxt, sep=";", index=False, columns=header)

#Write output text file:
outTxt =r"C:\HY-Data\VUOKKHEI\documents\MetropAccess\Matriisiajot\OrigDestPoints\destPoints.txt"
header = ['ID_dest', 'X_dest', 'Y_dest']
DestPoints.to_csv(outTxt, sep=";", index=False, columns=header)

### Optional: Write output shapefile:
##outShp =r"C:\HY-Data\VUOKKHEI\documents\MetropAccess\Matriisiajot\OrigDestPoints\origPoints.shp"
##GridCells.to_file(outShp)










    



