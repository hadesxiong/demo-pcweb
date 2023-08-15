CREATE TABLE IF NOT EXISTS `INDEX_INFO_TABLE` (
    `ID` INT NOT NULL AUTO_INCREMENT COMMENT '指标id',
    `INDEX_NUM` VARCHAR(10) NOT NULL COMMENT '指标编号',
    `INDEX_CLASS` INT COMMENT '指标分类-财务效益等',
    `BELONG_BU` INT COMMENT '指标归属条线-企金、零售、同业、其他等',
    `INDEX_UNIT` VARCHAR(10) COMMENT '指标单位',
    `INDEX_NAME` VARCHAR(64) NOT NULL COMMENT '指标名称',
    `INDEX_TYPE` INT COMMENT '指标类型-个人，机构等',
    `NEED_FOCUS` INT NOT NULL COMMENT '是否重点指标',
    `NEED_SHOW` INT NOT NULL COMMENT '是否需要展示',
    `IS_DB` INT COMMENT '是否是首页数据看板内容',
    `INDEX_CREATE` DATE NOT NULL COMMENT '指标创建时间',
    `INDEX_UPDATE` DATE COMMENT '指标更新时间',
    `INDEX_STATUS` INT COMMENT '指标状态',
    `INDEX_EXT_INFO` VARCHAR(64) COMMENT '指标扩展字段',
    PRIMARY KEY (`ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;