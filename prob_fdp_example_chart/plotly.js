const os = require('os');
const fs = require('fs');

const plotly = require('plotly');
const request = require('request');

const download = (uri, filename, callback) => {
    request.head(uri, (err, res, body) => {
        const r = request(uri).pipe(fs.createWriteStream(filename));
        if (callback) {
            r.on('close', callback);
        }
    });
};

const build = () => {
	const plotlyData = os.homedir() + '/.plotly.data';
	const data = fs.readFileSync(plotlyData, 'UTF-8');
	const parts = data.trim().split(':');
	return plotly(parts[0], parts[1]);
};

const plot = (plotly, x, y, name, cb) => {
    const data = [{
        x: x.data,
        y: y.data,
        name: 'Data',
        mode: 'lines',
        type: 'scatter',
        line: {
            color: '#000000',
            width: 2,
        }
    }];

    const graphOptions = {
        filename: 'chart-test-' + name,
        fileopt: 'overwrite',
        layout: {
            xaxis: {
                title: x.title,
                color: '#000000',
            },
            yaxis: {
                title: y.title,
                color: '#000000',
            },
        },
    };
    plotly.plot(data, graphOptions, (error, data) => {
		if (error) console.error(error);
		download(data.url + '.png', name + '.png', cb);
	});
};

module.exports = { build, plot, download };