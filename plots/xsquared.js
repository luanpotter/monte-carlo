const { build, plot } = require('./plotly.js');

const xs = Array(1000).fill().map((_, i) => i / 1000);
const g = x => 3 * x * x;

const pt = build();
plot(pt, {
	data: xs,
	title: 'x',
}, {
	data: xs.map(g),
	title: 'g(x)',
}, 'g_x', () => console.log('g done'));

const f = x => 1;

plot(pt, {
	data: xs,
	title: 'u',
}, {
	data: xs.map(f),
	title: 'f(u)',
}, 'f_u', () => console.log('f done'));