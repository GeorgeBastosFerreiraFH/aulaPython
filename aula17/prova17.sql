CREATE DATABASE mercadinho;
USE mercadinho;

CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
    NomeProduto VARCHAR(255) NOT NULL,
    Quantidade INT NOT NULL,
    Preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE Fornecedores (
    FornecedorID INT PRIMARY KEY AUTO_INCREMENT,
    NomeFornecedor VARCHAR(255) NOT NULL,
    Contato VARCHAR(100)
);

-- TABELA ESTOQUE

CREATE TABLE Estoque (
    EstoqueID INT PRIMARY KEY AUTO_INCREMENT,
    ProdutoID INT NOT NULL,
    FornecedorID INT NOT NULL,
    Quantidade INT NOT NULL,
    DataEntrada DATE NOT NULL,
    CONSTRAINT FkProduto FOREIGN KEY (ProdutoID)
        REFERENCES Produtos(ProdutoID),
    CONSTRAINT FkFornecedor FOREIGN KEY (FornecedorID)
        REFERENCES Fornecedores(FornecedorID)
);

-- FULL OUTER JOIN

SELECT 
    p.NomeProduto,
    f.NomeFornecedor,
    e.Quantidade,
    e.DataEntrada
FROM Produtos p
LEFT JOIN Estoque e ON p.ProdutoID = e.ProdutoID
LEFT JOIN Fornecedores f ON e.FornecedorID = f.FornecedorID;

-- GROUP BY

SELECT 
    ProdutoID,
    SUM(Quantidade) AS TotalEstoque
FROM Estoque
GROUP BY ProdutoID;

-- ALTER TABLE

ALTER TABLE Estoque
ADD PrecoCusto DECIMAL(10,2);

