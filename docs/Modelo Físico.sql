/* Lógico_1: */

CREATE TABLE Colecao (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    descricao VARCHAR
);

CREATE TABLE Objeto (
    id INTEGER PRIMARY KEY,
    titulo VARCHAR,
    descricao VARCHAR,
    data VARCHAR,
    caminho VARCHAR
);

CREATE TABLE Categoria (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    fk_Objeto_id INTEGER
);

CREATE TABLE Visualizacao (
    id INTEGER PRIMARY KEY,
    rotulo VARCHAR,
    largura INTEGER,
    altura INTEGER
);

CREATE TABLE Anotacao (
    id INTEGER PRIMARY KEY,
    texto VARCHAR,
    tipo VARCHAR,
    posicao VARCHAR
);

CREATE TABLE pertence (
    fk_Objeto_id INTEGER,
    fk_Colecao_id INTEGER
);

CREATE TABLE representado (
    fk_Objeto_id INTEGER,
    fk_Visualizacao_id INTEGER
);

CREATE TABLE anotado (
    fk_Anotacao_id INTEGER,
    fk_Visualizacao_id INTEGER
);
 
ALTER TABLE Categoria ADD CONSTRAINT FK_Categoria_2
    FOREIGN KEY (fk_Objeto_id)
    REFERENCES Objeto (id)
    ON DELETE CASCADE;
 
ALTER TABLE pertence ADD CONSTRAINT FK_pertence_1
    FOREIGN KEY (fk_Objeto_id)
    REFERENCES Objeto (id)
    ON DELETE SET NULL;
 
ALTER TABLE pertence ADD CONSTRAINT FK_pertence_2
    FOREIGN KEY (fk_Colecao_id)
    REFERENCES Colecao (id)
    ON DELETE SET NULL;
 
ALTER TABLE representado ADD CONSTRAINT FK_representado_1
    FOREIGN KEY (fk_Objeto_id)
    REFERENCES Objeto (id)
    ON DELETE RESTRICT;
 
ALTER TABLE representado ADD CONSTRAINT FK_representado_2
    FOREIGN KEY (fk_Visualizacao_id)
    REFERENCES Visualizacao (id)
    ON DELETE RESTRICT;
 
ALTER TABLE anotado ADD CONSTRAINT FK_anotado_1
    FOREIGN KEY (fk_Anotacao_id)
    REFERENCES Anotacao (id)
    ON DELETE SET NULL;
 
ALTER TABLE anotado ADD CONSTRAINT FK_anotado_2
    FOREIGN KEY (fk_Visualizacao_id)
    REFERENCES Visualizacao (id)
    ON DELETE SET NULL;