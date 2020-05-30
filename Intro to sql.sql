--C1：SQL Intro
--(1)Unique
  SELECT DISTINCT role
  FROM roles
--(2)Agg
  SELECT COUNT(*)
  FROM people;
--(3)BETWEEN...AND... VS. AND...AND... 
  WHERE release_year BETWEEN 1990 AND 2000
--(4)WHERE...IN VS. OR...OR... 
  WHERE language IN ('English', 'Spanish', 'French')
--(5)NULL & IS NULL
  WHERE language IS NULL
--(6)LIKE & NOT LIKE
  WHERE name NOT LIKE 'A%';
--(7)Other basics
  SELECT release_year,AVG(budget) AS avg_budget,AVG(gross) AS avg_gross
  FROM films
  WHERE release_year>1990
  GROUP BY release_year
  HAVING AVG(budget)>	60000000
  ORDER BY AVG(gross)
  LIMIT 5
  
--C2: Joining Data in SQL
--1.Inner Join
--(1)Select...From
  SELECT cities.name AS city, countries.name AS country,region
  FROM cities
  INNER JOIN countries
  ON cities.country_code = countries.code;#or USING(code) \*row 增多是因为有重复值
--(2)Self Join #可以用来细分column
  SELECT p1.country_code, p1.size AS size2010, p2.size AS size2015
  FROM populations AS p1
  INNER JOIN populations AS p2
  USING(country_code)
--(3)CASE...WHEN
  SELECT name, continent, code, surface_area,
      CASE WHEN surface_area > 2000000 THEN 'large'
          WHEN surface_area BETWEEN 350000 AND 2000000  THEN 'medium'
          ELSE 'small' END
          AS geosize_group
  FROM countries;
  WHERE year = 2015;
--2.Outer Join
--(1)LEFT join
--(2)Right join
--(3)Full join
--3.CROSS JOIN 
SELECT c.name AS city, l.name AS language
FROM cities AS c        
  CROSS JOIN languages AS l */Do not need ON condition
WHERE c.name like 'Hyder%';
--4.Set theory clauses
--(1)UNION & UNION ALL
SELECT code, year
  FROM economies
	UNION ALL
SELECT country_code, year
  FROM populations
ORDER BY code, year;
--(2)INTERSECT&	EXCEPT
SELECT name 
  From countries
	INTERSECT
SELECT name 
  From cities;
--(3)Semi-Join
SELECT DISTINCT name
  FROM languages
WHERE code IN
  (SELECT code
   FROM countries
  WHERE region='Middle East')
--(4)Anti-Join
SELECT code,name
  FROM countries
  WHERE continent='Oceania'
  	AND code NOT IN
  (SELECT code FROM currencies);
--5.Subqueries
--(1)Subquery inside where
 SELECT name, country_code, urbanarea_pop
  FROM cities
Where name IN
  (SELECT capital
   FROM countries)
ORDER BY urbanarea_pop DESC;
--(2)Subquery inside select
  (SELECT COUNT(*)
   FROM cities
   WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;
--(3)Subquery inside from
SELECT local_name, subquery.lang_num
  FROM countries,
  	(SELECT code, COUNT(*) AS lang_num
  	 FROM languages
  	 GROUP BY code) 
  	 AS subquery
  WHERE countries.code=subquery.code
ORDER BY lang_num desc
;
