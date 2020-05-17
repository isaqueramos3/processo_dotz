CREATE TABLE `price_quote` (
  `index` bigint(20) DEFAULT NULL,
  `tube_assembly_id` text,
  `supplier` text,
  `quote_date` text,
  `annual_usage` bigint(20) DEFAULT NULL,
  `min_order_quantity` bigint(20) DEFAULT NULL,
  `bracket_pricing` text,
  `quantity` bigint(20) DEFAULT NULL,
  `cost` double DEFAULT NULL,
  KEY `ix_price_quote_index` (`index`)
)