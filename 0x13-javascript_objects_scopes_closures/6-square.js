#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
class Square1 extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c) super.print(c); else super.print();
  }
};
