-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema thoughts_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `thoughts_schema` ;

-- -----------------------------------------------------
-- Schema thoughts_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `thoughts_schema` DEFAULT CHARACTER SET utf8 ;
USE `thoughts_schema` ;

-- -----------------------------------------------------
-- Table `thoughts_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `thoughts_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `form_first_name` VARCHAR(45) NULL,
  `form_last_name` VARCHAR(45) NULL,
  `form_email` VARCHAR(45) NULL,
  `form_password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT Now() ON UPDATE Now(),
  `updated_at` DATETIME NULL DEFAULT Now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `thoughts_schema`.`thoughts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `thoughts_schema`.`thoughts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NULL,
  `user_post` VARCHAR(45) NULL,
  `other_user_post` VARCHAR(45) NULL DEFAULT 'Now()',
  `created_at` VARCHAR(45) NULL DEFAULT 'Now() ON UPDATE Now()',
  `poster_id` INT NOT NULL,
  `other_users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_thoughts_users_idx` (`poster_id` ASC) VISIBLE,
  INDEX `fk_thoughts_users1_idx` (`other_users_id` ASC) VISIBLE,
  CONSTRAINT `fk_thoughts_users`
    FOREIGN KEY (`poster_id`)
    REFERENCES `thoughts_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_thoughts_users1`
    FOREIGN KEY (`other_users_id`)
    REFERENCES `thoughts_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
