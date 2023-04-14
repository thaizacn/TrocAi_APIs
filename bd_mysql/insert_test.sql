
SHOW TABLES;

SELECT * FROM usuarios;

# Adicionando dados
-- usuarios

INSERT INTO usuarios VALUES (
NULL, 'Luiz Eduardo', 'luiz@email.com', 'senha123', NULL);

INSERT INTO usuarios VALUES (
NULL, 'Thaiza Nascimento', 'thaiza@email.com', 'passwd', NULL);

INSERT INTO usuarios VALUES (
NULL, 'Gabriel Amorim', 'gabriel@email.com', 'pass123', NULL);

INSERT INTO usuarios VALUES (
NULL, 'Danielle Trajano', 'danielle@email.com', 'senha', NULL);

INSERT INTO usuarios VALUES (
NULL, 'André Toti', 'andre@email.com', 'password123', NULL);

-- itens
SELECT * FROM itens;
INSERT INTO itens VALUES (NULL,
'Box completo - Harry Potter',
'Está novinho em folha, estou desapegando porque estou me mudando',
 CURDATE(),
 2,
 'media.png')
 ;
 
 INSERT INTO itens VALUES (NULL,
'Caderno Inteligente',
'Estou procurando livros de Albert Camus',
 CURDATE(),
 3,
 'media1.png')
 ;
 
  INSERT INTO itens VALUES (NULL,
'Mochila Nike',
'Está em bom estado, mas tem algumas costuras',
 CURDATE(),
 4,
 'media2.png')
 ;
 
 -- operações
 SELECT * FROM operacoes;
 
 INSERT INTO operacoes VALUES (NULL, 1, 2, NOW());
 INSERT INTO operacoes VALUES (NULL, 3, NULL, NOW());
 
 -- avaliações operação
 SELECT * FROM avaliacoes_operacao;
 
INSERT INTO avaliacoes_operacao VALUES (
NULL,
'Troca bem sucedida, o Gabriel foi muito simpático',
5,
1,
2
);

INSERT INTO avaliacoes_operacao VALUES (
NULL,
'Gostei de trocar com a Thaiza, deu tudo certo!',
5,
1,
3
);

-- mensagens
SELECT * FROM mensagens;

INSERT INTO mensagens VALUES(
NULL,
'Oi Gabriel, me interessei pelo caderno inteligente. Eu não tenho
nenhum livro do Albert Camus, mas tenho um box do Harry Potter.
Te interessa?',
2,
3,
NOW()
);

INSERT INTO mensagens VALUES(
NULL,
'Boa noite Thaiza! me interessa sim rs',
3,
2,
NOW()
);

## campo 'data_envio' deveria se chamar 'data_e_hora'

-- avaliacoes plataforma

SELECT * FROM avaliacoes_plataforma;

INSERT INTO avaliacoes_plataforma VALUES (
NULL,
'Gostaria que melhorassem a visualização do feed',
3,
4
);