import { jest } from '@jest/globals';

import * as model from "./model.js";

describe("model.js", () => {
  beforeEach(() => {
    jest.useFakeTimers();
  });

  test("addPie pushes pie", () => {
    const cb = jest.fn();
    model.addPie("apple", cb);
    jest.runAllTimers();
    expect(cb).toHaveBeenCalledWith("apple", expect.any(Number));
  });

  test("getPies returns array", () => {
    const cb = jest.fn();
    model.getPies(cb);
    jest.runAllTimers();
    expect(cb).toHaveBeenCalledWith(expect.any(Array));
  });

  test("deletePie removes and returns pie", (done) => {
    model.addPie("berry", () => {
      model.deletePie("berry", (err, pie) => {
        expect(err).toBeNull();
        expect(pie).toBe("berry");
        done();
      });
      jest.runAllTimers();
    });
    jest.runAllTimers();
  });

  test("deletePie calls error callback when not found", (done) => {
    model.deletePie("ghost", (err, pie) => {
      expect(err).toBeInstanceOf(Error);
      expect(pie).toBeUndefined();
      done();
    });
    jest.runAllTimers();
  });
});
