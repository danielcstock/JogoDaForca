CREATE DATABASE `db_jogodaforca` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

-- db_jogodaforca.tb_categoria definition

CREATE TABLE `tb_categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

-- db_jogodaforca.tb_palavra definition

CREATE TABLE `tb_palavra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `palavra` varchar(100) NOT NULL,
  `categoria` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_palavra_FK` (`categoria`),
  CONSTRAINT `tb_palavra_FK` FOREIGN KEY (`categoria`) REFERENCES `tb_categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

INSERT INTO tb_categoria  (nome) VALUES ("Escola");
INSERT INTO tb_categoria  (nome) VALUES ("Hospital");
INSERT INTO tb_categoria  (nome) VALUES ("Animal");
INSERT INTO tb_categoria  (nome) VALUES ("Brinquedo");
INSERT INTO tb_categoria  (nome) VALUES ("Planta");
INSERT INTO tb_categoria  (nome) VALUES ("Fruta");
INSERT INTO tb_categoria  (nome) VALUES ("Música");

INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Caderno", 1);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Recreio", 1);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Mochila", 1);

INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Vacina", 2);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Leito", 2);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Cirurgia", 2);

INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Papagaio", 3);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Lhama", 3);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Macaco", 3);

INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Roda Gigante", 4);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Bicicleta", 4);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Boneca", 4);

INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Hortelã", 5);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Laranjeira", 5);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Girassol", 5);

INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Abacate", 6);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Limão", 6);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Maracujá", 6);

INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Evidências", 7);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Sandy e Júnior", 7);
INSERT INTO tb_palavra  (palavra, categoria) VALUES ("Beyoncé", 7);