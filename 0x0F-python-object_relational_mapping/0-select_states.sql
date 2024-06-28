-- Drop `states` table if it exists and recreate it
DROP TABLE IF EXISTS `states`;

-- Create the `states` table
CREATE TABLE `states` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
);

-- Insert initial data into `states` table
INSERT INTO `states` (`name`) VALUES
    ('California'),
    ('Arizona'),
    ('Texas'),
    ('New York'),
    ('Nevada');
