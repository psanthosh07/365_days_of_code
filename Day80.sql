/* YOUR QUERY GOES HERE 
*/
SELECT SUM(DISTINCT j.Salary) AS Salary
FROM Students s
JOIN Departments d ON s.DepartmentId = d.DepartmentId
JOIN Jobs j ON s.Id = j.Id
WHERE d.DepartmentName = 'CSE'
GROUP BY d.DepartmentName
ORDER BY d.DepartmentName;
