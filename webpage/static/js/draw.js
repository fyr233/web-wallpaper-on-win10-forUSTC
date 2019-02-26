// 基于准备好的dom，初始化echarts实例
var Chart_test1 = echarts.init(document.getElementById('test1'), 'mydark');
var Chart_showtime = echarts.init(document.getElementById('clock'), 'mydark');

// 指定图表的配置项和数据

// 使用刚指定的配置项和数据显示图表。
Chart_test1.setOption(option = {
    title: {
        text: 'ECharts 入门示例',
        textStyle:{
            fontSize: 30,
            fontFamily: "'Microsoft YaHei', '微软雅黑', Arial, Verdana, 'sans-serif'",
        },
        left: 'center',
    },
    tooltip: {},
    /*legend: {
        data:['销量'],
        left: 'center',
    },*/
    xAxis: {
        data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
    },
    yAxis: {},
    animation: false,
    series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
});


var date = new Date();
Chart_showtime.setOption(option = {
    title: {
        textStyle:{
            fontSize: 110,
            fontFamily: "'Microsoft YaHei', '微软雅黑', Arial, Verdana, 'sans-serif'",
        },
        left: 'center',
        top: "center",
        text: date.toLocaleTimeString().slice(0,-3),
        borderRadius: [5, 5, 0, 0]
    },
});