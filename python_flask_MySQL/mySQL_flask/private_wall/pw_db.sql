-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema private_wall
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema private_wall
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `private_wall` DEFAULT CHARACTER SET utf8 ;
USE `private_wall` ;

-- -----------------------------------------------------
-- Table `private_wall`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `private_wall`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `form_first_name` VARCHAR(45) NULL,
  `form_last_name` VARCHAR(45) NULL,
  `form_password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT Now(),
  `updated_at` DATETIME NULL DEFAULT Now() ON UPDATE Now(),
  `form_email` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `private_wall`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `private_wall`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` TEXT NULL,
  `created_at` VARCHAR(45) NULL DEFAULT 'Now()',
  `updated_at` VARCHAR(45) NULL DEFAULT 'Now() ON UPDATE Now()',
  `sender_id` INT NOT NULL,
  `receiver_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users_idx` (`sender_id` ASC) VISIBLE,
  INDEX `fk_messages_users1_idx` (`receiver_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`sender_id`)
    REFERENCES `private_wall`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_users1`
    FOREIGN KEY (`receiver_id`)
    REFERENCES `private_wall`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
