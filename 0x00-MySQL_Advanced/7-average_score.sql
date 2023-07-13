-- Create a stored procedure ComputeAverageScoreForUser
DELIMITER // ;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
-- Calculate average score
SET @ave_score := (SELECT AVG(score) FROM corrections WHERE user_id = user_id);

-- Update record in users table
UPDATE users
SET average_score = @ave_score
WHERE id = user_id;
END //
DELIMITER ; //
