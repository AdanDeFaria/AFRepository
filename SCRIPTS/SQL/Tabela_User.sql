USE safegsi;
CREATE TABLE safe_user (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    usuario VARCHAR(255) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    hash_senha VARCHAR(255) NOT NULL,
    e_mail VARCHAR(255) NOT NULL,
    telefone VARCHAR(255) NOT NULL,
    solicitante BOOLEAN NOT NULL,
    funcionario BOOLEAN NOT NULL,
    id_status INT NOT NULL,
    data_nascimento DATE,
    data_criacao DATETIME NOT NULL
);