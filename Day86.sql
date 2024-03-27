/* YOUR QUERY GOES HERE
*/
SELECT COUNT(*) AS A
FROM WORKERS
WHERE DailyWage * DaysWorked = (
    SELECT MAX(DailyWage * DaysWorked)
    FROM WORKERS
);
