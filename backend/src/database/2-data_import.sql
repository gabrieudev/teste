COPY operadoras(
    registro_ans,
    cnpj,
    razao_social,
    nome_fantasia,
    modalidade,
    logradouro,
    numero,
    complemento,
    bairro,
    cidade,
    uf,
    cep,
    ddd,
    telefone,
    fax,
    endereco_eletronico,
    representante,
    cargo_representante,
    regiao_de_comercializacao,
    data_registro_ans
)
FROM '/csv-data/operadoras.csv'
WITH (
    FORMAT csv,
    DELIMITER ';',
    HEADER true,
    ENCODING 'UTF-8'
);

COPY despesas(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/csv-data/1T2023.csv'
WITH (
    FORMAT csv,
    DELIMITER ';',
    HEADER true,
    ENCODING 'UTF-8'
);

COPY despesas(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/csv-data/1T2024.csv'
WITH (
    FORMAT csv,
    DELIMITER ';',
    HEADER true,
    ENCODING 'UTF-8'
);

COPY despesas(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/csv-data/2t2023.csv'
WITH (
    FORMAT csv,
    DELIMITER ';',
    HEADER true,
    ENCODING 'UTF-8'
);

COPY despesas(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/csv-data/2T2024.csv'
WITH (
    FORMAT csv,
    DELIMITER ';',
    HEADER true,
    ENCODING 'UTF-8'
);

COPY despesas(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/csv-data/3T2023.csv'
WITH (
    FORMAT csv,
    DELIMITER ';',
    HEADER true,
    ENCODING 'UTF-8'
);

COPY despesas(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/csv-data/3T2024.csv'
WITH (
    FORMAT csv,
    DELIMITER ';',
    HEADER true,
    ENCODING 'UTF-8'
);

COPY despesas(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/csv-data/4T2023.csv'
WITH (
    FORMAT csv,
    DELIMITER ';',
    HEADER true,
    ENCODING 'UTF-8'
);

COPY despesas(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/csv-data/4T2024.csv'
WITH (
    FORMAT csv,
    DELIMITER ';',
    HEADER true,
    ENCODING 'UTF-8'
);
