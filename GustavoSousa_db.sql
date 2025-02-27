create database GustavoSousa_db

create table usuario(
	idusuario int not null auto_increment,
    nome text,
    telefone text,
    emaill text,
    usuario text,
    senha text,
    primary key (idusuario)
    );