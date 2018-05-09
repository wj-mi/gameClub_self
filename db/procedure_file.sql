
/* create_game_club*/
DELIMITER &&
DROP PROCEDURE IF EXISTS games.create_game_club;
CREATE DEFINER=`root`@`%` PROCEDURE `create_game_club`(
	IN _creator_id  INT,
    IN _create_time INT,
    IN _club_uuid  INT,
    IN _player_num  INT,
    IN _club_name INT,
    IN _game_type VARCHAR(50)
)
BEGIN
	DECLARE room_id INT(11) DEFAULT -1;
    START TRANSACTION;
	INSERT INTO game_club (
		uuid, name, max_person, chairman, game_types, create_time
    )
    VALUES (
		_club_uuid, _club_name, _player_num, _creator_id, _game_type, _create_time
    );
	COMMIT;

END;
DELIMITER ;