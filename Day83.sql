/* YOUR QUERY GOES HERE
*/
SELECT  
    CONCAT(Role, ' Count is ', COUNT(*)) AS Count
FROM GAMERS
GROUP BY Role
ORDER BY COUNT(*) ASC;
