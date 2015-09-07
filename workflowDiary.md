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