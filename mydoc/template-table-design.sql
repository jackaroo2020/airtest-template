-- ----------------------------------------
-- Table structure for uicase 
-- Desc: UI测试场景用例表
-- Author: LT
-- -----------------------------------------
-- DROP TABLE IF EXISTS `uicase`;
CREATE TABLE IF NOT EXISTS `ui_case` (
  `case_id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id序号',
  `case_desc` varchar(500) DEFAULT '' COMMENT '业务描述',
  `classify` varchar(20) DEFAULT '' COMMENT '业务分类标识,约定统一英文,h5使用`_h5`,微信公众号用`_wx`,app用`_app`，如phonebank_h5,phonebank_app,phonebank_wx',
  `method` varchar(50) NOT NULL COMMENT '方法名',
  `implement` char(2) DEFAULT 'Y' COMMENT '是否执行，Y：执行，N：不执行',
  `exp_result` varchar(64) DEFAULT 'pass' COMMENT '期望结果',
  `sort`  int(10) DEFAULT 0 COMMENT '排序编号',
  `status` char(1) DEFAULT '0' COMMENT '用例状态（0正常 1停用）',
  `create_by` varchar(64) DEFAULT 'LT' COMMENT '创建者',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_by` varchar(64) DEFAULT 'LT' COMMENT '更新者',
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `remark` varchar(500) DEFAULT '' COMMENT '备注',
  PRIMARY KEY (`case_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='UI测试场景用例表';

-- ----------------------------------------
-- Table structure for ui_log 
-- Desc: UI测试场景日志主表
-- Author: LT
-- -----------------------------------------
-- DROP TABLE IF EXISTS `ui_log`;
CREATE TABLE IF NOT EXISTS `ui_log` (
  `log_id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '日志序号',
  `start_time` varchar(32) DEFAULT '' COMMENT '用例执行开始时间',
  `end_time` varchar(32) DEFAULT '' COMMENT '用例执行结束时间',
  `total_time` float DEFAULT NULL COMMENT '执行总耗时，单位 秒,保留2位小数',
  `sum` INT DEFAULT NULL COMMENT '总执行用例数',
  `success` INT DEFAULT NULL COMMENT '成功总数',
  `success_rate` varchar(10) DEFAULT '' COMMENT '成功率,百分数表示，保留2位小数',
  `operation_ip` varchar(32) DEFAULT '' COMMENT '结果描述',
  `remark` varchar(500) DEFAULT '' COMMENT '备注',
  PRIMARY KEY (`log_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='UI测试场景日志主表';

-- ----------------------------------------
-- Table structure for ui_detail_log 
-- Desc: UI测试场景日志详细表
-- Author: LT
-- -----------------------------------------
-- DROP TABLE IF EXISTS `ui_detail_log`;
CREATE TABLE IF NOT EXISTS `ui_detail_log` (
  `log_detail_id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '日志详细序号',
  `log_id`  bigint(20) NOT NULL COMMENT '非空，关联ui_log的log_id号',
  `case_id` bigint(20) NOT NULL COMMENT '非空，关联ui_case的case_id字段',
  `start_time` varchar(32) DEFAULT '' COMMENT '用例执行开始时间',
  `end_time` varchar(32) DEFAULT '' COMMENT '用例执行结束时间',
  `total_time` float DEFAULT NULL COMMENT '执行总耗时，单位 秒,保留2位小数',
  `exp_result` varchar(64) DEFAULT '' COMMENT '期望结果',
  `act_result` varchar(64) DEFAULT '' COMMENT '实际结果',
  `result_desc` text DEFAULT NULL COMMENT '结果描述,也存放异常的日志信息',
  PRIMARY KEY (`log_detail_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='UI测试场景日志详细表';