var randomNo = function() {
  return Math.floor(Math.random() * 60) + 30
};

var handleRenderDataFabricApexChart = function () {
  // global apexchart settings
  Apex = {
    title: {
      style: {
        fontSize: "12px",
        fontWeight: "bold",
        fontFamily: app.font.family,
        color: app.color.white,
      },
    },
    legend: {
      fontFamily: app.font.family,
      labels: {
        colors: "#fff",
        show: true,
      },
    },
    tooltip: {
      style: {
        fontSize: "10px",
        fontFamily: app.font.family,
      },
    },
    grid: {
      borderColor: "rgba(" + app.color.whiteRgb + ", .25)",
    },
    dataLabels: {
      style: {
        fontSize: "12px",
        fontFamily: app.font.family,
        fontWeight: "bold",
        colors: undefined,
      },
    },
    xaxis: {
      axisBorder: {
        show: false,
        color: "rgba(" + app.color.whiteRgb + ", .25)",
        height: 1,
        width: "100%",
        offsetX: 0,
        offsetY: -1,
      },
      axisTicks: {
        show: false,
        borderType: "solid",
        color: "rgba(" + app.color.whiteRgb + ", .25)",
        height: 6,
        offsetX: 0,
        offsetY: 0,
      },
      labels: {
        style: {
          colors: "#fff",
          fontSize: "9px",
          fontFamily: app.font.family,
          fontWeight: 400,
          cssClass: "apexcharts-xaxis-label",
        },
      },
    },
    yaxis: {
//      min: 0,
//      max: 20,
      labels: {
        style: {
          colors: "#fff",
          fontSize: "9px",
          fontFamily: app.font.family,
          fontWeight: 400,
          cssClass: "apexcharts-xaxis-label",
        },
      },
    },
  };

// BEGIN databaseConnect-ColumChart
  var DatabaseConnectChartOptions = {
    chart: {
      height: 190,
      type: 'bar',
        toolbar: {
          show: false
        },
    },
    plotOptions: {
      bar: {
        columnWidth: '50%',
        distributed: true,
      }
    },
    legend: {
      show: false
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
        show: true,
        width: 1,
        colors: ['transparent']
    },
    colors: ["#f39c12", "#fdb43f", "#ffc365", "#c58a2e"],
    series: [{
      data: [41, 28, 36, 22]
    }],
    grid: {
        show: true
    },
    xaxis: {
      categories: ['Teradata', 'Postgres', 'ETC1', 'ETC2',],
      labels: {
        show: true,
        style: {
          colors: '#fff',
          fontSize: '9px',
          cssClass: 'apexcharts-xaxis-label',
        }
      }
    },
    yaxis: {
      labels: {
        show: true,
      }
    },
	fill: {
	  opacity: 1
	},
    tooltip: {
      theme: 'dark',
        x: {
          show: true,
        },
		y: {
	      title: {
		    formatter: function (seriesName) {
		    return ''
			}
		  },
	    formatter: (value) => { return '' + value },
	  }
    }
  }

    var databaseConnectChart = new ApexCharts(
      document.querySelector("#databaseConnectChart"),
      DatabaseConnectChartOptions
    );
    databaseConnectChart.render();
  // END databaseConnect-ColumChart
//--------------------------------------------------------------------------
  // BEGIN UserConnectChart
  var UserConnectChartOptions = {
//   BEGIN UserConnect-ColumChart
//    chart: {
//      height: 190,
//      type: 'bar',
//        toolbar: {
//          show: false
//        },
//    },
//    plotOptions: {
//      bar: {
//        columnWidth: '50%',
//        distributed: true,
//      }
//    },
//    legend: {
//      show: false
//    },
//    dataLabels: {
//      enabled: false
//    },
//    stroke: {
//        show: true,
//        width: 1,
//        colors: ['transparent']
//    },
//    colors: ["#c58a2e", "#ffc365", "#fdb43f", "#f39c12"],
//    series: [{
//      data: [4, 11, 8, 18]
//    }],
//    grid: {
//        show: true
//    },
//    xaxis: {
//      categories: ['User1', 'Admin', 'Guest', 'Manager'],
//      labels: {
//        show: true,
//        style: {
//          colors: '#fff',
//          fontSize: '9px',
//          cssClass: 'apexcharts-xaxis-label',
//        }
//      }
//    },
//    yaxis: {
//      labels: {
//        show: true,
//      }
//    },
//    fill: {
//      opacity: 1
//    },
//    tooltip: {
//      theme: 'dark',
//        x: {
//          show: true,
//        },
//        y: {
//          title: {
//            formatter: function (seriesName) {
//            return ''
//            }
//          },
//        formatter: (value) => { return '' + value },
//      }
//    }
  // END UserConnect-ColumChart
// ============================================================================
  // BEGIN UserConnect-BarChart
//    chart: {
//      height: 190,
//      type: 'bar',
//      toolbar: {
//        show: false
//      },
//    },
//    plotOptions: {
//      bar: {
//        horizontal: true,
//        distributed: true
//      },
//    },
//    legend : {
//      show: false
//    },
//    dataLabels: {
//      enabled: false
//    },
//    stroke: {
//      show: true,
//      width: 1,
//      colors: ['transparent']
//    },
//    colors: ["#f39c12", "#fdb43f", "#ffc365", "#c58a2e"],
//    series: [{
//      data: [4, 11, 8, 18]
//    }],
//    grid: {
//      show: true
//    },
//    xaxis: {
//      categories: ['Manager', 'Admin', 'Guest', 'Manager'],
//        labels: {
//          show: true,
//          style: {
//            colors: '#fff',
//              fontSize: '9px',
//              cssClass: 'apexcharts-xaxis-label',
//          },
//        offsetX: 30,
//        },
//    },
//    yaxis: {
//        labels: {
//            show: true,
//        }
//    },
//    fill: {
//        opacity: 1
//    },
//    tooltip: {
//      theme: 'dark',
//      x: {
//        show: true,
//      },
//      y: {
//            title: {
//                formatter: function (seriesName) {
//                    return ''
//                }
//            },
//            formatter: (value) => { return '' + value },
//      }
//    }
  // END UserConnect-BarChart
// ============================================================================
//   BEGIN UserConnect-DonutChart
      chart: {
        height: 170,
        type: 'donut',
      },
      animations: {
        enabled: true,
      },
    plotOptions: {
      pie: {
        dataLabels: {
          offset: 8
        },
      },
    },
    dataLabels: {
      enabled: true,
      formatter(val, opts) {
        const name = opts.w.globals.labels[opts.seriesIndex]
        return [val.toFixed(1) + '%']
      },
      style: {
        fontSize: '12px',
        colors: [app.color.white],
        fontWeight: 400
      },
    },
    stroke: {
      show: false
    },
    colors: ["#934903", "#b76306", "#db7f08", "#ff9f0c", "#ffbe48", "#ffd16d", "#ffe49d", "#fff3ce"],
    labels: ["User1","Admin","Guest","Manager"],
    series: [4, 11, 8, 18],
    tooltip: {
      theme: 'dark',
      x: {
        show: true
      },
      y: {
        title: {
          formatter: function (val) {
            return '' + val + "<br>" + " Count:"
          }
        },
        formatter: (value) => { return '' + value },
      }
    }
//   END UserConnect-DonutChart
  }
    var UserConnectChart = new ApexCharts(
      document.querySelector("#UserConnectChart"),
      UserConnectChartOptions
    );
    UserConnectChart.render();
  // END UserConnect-Chart
//--------------------------------------------------------------------------
  // BEGIN monitoring-LineChart
  var CpuUsageChartOptions = {
    series: [{
      name: "Teradata",
      data: [80, 90, 100, 70, 32, 60, 78]
    },
    {
      name: "Postgres",
      data: [69, 79, 85, 92, 83, 74, 99]
    },
    {
      name: "ETC1",
      data: [41, 62, 20, 50, 72, 69, 82]
    },
    {
      name: "ETC2",
      data: [85, 98, 69, 47, 87, 92, 100]
    }],
    chart: {
      height: 240,
      type: 'line',
      toolbar: {
        show: false
      },
      events: {
        mounted: (chart) => {
          chart.windowResizeHandler();
        }
      },
      zoom: {
        enabled: false
      },
    },
    colors: ['rgba(' + app.color.themeRgb + ', .95)', 'rgba(' + app.color.themeRgb + ', .70)',  'rgba(' + app.color.themeRgb + ', .45)',  'rgba(' + app.color.themeRgb + ', .20)'],
    dataLabels: {
      enabled: false,
    },
    legend : {
      show: false,
    },
    stroke: {
      curve: 'straight',
      width: 3
    },
    grid: {
      row: {
        colors: ['rgba(' + app.color.whiteRgb + ', .25)', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      }
    },
    markers: {
      size: 1
    },
    xaxis: {
      tooltip: {
        enabled: false,
      },
      labels: {
        show: true,
        formatter: function (val) {
          return 'Jan ' + Math.round(val) + 'st';
        }
      }
    },
    yaxis: {
      forceNiceScale: false,
      min: 0,
      max: 100,
      labels: {
        formatter: (value) => value.toFixed(0) +'%',
      },
    },
    tooltip: {
      theme: 'dark',
      x: {
        show: true
      },
      y: {
        title: {
          formatter: function (val) {
            return '' + val + " :"
          }
        },
        formatter: (value) => { return '' + value + '%' },
      }
    }
  };
  var CpuUsageChart = new ApexCharts(
    document.querySelector("#CpuUsageChart"),
    CpuUsageChartOptions
  );
  CpuUsageChart.render();
  // END monitoring-LineChart
};
/* Controller
------------------------------------------------ */
$(document).ready(function () {
	handleRenderDataFabricApexChart();
});