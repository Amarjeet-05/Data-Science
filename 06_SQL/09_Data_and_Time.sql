-- Function				Returns				Example Output
-- CURRENT_DATE			Date only			2025-05-02
-- CURRENT_TIME			Time only			14:23:45
-- NOW()				Date and time		2025-05-02 14:23:45
-- CURRENT_TIMESTAMP	Date and time		2025-05-02 14:23:45
-- LOCALTIME			Date and time		2025-05-02 14:23:45


-- now() and current_timestamp() function are giving data and time of the server side.

UPDATE std_data SET adm_date = current_date();
SELECT * FROM std_data;