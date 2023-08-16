-- List all records with non-empty name fields
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
