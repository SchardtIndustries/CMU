import { jest } from "@jest/globals";

jest.useFakeTimers();

describe("async playground (ordered logging)", () => {
  let output = [];
  const consoleSpy = jest.spyOn(console, "log").mockImplementation((x) => output.push(x));

  const functions = {
    timeout1000(x) {
      setTimeout(() => console.log(x), 1000);
    },
    timeout0(x) {
      setTimeout(() => console.log(x));
    },
    resolved1000(x) {
      setTimeout(() => Promise.resolve(true).then(() => console.log(x)), 1000);
    },
    resolved0(x) {
      Promise.resolve(true).then(() => console.log(x));
    },
    placeholder(x) {
      console.log(x);
    },
  };

  const fun = {
    foo: functions.timeout1000,
    bar: functions.timeout0,
    baz: functions.timeout1000,
    qux: functions.placeholder,
  };

  const tmnt = {
    raphael() {
      setTimeout(() => {
        fun.foo(9);
        fun.qux(6);
      }, 1000);
    },
    michelangelo() {
      fun.foo(5);
      fun.bar(3);
      fun.qux(2);
    },
    leonardo() {
      console.log(1);
      Promise.resolve(true).then(() => fun.foo(4));
    },
    donatello(fn) {
      fun.baz(7);
      setTimeout(() => fn(8), 1000);
    },
  };

  test("numbers print in correct order", () => {
    output = [];
    tmnt.leonardo();
    tmnt.michelangelo();
    tmnt.raphael();
    tmnt.donatello(fun.qux);

    jest.runAllTimers();

    expect(output).toEqual([1, 2, 3, 5, 6, 7, 8, 9]);
    consoleSpy.mockRestore();
  });
});
