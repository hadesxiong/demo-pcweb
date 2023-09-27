// 对于固定的表头进行定义
 
export const userTableHead = [
    {
        "title":"NotesID",
        "key":"notes_id",
        "dataIndex":"notes_id",
        "width":"15%"
    },
    {
        "title":"用户名称",
        "key":"user_name",
        "dataIndex":"user_name",
        "width":"15%"
    },
    {
        "title":"用户角色",
        "key":"character_name",
        "dataIndex":"character_name",
        "width":"15%"
    },
    {
        "title":"归属条线",
        "key":"group_name",
        "dataIndex":"group_name",
        "width":"10%"
    },
    {
        "title":"归属机构",
        "key":"org_name",
        "dataIndex":"org_name",
        "width":"15%"
    },
    {
        "title":"直属上级",
        "key":"org_manager",
        "dataIndex":"org_manager",
        "width":"15%"
    },
    {
        "title":"操作",
        "key":"operation",
        "dataIndex":"operation",
        "width":"20%"
    }
]

export const userEditIndex = [
    {
        column: 'user_name',
        type: 'input',
        option_list: [],
    },
    {
        column: 'character_name',
        type: 'select',
        option_list: []
    },
    {
        column: 'group_name',
        type:'select',
        option_list:[]
    },
    {
        column: 'org_name',
        type: 'search',
        option_list: []
    }
]

export const orgTableHead = [
    {
        "title":"机构编号",
        "key":"org_num",
        "dataIndex":"org_num",
        "width":"10%"
    },
    {
        "title":"机构名称",
        "key":"org_name",
        "dataIndex":"org_name",
        "width":"15%"
    },
    {
        "title":"机构分组",
        "key":"group_name",
        "dataIndex":"group_name",
        "width":"10%"
    },
    {
        "title":"机构层级",
        "key":"level_name",
        "dataIndex":"level_name",
        "width":"10%"
    },
    {
        "title":"上级机构",
        "key":"parent_org_name",
        "dataIndex":"parent_org_name",
        "width":"15%"
    },
    {
        "title":"负责人",
        "key":"org_manager_name",
        "dataIndex":"org_manager_name",
        "width":"15%"
    },
    {
        "title":"操作",
        "key":"operation",
        "dataIndex":"operation",
        "width":"15%"
    }
]

export const orgEditIndex = [
    {
        column:'org_name',
        type:'input',
        option_list:[]
    },
    {
        column:'group_name',
        type:'select',
        option_list:[]
    },
    {
        column:'level_name',
        type:'select',
        option_list:[]
    },
    {
        column:'parent_org_name',
        type:'search',
        option_list:[]
    },
    {
        column:'org_manager_name',
        type:'search',
        option_list:[]
    }
]

export const orgEditMap = [
    {
        code_target:'org_group',
        name_target:'group_name',
        range:[]
    },
    {
        code_target:'org_level',
        name_target:'level_name',
        range:[]
    }
]

export const userEditMap = [
    {
        code_target: 'user_character',
        name_target: 'character_name',
        range: []
    },
    {
        code_target: 'user_belong_group',
        name_target: 'group_name',
        range: []
    }
]

export const userSearchInfo = {
    search_map: {
        org_name: {
            in:{label:'org_name',key:'org_num',value:'org_name'},
            out: {label:'org_name',key:'user_belong_org',value:'org_name'}
        }
    },
    search_api: {
        org_name:{
            url:'/api/org/getOrgList',
            params: {
                level:0,
                group:0,
                client:0,
                size:10,
                ext:''
            }
        }
    }
}

export const orgSearchInfo = {
    search_map: {
        parent_org_name:{
            in:{label:'parent_org_name',key:'org_num',value:'parent_org_name'},
            out:{label: 'parent_org_name',key:'parent_org_id',value:'parent_org_name'}
        },
        org_manager_name:{
            in:{label:'user_name_withId',key:'notes_id',value:'user_name_withId'},
            out:{label:'org_manager_name',key:'org_manager',value:'org_manager_name'}
        }
    },
    search_api: {
        parent_org_name:{
            url:'/api/org/getOrgList',
            params: {
                level:0,
                group:0,
                client:0,
                size:10,
                ext:''
            }
        },
        org_manager_name:{
            url:'/api/user/getUserList',
            params:{
                group:5,
                character:3,
                client:0,
                size:10,
                ext:''
            }
        }
    }
}

export const updateUserModal = {
    group_info:{
        label: '新增方式',
        data: [{key:0,label:'单条新增'},{key:1,label:'批量新增'}],
        need_show: true
    },
    form_list: [
        {
            group:0,
            label:'NotesID',
            dataIndex:'notes_id',
            type:'input',
            option:[],
            optionIndex:'',
            search_map:{},
            search_func:{},
            required: true
        },
        {
            group:0,
            label:'用户名称',
            dataIndex:'user_name',
            type:'input',
            option:[],
            optionIndex:'',
            search_map:{},
            search_func:{},
            required: true
        },
        {
            group:0,
            label:'用户角色',
            dataIndex: 'character_name',
            type:'select',
            option:[
                {ref_code:1,ref_name:'超级管理员'},
                {ref_code:2,ref_name:'管理员'},
                {ref_code:3,ref_name:'部分负责人'},
                {ref_code:4,ref_name:'客户经理'},
                {ref_code:5,ref_name:'部门成员'}
            ],
            optionIndex:'user_character',
            search_map:{},
            search_func:{},
            required: true
        },
        {
            group:0,
            label:"归属条线",
            dataIndex:'group_name',
            type:'select',
            option:[
                {ref_code:1,ref_name:'企金'},
                {ref_code:2,ref_name:'零售'},
                {ref_code:3,ref_name:'同业'},
                {ref_code:4,ref_name:'其他'},
                {ref_code:5,ref_name:'管理'}
            ],
            optionIndex:'user_belong_group',
            search_map:{},
            search_func:{},
            required: true
        },
        {
            group:0,
            label:"归属机构",
            dataIndex:'org_name',
            type:'search',
            option:[],
            optionIndex:'',
            search_map:{
                in:{label:'org_name',key:'org_num',value:'org_name'},
                out: {label:'org_name',key:'user_belong_org',value:'org_name'}
            },
            search_func:{
                url:'/api/org/getOrgList',
                params: {
                    level:0,
                    group:0,
                    client:0,
                    size:10,
                    ext:''
                }
            },
            required: true
        },
        {
            group:0,
            label:"直属上级",
            dataIndex:'org_manager',
            type:'show-only',
            option:[],
            optionIndex:'',
            search_map:{},
            search_func:{}
        },
        {
            group:1,
            label:'数据文件',
            dataIndex: 'file_upload',
            type:'file',
            option:[],
            optionIndex:'',
            search_map:{},
            search_func:{},
            required: true
        }
    ]
}

export const updateOrgModal = {
    group_info: {
        label: '新增方式',
        data: [{key:0,label:'单条新增'}],
        need_show: false
    },
    form_list: [
        {
            group:0,
            label:'机构编号',
            dataIndex:'org_num',
            type:'input',
            option:[],
            optionIndex:'',
            search_map:{},
            search_func:{},
            required:true
        },
        {
            group:0,
            label:'机构名称',
            dataIndex:'org_name',
            type:'input',
            option:[],
            optionIndex:'',
            search_map:{},
            search_func:{},
            required:true
        },
        {
            group:0,
            label:'机构分组',
            dataIndex:'group_name',
            type:'select',
            option:[
                {ref_code:1,ref_name:'区域中心支行'},
                {ref_code:2,ref_name:'战略客户部'},
                {ref_code:3,ref_name:'单点支行'},
                {ref_code:4,ref_name:'职能部门'},
                {ref_code:5,ref_name:'其他'}
            ],
            optionindex:'org_group',
            search_map:{},
            search_func:{}
        },
        {
            group:0,
            label:'机构层级',
            dataIndex:'level_name',
            type:'select',
            option:[
                {ref_code:1,ref_name:'分行'},
                {ref_code:2,ref_name:'分行部门'},
                {ref_code:3,ref_name:'一级经营机构'},
                {ref_code:4,ref_name:'二级经营机构'},
                {ref_code:5,ref_name:'经营机构部门'}
            ],
            search_map:{},
            search_func:{},
            required:true
        },
        {
            group:0,
            label:'上级机构',
            dataIndex:'parent_org_name',
            type:'search',
            option:[],
            optionindex:'',
            search_map:{
                in:{label:'org_name',key:'org_num',value:'org_name'},
                out:{label: 'parent_org_name',key:'parent_org_id',value:'parent_org_name'}
            },
            search_func:{
                url:'/api/org/getOrgList',
                params: {
                    level:0,
                    group:0,
                    client:0,
                    size:10,
                    ext:''
                }
            },
            required:true
        },
        {
            group:0,
            label:'负责人',
            dataIndex:'org_manager_name',
            type:'search',
            option:[],
            optionIndex:'',
            search_map:{
                in:{label:'user_name_withId',key:'notes_id',value:'user_name_withId'},
                out:{label:'org_manager_name',key:'org_manager',value:'org_manager_name'}
            },
            search_func:{
                url:'/api/user/getUserList',
                params:{
                    group:5,
                    character:3,
                    client:0,
                    size:10,
                    ext:''
                }
            },
            required:true
        }
    ]

}