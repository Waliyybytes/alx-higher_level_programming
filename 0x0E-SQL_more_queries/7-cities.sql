-- script that creates database and table in a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	FOREIGN KEY (state_id)
	    REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
