USE safegsi;
CREATE TABLE safe_tarefas_tipos (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    tarefas_tipo VARCHAR(255) NOT NULL,
    id_status INT NOT NULL
);