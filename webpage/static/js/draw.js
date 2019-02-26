// 基于准备好的dom，初始化echarts实例
var Chart_test1 = echarts.init(document.getElementById('test1'), 'mydark');
var Chart_showtime = echarts.init(document.getElementById('clock'), 'mydark');
var Chart_netspeed = echarts.init(document.getElementById('netspeed'), 'mydark');

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
        padding: 15,
        text: date.toLocaleTimeString().slice(0,-3),
        borderRadius: [5, 5, 0, 0]
    },
});

Chart_netspeed.setOption(option = {
    title : {
        text: '网\n速',
        textStyle:{
            fontSize: 60,
            fontFamily: "'Microsoft YaHei', '微软雅黑', Arial, Verdana, 'sans-serif'",
        },
        padding: 20
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:['网速', '', 'ping-baidu.com', '', 'ping-ustc.edu.cn'],
        textStyle:{
            fontSize: 25,
            fontFamily: "'Microsoft YaHei', '微软雅黑', Arial, Verdana, 'sans-serif'",
        },
        padding: 10
    },
    calculable : true,
    grid:{
        //x:100,
        y:140,
        width:1100,
        height:400,
    },
    xAxis : [
        {
            type : 'category',
            // x轴的字体样式
            axisLabel: {        
                show: true,
                textStyle: {
                    color: '#EEEEEE',
                    fontSize:16
                }
            },
            boundaryGap : false,
            data : netspeeddata['time']
        }
    ],
    yAxis : [
        {
            name: 'Mbps',
            type: 'value',
            axisLabel: {        
                show: true,
                textStyle: {
                    color: '#EEEEEE',
                    fontSize:16
                }
            },
        },
        {
            name: 'ms',
            type: 'value',
            axisLabel: {        
                show: true,
                textStyle: {
                    color: '#EEEEEE',
                    fontSize:16
                }
            },
        }
    ],
    animation: false,
    series : [
        {
            name:'网速',
            type:'line',
            yAxisIndex: 0,
            smooth:true,
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: netspeeddata['speed']
        },
        {
            name:'ping-baidu.com',
            type:'line',
            yAxisIndex: 1,
            smooth:true,
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: netspeeddata['ping']['baidu.com']
        },
        {
            name:'ping-ustc.edu.cn',
            type:'line',
            yAxisIndex: 1,
            smooth:true,
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: netspeeddata['ping']['ustc.edu.cn']
        }
    ]
});
                    