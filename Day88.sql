/* YOUR QUERY GOES HERE
*/
SELECT
    CASE
        WHEN (A + B + C) > 0 THEN 'Positive'
        WHEN (A + B + C) < 0 THEN 'Negative'
        ELSE 'Zero'
    END AS A
FROM
    NUMBERS;
