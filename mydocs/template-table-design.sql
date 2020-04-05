-- ----------------------------------------
-- Table structure for uicase 
-- Desc: UI���Գ���������
-- Author: LT
-- -----------------------------------------
-- DROP TABLE IF EXISTS `uicase`;
CREATE TABLE IF NOT EXISTS `ui_case` (
  `case_id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id���',
  `case_desc` varchar(500) DEFAULT '' COMMENT 'ҵ������',
  `classify` varchar(20) DEFAULT '' COMMENT 'ҵ������ʶ,Լ��ͳһӢ��,h5ʹ��`_h5`,΢�Ź��ں���`_wx`,app��`_app`����phonebank_h5,phonebank_app,phonebank_wx',
  `method` varchar(50) NOT NULL COMMENT '������',
  `implement` char(2) DEFAULT 'Y' COMMENT '�Ƿ�ִ�У�Y��ִ�У�N����ִ��',
  `exp_result` varchar(64) DEFAULT 'pass' COMMENT '�������',
  `sort`  int(10) DEFAULT 0 COMMENT '������',
  `status` char(1) DEFAULT '0' COMMENT '����״̬��0���� 1ͣ�ã�',
  `create_by` varchar(64) DEFAULT 'LT' COMMENT '������',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '����ʱ��',
  `update_by` varchar(64) DEFAULT 'LT' COMMENT '������',
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '����ʱ��',
  `remark` varchar(500) DEFAULT '' COMMENT '��ע',
  PRIMARY KEY (`case_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='UI���Գ���������';

-- ----------------------------------------
-- Table structure for ui_log 
-- Desc: UI���Գ�����־����
-- Author: LT
-- -----------------------------------------
-- DROP TABLE IF EXISTS `ui_log`;
CREATE TABLE IF NOT EXISTS `ui_log` (
  `log_id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '��־���',
  `start_time` varchar(32) DEFAULT '' COMMENT '����ִ�п�ʼʱ��',
  `end_time` varchar(32) DEFAULT '' COMMENT '����ִ�н���ʱ��',
  `total_time` float DEFAULT NULL COMMENT 'ִ���ܺ�ʱ����λ ��,����2λС��',
  `sum` INT DEFAULT NULL COMMENT '��ִ��������',
  `success` INT DEFAULT NULL COMMENT '�ɹ�����',
  `success_rate` varchar(10) DEFAULT '' COMMENT '�ɹ���,�ٷ�����ʾ������2λС��',
  `operation_ip` varchar(32) DEFAULT '' COMMENT '�������',
  `remark` varchar(500) DEFAULT '' COMMENT '��ע',
  PRIMARY KEY (`log_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='UI���Գ�����־����';

-- ----------------------------------------
-- Table structure for ui_detail_log 
-- Desc: UI���Գ�����־��ϸ��
-- Author: LT
-- -----------------------------------------
-- DROP TABLE IF EXISTS `ui_detail_log`;
CREATE TABLE IF NOT EXISTS `ui_detail_log` (
  `log_detail_id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '��־��ϸ���',
  `log_id`  bigint(20) NOT NULL COMMENT '�ǿգ�����ui_log��log_id��',
  `case_id` bigint(20) NOT NULL COMMENT '�ǿգ�����ui_case��case_id�ֶ�',
  `start_time` varchar(32) DEFAULT '' COMMENT '����ִ�п�ʼʱ��',
  `end_time` varchar(32) DEFAULT '' COMMENT '����ִ�н���ʱ��',
  `total_time` float DEFAULT NULL COMMENT 'ִ���ܺ�ʱ����λ ��,����2λС��',
  `exp_result` varchar(64) DEFAULT '' COMMENT '�������',
  `act_result` varchar(64) DEFAULT '' COMMENT 'ʵ�ʽ��',
  `result_desc` text DEFAULT NULL COMMENT '�������,Ҳ����쳣����־��Ϣ',
  PRIMARY KEY (`log_detail_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='UI���Գ�����־��ϸ��';