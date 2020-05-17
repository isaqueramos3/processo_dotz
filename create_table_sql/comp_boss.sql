comp_boss | CREATE TABLE `comp_boss` (
  `index` bigint(20) DEFAULT NULL,
  `component_id` text,
  `component_type_id` text,
  `type` text,
  `connection_type_id` text,
  `outside_shape` text,
  `base_type` text,
  `height_over_tube` double DEFAULT NULL,
  `bolt_pattern_long` double DEFAULT NULL,
  `bolt_pattern_wide` double DEFAULT NULL,
  `groove` text,
  `base_diameter` double DEFAULT NULL,
  `shoulder_diameter` double DEFAULT NULL,
  `unique_feature` text,
  `orientation` text,
  `weight` double DEFAULT NULL,
  KEY `ix_comp_boss_index` (`index`)
)