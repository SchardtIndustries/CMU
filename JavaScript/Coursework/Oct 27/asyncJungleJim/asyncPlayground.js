// Redefine the methods of the fun object with methods from the functions object
// such that the numbers print out in order

const functions = {
  timeout1000: function (x) {
    setTimeout(() => {
      console.log(x);
    }, 1000);
  },
  timeout0: function (x) {
    setTimeout(() => {
      console.log(x);
    });
  },
  resolved1000: function (x) {
    setTimeout(() => {
      Promise.resolve(true).then(console.log(x));
    }, 1000);
  },
  resolved0: function (x) {
    Promise.resolve(true).then(console.log(x));
  },
  placeholder: function (x) {
    console.log(x);
  },
};

// Redefine this object so the logs print in order
const fun = {
  foo: functions.placeholder,
  bar: functions.placeholder,
  baz: functions.placeholder,
  qux: functions.placeholder,
};
//Only redefine the above object

const tmnt = {
  raphael: function () {
    setTimeout(() => {
      fun.foo(9);
      fun.qux(6);
    }, 1000);
  },
  michelangelo: function () {
    fun.foo(5);
    fun.bar(3);
    fun.qux(2);
  },
  leonardo: function () {
    console.log(1);
    Promise.resolve(true).then(fun.foo(4));
  },
  donatello: function (fn) {
    fun.baz(7);
    setTimeout(() => {
      fn(8);
    }, 1000);
  },
};

tmnt.leonardo();
tmnt.michelangelo();
tmnt.raphael();
tmnt.donatello(fun.qux);
