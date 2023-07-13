-- Create the stored procedure AddBonus
DELIMITER // ;
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
 -- Check if the project already exists in the projects table
  SET @project_id := (SELECT id FROM projects WHERE name = project_name);

  -- If the project does not exist, create a new entry in the projects table
  IF @project_id IS NULL THEN
    INSERT INTO projects (name) VALUES (project_name);
    SET @project_id := LAST_INSERT_ID();
  END IF;

   -- Insert the correction into the corrections table
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @project_id, score);
  END //
  DELIMITER ; //
