import sqlite3

conn = sqlite3.connect('concessionaria.db')
c = conn.cursor()

c.execute("PRAGMA foreign_keys = ON;")

c.executescript("""
CREATE TABLE IF NOT EXISTS comprador (
    cpf TEXT PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    estadoCivil TEXT NOT NULL,
    nomeConjuge TEXT,
    cpfConjuge TEXT
);

CREATE TABLE IF NOT EXISTS corretor (
    nrMatricula INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    dataAdmissao TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS venda (
    idvenda INTEGER PRIMARY KEY NOT NULL,
    dataVenda TEXT NOT NULL,
    valorVenda REAL NOT NULL,
    comissao REAL NOT NULL,
    comprador_cpf TEXT NOT NULL,
    corretor_nrMatricula INTEGER NOT NULL,
    FOREIGN KEY (comprador_cpf) REFERENCES comprador(cpf),
    FOREIGN KEY (corretor_nrMatricula) REFERENCES corretor(nrMatricula)
);

CREATE TABLE IF NOT EXISTS Marca (
    idMarca INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS modelo (
    idmodelo INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    Marca_idMarca INTEGER NOT NULL,
    FOREIGN KEY (Marca_idMarca) REFERENCES Marca(idMarca)
);

CREATE TABLE IF NOT EXISTS veiculo (
    idVeiculo INTEGER NOT NULL,
    chassi TEXT NOT NULL,
    anoFabricacao TEXT NOT NULL,
    cor TEXT NOT NULL,
    quilometragem INTEGER,
    venda_idvenda INTEGER NOT NULL,
    modelo_idmodelo INTEGER NOT NULL,
    PRIMARY KEY (idVeiculo, venda_idvenda),
    FOREIGN KEY (venda_idvenda) REFERENCES venda(idvenda),
    FOREIGN KEY (modelo_idmodelo) REFERENCES modelo(idmodelo)
);
""")

conn.commit()
conn.close()
