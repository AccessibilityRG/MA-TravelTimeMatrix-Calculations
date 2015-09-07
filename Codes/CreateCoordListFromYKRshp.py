import geopandas as gdp
import fiona
from fiona.crs import from_epsg #currently useless!

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
        new['properties']['ID_orig'] = feature['properties'][col1]
        new['properties']['X_orig'] = feature['properties'][col2]
        new['properties']['Y_orig'] = feature['properties'][col3]
        
        yield new

# Execute method for input shapefile
GridCells = gdp.GeoDataFrame.from_features(getRecords(inputFile, "ID", "x", "y"))

#----------------------------------------------------------------------------
# Generate coordinate list (and shapefile)
#-----------------------------------------------------------------------------
#Write output text file:
outTxt =r"C:\HY-Data\VUOKKHEI\documents\MetropAccess\Matriisiajot\origPoints.txt"
header = ['ID_orig', 'X_orig', 'Y_orig']
GridCells.to_csv(outTxt, sep=";", index=False, columns=header)

### Optional: Write output shapefile:
##outShp =r"C:\HY-Data\VUOKKHEI\documents\MetropAccess\Matriisiajot\origPoints.shp"
##GridCells.to_file(outShp)










    



