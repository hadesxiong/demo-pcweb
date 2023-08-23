// 用于监听echarts的宽度变化造成的自适应问题

export function echartsResize(echart,mychart) {
    const elementResizeDetecotrMaker = require('element-resize-detector');
    const erd = elementResizeDetecotrMaker();
    erd.listenTo(echart,function() {
        mychart.resize();
    })
}