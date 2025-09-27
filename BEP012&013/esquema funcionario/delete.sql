-- a) Remover funcionários com idade superior a 60 anos
DELETE FROM Funcionarios
WHERE idade > 60;

-- b) Excluir funcionário F007
DELETE FROM Funcionarios
WHERE idFuncionario = 'F007';

-- c) Remover todos com salário inferior a 30000
DELETE FROM Funcionarios
WHERE salario < 30000;
