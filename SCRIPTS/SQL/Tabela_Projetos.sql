USE safegsi;
CREATE TABLE safe_projetos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    projetos VARCHAR(255),
    id_funcionario INT,
    id_solicitante INT,
    id_prioridade INT,
    id_status INT,
    versao VARCHAR(10),
    data_prevista DATE,
    data_criacao DATETIME,
    data_finalizacao DATETIME,
    obs BLOB
);