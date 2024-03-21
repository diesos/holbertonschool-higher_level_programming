-- This query is used to find the highest score of the second table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;