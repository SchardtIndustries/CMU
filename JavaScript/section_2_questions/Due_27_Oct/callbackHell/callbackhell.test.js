import { jest } from '@jest/globals';

import * as controller from "./controller.js";

describe("callbackhell.js integration", () => {
  test("controller.showPies is callable and runs callback", (done) => {
    controller.showPies(() => {
      done();
    });
  });

  test("controller.addPie adds and calls callback", (done) => {
    controller.addPie("banana", () => {
      done();
    });
  });

  test("controller.eatPie gracefully handles non-existent pie", (done) => {
    controller.eatPie("ghost", () => {
      done();
    });
  });
});
