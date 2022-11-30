#!/usr/bin/node
exports.converter = function (base) {
  return (numb) => {
    return numb.toString(base);
  };
};
