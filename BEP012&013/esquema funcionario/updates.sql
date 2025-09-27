-- a) Aumentar salário em 15% para programadores
UPDATE Funcionarios
SET salario = salario * 1.15
WHERE cargo = 'Programador';

-- b) Alterar cargo do funcionário F005 para Gerente de Projeto
UPDATE Funcionarios
SET cargo = 'Gerente de Projeto'
WHERE idFuncionario = 'F005';

-- c) Adicionar 1 ano ao tempo de serviço dos que têm mais de 5 anos
UPDATE Funcionarios
SET tempoServico = tempoServico + 1
WHERE tempoServico > 5;
