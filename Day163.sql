SELECT reviewers.reviewer_name
FROM reviewers
JOIN ratings ON reviewers.reviewer_id = ratings.reviewer_id
WHERE ratings.reviewer_stars IS NULL;
