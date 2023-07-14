-- Create a stored procedure ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.
DELIMITER // ;
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
-- Calculate average score and update record in users table
UPDATE users
SET average_score = (
    SELECT SUM(projects.weight * score) / SUM(projects.weight)
    FROM corrections
    INNER JOIN projects
    ON projects.id = corrections.project_id
    WHERE corrections.user_id = user_id
)
WHERE id = user_id;

END //
DELIMITER ; //
