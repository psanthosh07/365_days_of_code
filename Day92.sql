SELECT 
    CONCAT_WS(',', s.Name, COALESCE(j.Date, '')) AS Offers
FROM 
    Students s
JOIN 
    Departments d ON s.DepartmentId = d.DepartmentId
JOIN 
    Jobs j ON s.Id = j.Id
ORDER BY 
    d.DepartmentName;
