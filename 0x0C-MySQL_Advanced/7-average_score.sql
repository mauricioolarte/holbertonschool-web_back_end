-- script that creates a stored procedure ComputeAverageScoreForUser
-- computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT)
BEGIN
    DECLARE prom_score FLOAT;
    SET prom_score = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id=user_id);
    UPDATE users SET average_score = prom_score WHERE id=user_id;
END
//
DELIMITER ;
