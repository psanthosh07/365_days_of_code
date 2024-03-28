/* YOUR QUERY GOES HERE
*/
SELECT SQRT(
        POW(MAX(XCoordinate) - MIN(XCoordinate), 2) + 
        POW(MAX(YCoordinate) - MIN(YCoordinate), 2)
    ) AS A
FROM HOUSES;
