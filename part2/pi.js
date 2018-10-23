const { pow, sqrt } = Math;

const a = n => a.cache[n] = a.cache[n] || a.new(n);
a.cache = {};
a.new = n => n === 0 ? (6 - 4 * sqrt(2)) : a.rec(n);
a.rec = n => pow(1 + y(n), 4)*a(n - 1) - pow(2, 2*(n - 1)+3)*y(n)*(1 + y(n) + pow(y(n), 2));

const y = n => y.cache[n] = y.cache[n] || y.new(n);
y.cache = {};
y.new = n => n === 0 ? (sqrt(2) - 1) : y.rec(n);
y.rec = n => (1 - pow(1 - pow(y(n - 1), 4), 1/4)) / (1 + pow(1 - pow(y(n - 1), 4), 1/4));

console.log(1/a(4));
