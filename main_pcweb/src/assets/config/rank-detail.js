// 排名详情数据相关
export const detailTableHeadMap = [
    {key:'key',dataIndex:'key',title:'序号',width:100},
    {key:'org_name',dataIndex:'org_name', title:'机构名称',width:250},
    {key:'value_tm_done',dataIndex:'value_tm_done',title:'期末数'},
    {key:'value_ly_done',dataIndex:'value_ly_done',title:'上年数'},
    {key:'value_compare',dataIndex:'value_compare',title:'期末比上年'},
    {key:'value_ty_plan',dataIndex:'value_ty_plan',title:'计划数'},
    {key:'value_rate',dataIndex:'value_rate',title:'计划完成率'},
    {key:'operation',dataIndex:'operation',title:'操作'}
]

export const histroyTableHeadMap = [
    {key:'detail_date',dataIndex:'detail_date',title:'数据时间',width:100},
    {key:'value_tm_done',dataIndex:'value_tm_done',title:'期末数',align:'right'},
    {key:'value_ly_done',dataIndex:'value_ly_done',title:'上年数',align:'right'},
    {key:'value_compare',dataIndex:'value_compare',title:'期末比上年',align:'right'},
    {key:'value_ty_plan',dataIndex:'value_ty_plan',title:'计划数',align:'right'},
    {key:'value_rate',dataIndex:'value_rate',title:'计划完成率',align:'right'},
]

export const histroyEchartsConf = {
    resize:true,
    grid:{
        left:6,
        right:6,
        bottom:6,
        height:'90%',
        containLabel: true
    },
    xAxis:{
        type:'category',
        data:[],
        axisLine:{
            lineStyle:{color:'#e5e8ef',type:'dashed'}
        },
        axisLabel:{
            interval:0,
            color:'#86909c',
            type:'dashed',
            align:'center',
            rich:{
                start:{padding:[0,0,0,35]},
                end:{padding:[0,35,0,0]}
            }
        },
        boundaryGap:false
    },
    yAxis:{
        type:'value',
        axisLabel:{margin:24},
        splitLine:{
            lineStyle:{type:'dashed'}
        }
    },
    series:[
        {
            name:'期末数',
            data:[],
            type:'line',
            smooth:true,
            symbol:'none',
            lineStyle:{color:'#3469ff'},
            areaStyle:{color:''}
        },
        {
            name:'计划数',
            data:[],
            type:'line',
            smooth:true,
            symbol:'none',
            lineStyle:{color:'#722ed1'},
            areaStyle:{color:''}
        }
    ]
}