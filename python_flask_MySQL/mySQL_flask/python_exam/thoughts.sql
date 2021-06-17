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
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `thoughts_schema`.`thoughts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `thoughts_schema`.`thoughts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` VARCHAR(45) NULL DEFAULT 'Now() ON UPDATE Now()',
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_thoughts_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_thoughts_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `thoughts_schema`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `thoughts_schema`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `thoughts_schema`.`likes` (
  `users_id` INT NOT NULL,
  `thoughts_id` INT NOT NULL,
  PRIMARY KEY (`users_id`, `thoughts_id`),
  INDEX `fk_users_has_thoughts_thoughts1_idx` (`thoughts_id` ASC) VISIBLE,
  INDEX `fk_users_has_thoughts_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_thoughts_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `thoughts_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_thoughts_thoughts1`
    FOREIGN KEY (`thoughts_id`)
    REFERENCES `thoughts_schema`.`thoughts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
