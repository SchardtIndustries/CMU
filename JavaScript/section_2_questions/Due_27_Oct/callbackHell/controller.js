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

// NEW: eat a pie using error-first callbacks
export function eatPie(chosenPie, cb) {
  model.deletePie(chosenPie, function (err, eatenPie /*, piesLength */) {
    if (err) {
      // pie not found
      view.noSuchPie(chosenPie);
      return cb();
    }
    // success
    view.atePie(eatenPie);
    cb();
  });
}
