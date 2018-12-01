const ChartjsNode = require('chartjs-node');

const plot = (xs, ys) => {
    const chartNode = new ChartjsNode(800, 600);
    return chartNode.drawChart(options(xs, ys))
        .then(() => chartNode.getImageBuffer('image/png'))
        .then(() => chartNode.writeImageToFile('image/png', './result.png'))
        .then(() => chartNode.destroy());
};

const options = (xs, ys) => ({
    type: 'line',
    data: {
        datasets: [{
            borderColor: 'rgba(0, 0, 0, 255)',
            backgroundColor: 'rgba(0, 0, 0, 255)',
            fill: false,
            showLine: true,
            pointBorderWidth: 0,
            label: 'f(x)',
            borderWidth : 2,
            data: ys,
        }],
    },
    options: {
        elements: { point: { radius: 0 } },
        legend: {
            display: false
        },
        scales: {
            xAxes: [{
                type: 'category',
                labels: xs,
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'x',
                },
                ticks: {
                    autoSkip: true,
                    autoSkipPadding: 20,
                }
            }],
            yAxes: [{
                type: 'linear',
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'f(x)',
                },
                ticks: {
                    beginAtZero: true,
                }
            }],
        },
    },
});

module.exports = { plot };