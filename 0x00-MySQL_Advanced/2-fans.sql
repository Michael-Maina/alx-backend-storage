-- Create a temporary table to store the aggregated fan counts by country
CREATE TEMPORARY TABLE temp_fan_counts AS
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin;

-- Rank the country origins based on the total number of fans
SELECT origin, nb_fans
FROM temp_fan_counts
ORDER BY nb_fans DESC;
