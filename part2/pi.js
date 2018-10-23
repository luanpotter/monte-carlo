const a = n => a.cache[n] = a.cache[n] || a.new(n);
a.cache = {};
a.new = n => n === 0 ? (6 - 4 * Math.sqrt(2)) : a.rec(n);
a.rec = n => Math.pow(1 + y(n), 4)*a(n - 1) - Math.pow(2, 2*(n - 1)+3)*y(n)*(1 + y(n) + Math.pow(y(n), 2));

const y = n => y.cache[n] = y.cache[n] || y.new(n);
y.cache = {};
y.new = n => n === 0 ? (Math.sqrt(2) - 1) : y.rec(n);
y.rec = n => (1 - Math.pow(1 - Math.pow(y(n - 1), 4), 1/4)) / (1 + Math.pow(1 - Math.pow(y(n - 1), 4), 1/4));

console.log(1/a(10));
