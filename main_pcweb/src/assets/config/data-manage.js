// 对于data-manage页面的表头进行定义
export const dataTableHead = [
    {
        key:'record_id',
        dataIndex: 'record_id',
        title:'导入编号'
    },
    {
        key:'class_name',
        dataIndex:'class_name',
        title:'数据分类'
    },
    {
        key:'record_dt',
        dataIndex:'record_dt',
        title:'通报月份'
    },
    {
        key:'record_update_time',
        dataIndex:'record_update_time',
        title:'导入日期'
    },
    {
        key:'user_name',
        dataIndex:'user_name',
        title:'导入人'
    },
    {
        key:'view_more',
        dataIndex:'view_more',
        title:'操作'
    }
]

export const dataEditIndex = []

export const dataEditMap = []

export const dataViewMap = [
    {text:'查看详情',target:'record_id',path_name:'data-detail',params:'data_id'}
]

export const dataViewInfo = []

export const dataImportModal = {
    group_info:{
        label: '新增方式',
        data: [{key:0,label:'单条新增'}],
        need_show:false
    },
    form_list: [
        {
            group:0,
            label: '数据分类',
            dataIndex:'class_name',
            type:'select',
            option: [
                {ref_code:1,ref_name:'企金'},
                {ref_code:2,ref_name:'零售'},
                {ref_code:3,ref_name:'同业'},
                {ref_code:4,ref_name:'其他'}
            ],
            optionIndex:'index_class',
            search_map:{},
            search_func:{},
            required:true
        },
        {
            group:0,
            label:'通报月份',
            dataIndex:'record_dt',
            type:'date-month',
            option:[],
            optionindex:'',
            search_map:{},
            search_func:{},
            required:true
        },
        {
            group:0,
            label:'导入文件',
            dataIndex:'upload_file',
            type:'file',
            option:[],
            optionIndex:'',
            search_map:{},
            search_func:{},
            required:true
        }
    ]
}