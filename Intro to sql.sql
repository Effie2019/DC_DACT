#UNIQUE
SELECT DISTINCT role
FROM roles
#Learning to COUNT
SELECT COUNT(*)
FROM people;
#BETWEEN...AND... VS AND AND 
WHERE release_year BETWEEN 1990 AND 2000
#WHERE...IN VS OR OR 
WHERE language IN ('English', 'Spanish', 'French')
#NULL & IS NULL
WHERE language IS NULL
#LIKE & NOT LIKE
WHERE name NOT LIKE 'A%';

#SAMPLE
SELECT release_year,AVG(budget) AS avg_budget,AVG(gross) AS avg_gross
FROM films
WHERE release_year>1990
GROUP BY release_year
HAVING AVG(budget)>	60000000
ORDER BY AVG(gross)
LIMIT 5
