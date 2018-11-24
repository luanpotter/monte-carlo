const { build, plot } = require('./plotly.js');

const xs = Array(1000).fill().map((_, i) => i / 1000);
const h = x => 10 * Math.sin(x*10)**2 + (x + 2)**3;

const pt = build();
plot(pt, {
	data: xs,
	title: 'x',
}, {
	data: xs.map(h),
	title: 'f(x)',
}, 'h_x', () => console.log('h done'));
