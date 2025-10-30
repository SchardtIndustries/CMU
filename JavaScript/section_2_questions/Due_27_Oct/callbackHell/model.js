const pies = ["tomatillo"]; // our in memory database

function randomDelay(callback) {
  setTimeout(function timedOut() {
    callback();
  }, Math.random() * 2000);
}

export function addPie(pie, cb) {
  randomDelay(() => {
    pies.push(pie);
    cb(pie, pies.length);
  });
}

export function getPies(cb) {
  randomDelay(() => {
    cb(pies);
  });
}

// NEW: error-first delete (eat) a pie
export function deletePie(chosenPie, cb) {
  randomDelay(function () {
    const idx = pies.indexOf(chosenPie);
    if (idx === -1) {
      // error-first: pass an Error as first arg
      return cb(new Error("No such pie: " + chosenPie));
    }
    const [eaten] = pies.splice(idx, 1);
    cb(null, eaten, pies.length); // success path: err=null
  });
}
