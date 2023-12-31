-- Create a trigger that resets the attribute valid_email only when the email has been changed
DELIMITER //
CREATE TRIGGER email_validation
FOR EACH ROW
BEFORE UPDATE ON users
BEGIN
	IF NEW.email != OLD.email THEN
	   SET.valid_email = 0;
	END IF
END//

DELIMITER ; //
