CREATE TABLE IF NOT EXISTS `ORG_INFO_TABLE` (
    `ID` INT NOT NULL AUTO_INCREMENT COMMENT '机构id',
    `ORG_NUM` VARCHAR(10) NOT NULL COMMENT '机构编号',
    `ORG_NAME` VARCHAR(64) NOT NULL COMMENT '机构名称',
    `PARENT_ORG_ID` INT COMMENT '上级机构id',
    `ORG_LEVEL` INT COMMENT '机构层级',
    `ORG_GROUP` INT COMMENT '机构分组',
    `ORG_CREATE` DATE NOT NULL COMMENT '机构创建时间',
    `ORG_UPDATE` DATE COMMENT '机构修改时间',
    `ORG_STATUS` INT COMMENT '机构状态',
    `ORG_EXT_INFO` VARCHAR(64) COMMENT '机构扩展字段',
    PRIMARY KEY (`ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;