CREATE DATABASE clientes;

USE clientes;

CREATE TABLE Clientes (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    Idade INT NOT NULL,
    Cidade VARCHAR(255) NOT NULL
);