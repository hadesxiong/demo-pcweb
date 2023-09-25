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

export const searchInfo = {
    search_map: {
        'org_name':{
            label:'org_name',
            key:'org_num',
            value:'org_name'
        }
    },
    search_api: {
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