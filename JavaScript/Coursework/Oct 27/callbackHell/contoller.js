import * as model from "./model.js";
import * as view from "./view.js";

export function addPie(pie, cb) {
  model.addPie(pie, (addedPie, piesLength) => {
    view.newPie(addedPie, piesLength);
    cb();
  });
}

export function showPies(cb) {
  model.getPies((pies) => {
    view.showPies(pies, pies.length);
    cb();
  });
}
export function eatPie(chosenPie, cb) {}
// look at the model for clues about how to implement your callback function

