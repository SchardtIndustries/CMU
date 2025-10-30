import { jest } from "@jest/globals";

// Manual ESM mocks
const model = {
  addPie: jest.fn(),
  getPies: jest.fn(),
  deletePie: jest.fn(),
};
const view = {
  newPie: jest.fn(),
  showPies: jest.fn(),
  atePie: jest.fn(),
  noSuchPie: jest.fn(),
};

jest.unstable_mockModule("./model.js", () => model);
jest.unstable_mockModule("./view.js", () => view);

// ✅ Dynamically import controller after mocks
const { addPie, showPies, eatPie } = await import("./controller.js");

describe("controller.js", () => {
  beforeEach(() => jest.clearAllMocks());

  test("addPie calls model and view correctly", () => {
    model.addPie.mockImplementation((_p, cb) => cb("apple", 2));
    const cb = jest.fn();
    addPie("apple", cb);
    expect(view.newPie).toHaveBeenCalledWith("apple", 2);
    expect(cb).toHaveBeenCalled();
  });

  test("showPies calls model and view", () => {
    model.getPies.mockImplementation((cb) => cb(["apple"]));
    const cb = jest.fn();
    showPies(cb);
    expect(view.showPies).toHaveBeenCalledWith(["apple"], 1);
    expect(cb).toHaveBeenCalled();
  });

  test("eatPie handles happy path", () => {
    model.deletePie.mockImplementation((_p, cb) => cb(null, "apple"));
    const cb = jest.fn();
    eatPie("apple", cb);
    expect(view.atePie).toHaveBeenCalledWith("apple");
    expect(cb).toHaveBeenCalled();
  });

  test("eatPie handles missing pie", () => {
    model.deletePie.mockImplementation((_p, cb) => cb(new Error("not found")));
    const cb = jest.fn();
    eatPie("ghost", cb);
    expect(view.noSuchPie).toHaveBeenCalledWith("ghost");
    expect(cb).toHaveBeenCalled();
  });
});
