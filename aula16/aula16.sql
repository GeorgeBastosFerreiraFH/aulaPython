CREATE DATABASE locadora;
USE locadora;

CREATE TABLE filmes(
	id_filme int primary key auto_increment,
    nome_filme varchar(100),
    genero varchar(100),
    duracao int
);

CREATE TABLE series(
	id_serie int primary key auto_increment,
    nome_serie varchar(100),
    genero varchar(100),
    temporadas int
);

INSERT INTO filmes(nome_filme, genero, duracao) VALUES
	("Draculla", "terror", 7200),
	("Rei Leão", "Animação", 8000),
    ("Carga Explosiva", "Ação", 6000);

INSERT INTO series(nome_serie, genero, temporadas) VALUES
	("Round 6", "Terror", 2),
    ("One Piece", "Animação", 22),
    ("Ruptura", "Suspense", 2);

SELECT * FROM filmes;

SELECT * FROM filmes WHERE duracao >= 7200;

SELECT * FROM series WHERE temporadas >= 5;
