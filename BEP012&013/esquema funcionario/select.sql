-- a) Nomes e sobrenomes dos empregados que são programadores
SELECT nome, sobrenome FROM Funcionarios
WHERE cargo = 'Programador';

-- b) Nomes e sobrenomes dos empregados com menos de 3 anos de serviço
SELECT nome, sobrenome FROM Funcionarios
WHERE tempoServico < 3;

-- c) Nomes e sobrenomes dos empregados cujo nome começa com 'J'
SELECT nome, sobrenome FROM Funcionarios
WHERE nome LIKE 'J%';

-- d) Nomes e sobrenomes dos empregados que trabalham como 'Senior'
SELECT nome, sobrenome FROM Funcionarios
WHERE cargo LIKE '%Senior%';

-- e) Nomes e sobrenomes dos empregados com salário entre 70.000 e 90.000
SELECT nome, sobrenome FROM Funcionarios
WHERE salario BETWEEN 70000 AND 90000;

-- f) Nomes, sobrenomes e idades dos empregados cujo sobrenome começa com 'A' ou 'S' e idade < 30
SELECT nome, sobrenome, idade FROM Funcionarios
WHERE (sobrenome LIKE 'A%' OR sobrenome LIKE 'S%')
  AND idade < 30;

-- g) Nomes, sobrenomes e cargos dos empregados que não são programadores
SELECT nome, sobrenome, cargo FROM Funcionarios
WHERE cargo <> 'Programador';

-- h) Nomes, sobrenomes e idades ordenados por idade desc, limitados a 4
SELECT nome, sobrenome, idade FROM Funcionarios
ORDER BY idade DESC
LIMIT 4;
