# Processo Dotz

# Desenho Arquitetura
![draw_io_dotz](https://user-images.githubusercontent.com/65379861/82136360-87cdc000-97e3-11ea-9c51-f35f93d94367.png)

# Ferramentas usadas na GCP

## Google Storage
Usado para armazenar os dados na fase raw(crua), para assim, poder ler o arquivo da maneira que foi apresentada.

## Compute Engine
Usado para criar uma VM com Python, para poder ler e processar os dados no bucket raw.

## Cloud SQL
Usado para criar uma VM MySQL, para armazenamento e vizualicação dos dados processados.

## Cloud Cron Job (Não realizado)
Utilizado para schedular todo o processo(diário).

# Necessário para rodar Programa
* VM gcp com Python;
* Ambiente vitural (virutalenv: https://github.com/pypa/virtualenv);
* instalar pacote de requerimentos;
``` shell
pip install -r requeriments.txt
```
* VM MySQL gcp;
* Conectar VM ip client a VM MySQL;
* Configurar cron job para o processo diário;

# CREATE TABLE
## bill_of_materials
``` sql
CREATE TABLE `bills_of_materials` (
  `tube_assembly_id` text,
  `component_id_1` text,
  `quantity_1` double NULL,
  `component_id_2` text,
  `quantity_2` double NULL,
  `component_id_3` text,
  `quantity_3` double NULL,
  `component_id_4` text,
  `quantity_4` double NULL,
  `component_id_5` text,
  `quantity_5` double NULL,
  `component_id_6` text,
  `quantity_6` double NULL,
  `component_id_7` text,
  `quantity_7` double NULL,
  `component_id_8` text,
  `quantity_8` double NULL
);
```
## comp_boss.sql
``` sql
CREATE TABLE `comp_boss` (
  `component_id` text,
  `component_type_id` text,
  `type` text,
  `connection_type_id` text,
  `outside_shape` text,
  `base_type` text,
  `height_over_tube` double NULL,
  `bolt_pattern_long` double NULL,
  `bolt_pattern_wide` double NULL,
  `groove` text,
  `base_diameter` double NULL,
  `shoulder_diameter` double NULL,
  `unique_feature` text,
  `orientation` text,
  `weight` double NULL
);
``` 

## price_quote
``` sql
CREATE TABLE `price_quote` (
  `tube_assembly_id` text,
  `supplier` text,
  `quote_date` text,
  `annual_usage` int(4)  NULL,
  `min_order_quantity` int(4) NULL,
  `bracket_pricing` text,
  `quantity` int(4) NULL,
  `cost` double NULL
);
```
# OBSERVAÇES
