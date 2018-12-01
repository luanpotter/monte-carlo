// const { build, plot } = require('./plotly.js');
const { plot } = require('./chart.js');

const xs = Array(1000).fill().map((_, i) => i / 1000);
const f = x => (62/3 - 5*Math.log(40))**(-1)*(15 + 2*x**2 - 5*Math.log(10 + x*10));

plot(xs, xs.map(f));
