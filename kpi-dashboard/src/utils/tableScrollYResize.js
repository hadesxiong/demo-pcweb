// 提供一个方法用来调整表格的scroll.y

export function tableScrollYResize(doc_id,obj) {
    // const viewHeight = window.innerHeight || document.documentElement.clientHeight;
    const conHeight = document.getElementById(doc_id).clientHeight
    const headHeight = 46;
    const scrolly = conHeight - headHeight - 4;
    console.log(conHeight,scrolly);
    obj['y'] = scrolly
}
