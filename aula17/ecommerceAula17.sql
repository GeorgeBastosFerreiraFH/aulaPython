CREATE DATABASE ecommerce;

USE ecommerce;

CREATE TABLE clientes(
	id_cliente INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(255),
    email VARCHAR(255),
    telefone VARCHAR(50)
);

CREATE TABLE produtos(
	id_produto INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    categoria VARCHAR(255),
    qntd_estoque INT DEFAULT 0
);

-- Inserir dados na tabela de clientes
INSERT INTO clientes (nome, email, telefone) VALUES
('João Silva', 'joao.silva@email.com', '(11) 98765-4321'),
('Maria Oliveira', 'maria.oliveira@email.com', '(21) 99876-5432'),
('Carlos Pereira', 'carlos.pereira@email.com', '(31) 91234-5678'),
('Ana Costa', 'ana.costa@email.com', '(41) 94567-1234'),
('Pedro Souza', 'pedro.souza@email.com', '(51) 99865-4321');

-- Inserir dados na tabela de produtos
INSERT INTO produtos (nome, preco, categoria, qntd_estoque) VALUES
('Camiseta Básica', 49.99, 'Roupas', 120),
('Tênis Esportivo', 299.90, 'Calçados', 50),
('Notebook Gamer', 4999.99, 'Eletrônicos', 30),
('Smartphone Android', 1999.90, 'Eletrônicos', 150),
('Cadeira Ergonômica', 799.90, 'Móveis', 25);


CREATE TABLE pedidos(
	id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
	dia_compra INT NOT NULL,
    mes_compra INT NOT NULL,
	ano_compra INT NOT NULL,
	valor_total DECIMAL(10,2) NOT NULL
);

INSERT INTO pedidos (id_cliente, dia_compra, mes_compra, ano_compra, valor_total) VALUES
(1, 10, 3, 2025, 150.00),
(2, 11, 3, 2025, 200.00),
(3, 12, 3, 2025, 120.00),
(4, 13, 3, 2025, 250.00),
(5, 14, 3, 2025, 175.00);

SELECT * FROM pedidos JOIN clientes 
ON pedidos.id_cliente = clientes.id_cliente;

DROP TABLE pagamento;

CREATE TABLE itens_pedidos(
	id_itens_pedidos INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    id_produto INT,
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto),
    quantidade INT
);

CREATE TABLE formas_pagamento(
	id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255)
);

CREATE TABLE pagamento(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    forma_pagamento_id INT,
    FOREIGN KEY (forma_pagamento_id) REFERENCES formas_pagamento(id_pagamento),
	status_pedido ENUM('pendente', 'aprovado', 'recusado') NOT NULL
);

INSERT INTO itens_pedidos(id_pedido, id_produto, quantidade) VALUES 
(2, 3, 20),
(1, 2, 3),
(3, 4, 5),
(4, 5, 2),
(5, 1, 99);

INSERT INTO formas_pagamento (nome) VALUE 
('Pix'),
('Cartão de crédito'),
('Cartão de débito'),
('Boleto'),
('Dinheiro');

INSERT INTO pagamento (id_pedido, forma_pagamento_id, status_pedido) VALUE 
(1, 4, 'aprovado'),
(2, 3, 'recusado'),
(3, 1, 'pendente'),
(4, 2, 'aprovado'),
(5, 3, 'recusado'),
(6, 1, 'pendente');

SELECT * FROM itens_pedidos;
SELECT * FROM formas_pagamento;
SELECT * FROM pagamento;
