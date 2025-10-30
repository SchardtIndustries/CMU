import { jest } from '@jest/globals';

import * as view from "./view.js";

describe("view.js", () => {
  let logSpy;

  beforeEach(() => {
    logSpy = jest.spyOn(console, "log").mockImplementation(() => {});
  });

  afterEach(() => {
    logSpy.mockRestore();
  });

  test("newPie logs baking message", () => {
    view.newPie("apple", 2);
    expect(logSpy).toHaveBeenCalledWith(expect.stringMatching(/apple/));
  });

  test("showPies logs available pies", () => {
    view.showPies(["apple", "berry"], 2);
    expect(logSpy).toHaveBeenCalledWith(expect.stringMatching(/apple/));
  });

  test("atePie logs correct message", () => {
    view.atePie("apple");
    expect(logSpy).toHaveBeenCalledWith(expect.stringMatching(/ate/));
  });

  test("noSuchPie logs correct message", () => {
    view.noSuchPie("pumpkin");
    expect(logSpy).toHaveBeenCalledWith(expect.stringMatching(/pumpkin/));
  });
});
