const Particle = class {
  constructor(game, p, speed) {
    this.game = game;
    this.p = p;
    this.speed = speed;
  }

  update(dt) {
    const modAcc = this.game.constants.alpha / this.p.squared();
    const acc = this.p.times(modAcc / this.p.mod());

    this.p = this.p.add(this.speed.times(dt)).add(acc.times((dt * dt) / 2));
    this.speed = this.speed.add(acc.times(dt));
  }

  render(canvas) {
    canvas.lineStyle(2, 0xfff4e6);
    canvas.drawCircle(
      this.game.width / 2 + this.p.x,
      this.game.height / 2 + this.p.y,
      1
    );
  }

  destroy() {
    const shouldDestroy =
      this.p.x < -(this.game.width / 2) ||
      this.p.y < -(this.game.height / 2) ||
      this.p.x > this.game.width / 2 ||
      this.p.y > this.game.height / 2;

    if (shouldDestroy) {
      this.runStats();
    }

    return shouldDestroy;
  }

  runStats() {
    this.game.stats.total += 1;
    this.game.stats.hits += this.isHit() ? 1 : 0;
  }

  isHit() {
    return Math.abs(this.p.y) < this.game.constants.dy;
  }
};
