create database if not exists escola;

use escola;

create table alunos(
	id_aluno int auto_increment primary key,
	nome varchar(50) not null,
    idade int not null
);

create table cursos(
	id_curso int auto_increment primary key,
    nome_curso varchar(255),
    carga_horario int
);

create table matriculas(
	id_matricula int auto_increment primary key,
    id_aluno int,
    foreign key (id_aluno) references alunos(id_aluno),
    id_curso int,
    foreign key (id_curso) references cursos(id_curso),
    data_matricual date
);
