create database VendasDW;
GO

USE VendasDW;
GO

create table fato_vendas
(
    id_venda int,
    data_venda date,
    produto varchar(100),
    categoria varchar(50),
    quantidade int,
    preco_unitario decimal(10,2),
    valor_total decimal(10,2),
    vendedor varchar(100)
);