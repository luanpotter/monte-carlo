const FormComponents = (() => {
    const Component = class {
        build(stage, x, y) {
            this.c.x = x;
            this.c.y = y;
            stage.append(this.c);
        }

        width() {
            return this.c.width;
        }

        height() {
            return this.c.height;
        }
    };

    const Label = class extends Component {
        constructor(text, style = STYLES.small) {
            this.c = new PIXI.Text(text, style)
        }
    }

    const Button = class extends Component {
        constructor(sheet, name, click) {
            this.c = new PIXI.Sprite(sheet.textures[`${name}.png`]);
            if (click) {
                this.c.on('pointerdown', click);
                this.c.interactive = true;
                this.c.buttonMode = true;
            }
        }
    };

    const Row = class {
        constructor(elements, m = SM, em = 0) {
            this.elements = elements;
            this.m = m;
            this.em = em;
            this._width = 2 * this.em - this.m + this.elements.reduce((total, el) => total + el.width() + this.m);
            this._height = 2 * this.em + this.elements.map(el => el.height()).reduce(Math.max);
        }

        width() {
            return this._width;
        }

        height() {
            return this._height;
        }

        build(stage, x, y) {
            let cX = x + em;
            this.elements.forEach(el => {
                el.x = cX;
                el.y = y;
                cX += el.width() + m;
                stage.addChild(el);
            });
        }
    }

    const Column = class {
        constructor(elements, m = SM, em = 0) {
            this.elements = elements;
            this.m = m;
            this.em = em;
            this._width = 2 * this.em + this.elements.map(el => el.width()).reduce(Math.max);
            this._height = 2 * this.em + - this.m + this.elements.reduce((total, el) => total + el.height() + this.m);
        }

        width() {
            return this._width;
        }

        height() {
            return this._height;
        }

        build(stage, x, y) {
            let cY = y + em;
            this.elements.forEach(el => {
                el.x = x;
                el.y = cY;
                cY += el.height() + m;
                stage.addChild(el);
            });
        }
    };
    return { Component, Column, Row, Label, Button };
})();