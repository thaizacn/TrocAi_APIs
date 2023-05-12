-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema trocai
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema trocai
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `trocai` ;
USE `trocai` ;

-- -----------------------------------------------------
-- Table `trocai`.`usuarios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `trocai`.`usuarios` ;

CREATE TABLE IF NOT EXISTS `trocai`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(20) NOT NULL,
  `imagem` BLOB NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocai`.`itens`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `trocai`.`itens` ;

CREATE TABLE IF NOT EXISTS `trocai`.`itens` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `item` VARCHAR(50) NOT NULL,
  `descricao` VARCHAR(255) NOT NULL,
  `data_entrada` DATE NOT NULL,
  `id_usuario` INT NOT NULL,
  `imagem` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_itens_1_idx` (`id_usuario` ASC),
  CONSTRAINT `fk_itens_1`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `trocai`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocai`.`operacoes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `trocai`.`operacoes` ;

CREATE TABLE IF NOT EXISTS `trocai`.`operacoes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_item` INT NOT NULL,
  `id_item_2` INT NULL,
  `data_e_hora` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_operacoes_1_idx` (`id_item` ASC),
  INDEX `fk_operacoes_2_idx` (`id_item_2` ASC),
  CONSTRAINT `fk_operacoes_1`
    FOREIGN KEY (`id_item`)
    REFERENCES `trocai`.`itens` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_operacoes_2`
    FOREIGN KEY (`id_item_2`)
    REFERENCES `trocai`.`itens` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocai`.`avaliacoes_operacao`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `trocai`.`avaliacoes_operacao` ;

CREATE TABLE IF NOT EXISTS `trocai`.`avaliacoes_operacao` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comentario` VARCHAR(255) NULL,
  `nota` INT NOT NULL,
  `id_operacao` INT NOT NULL,
  `id_usuario` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_avaliacoes_operacao_1_idx` (`id_operacao` ASC),
  INDEX `fk_avaliacoes_operacao_2_idx` (`id_usuario` ASC),
  CONSTRAINT `fk_avaliacoes_operacao_1`
    FOREIGN KEY (`id_operacao`)
    REFERENCES `trocai`.`operacoes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_avaliacoes_operacao_2`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `trocai`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocai`.`mensagens`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `trocai`.`mensagens` ;

CREATE TABLE IF NOT EXISTS `trocai`.`mensagens` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `conteudo` VARCHAR(1000) NOT NULL,
  `id_remetente` INT NOT NULL,
  `id_destinatario` INT NOT NULL,
  `data_envio` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_mensagens_1_idx` (`id_remetente` ASC),
  INDEX `fk_mensagens_2_idx` (`id_destinatario` ASC),
  CONSTRAINT `fk_mensagens_1`
    FOREIGN KEY (`id_remetente`)
    REFERENCES `trocai`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mensagens_2`
    FOREIGN KEY (`id_destinatario`)
    REFERENCES `trocai`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocai`.`avaliacoes_plataforma`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `trocai`.`avaliacoes_plataforma` ;

CREATE TABLE IF NOT EXISTS `trocai`.`avaliacoes_plataforma` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `conteudo` VARCHAR(255) NOT NULL,
  `nota` INT NOT NULL,
  `id_usuario` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_avaliacoes_plataforma_1_idx` (`id_usuario` ASC),
  CONSTRAINT `fk_avaliacoes_plataforma_1`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `trocai`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
