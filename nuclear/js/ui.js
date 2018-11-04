const UI = app => {
    const sheet = PIXI.loader.resources.sprites.spritesheet;

    const options = new PIXI.Text('Options', STYLES.title);
    options.x = SIZE + 2*MARGIN;
    options.y = MARGIN;
    app.stage.addChild(options);

    const time = new PIXI.Text('Time', STYLES.small);
    time.x = SIZE + 2*MARGIN;
    time.y = MARGIN + options.height + SM;
    app.stage.addChild(time);

    const p = new Point(SIZE + 2*MARGIN, time.y + SM + time.height);
    const d = new Point(16.0 + SM, 0);
    new Button(sheet, p.add(d.times(0)), 'stop', () => game.speed = 0).add(app);
    new Button(sheet, p.add(d.times(1)), 'play', () => game.speed = 1).add(app);
    new Button(sheet, p.add(d.times(2)), 'fast', () => game.speed = 10).add(app);

    const flow = new PIXI.Text('Flow', STYLES.small);
    flow.x = SIZE + 2*MARGIN;
    flow.y = p.y + SM + 16.0;
    app.stage.addChild(flow);

    const p2 = new Point(SIZE + 2*MARGIN, flow.y + SM + flow.height);
    new Button(sheet, p2.add(d.times(0)), 'pause', () => game.repeat = false).add(app);
    new Button(sheet, p2.add(d.times(1)), 'single', () => game.create()).add(app);
    new Button(sheet, p2.add(d.times(2)), 'repeat', () => game.repeat = true).add(app);
};