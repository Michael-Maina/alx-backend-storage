-- Create a stored procedure ComputeAverageScoreForUser
DELIMITER // ;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
-- Calculate average score and update record in users table
UPDATE users
SET average_score = (
    SELECT AVG(score)
    FROM corrections
    WHERE user_id = user_id
)
WHERE id = user_id;

END //
DELIMITER ; //
