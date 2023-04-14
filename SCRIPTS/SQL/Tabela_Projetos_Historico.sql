USE safegsi;
CREATE TABLE safe_projetos_historico (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_projetos INT NOT NULL,
    data_prevista DATE NOT NULL,
    nova_data_prevista DATE NOT NULL,
    data_alteracao TIMESTAMP NOT NULL,
    obs BLOB NOT NULL
);