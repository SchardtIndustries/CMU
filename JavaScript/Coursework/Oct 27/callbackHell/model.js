const pies = ["tomatillo"]; // our in memory database

function randomDelay(callback) {
  // simulates network call to a real database so we have a reason to need callbacks
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

export function deletePie(chosenPie, cb) {}
// pass this function a 2-parameter, error-first callback // (err, data)=>{}
// to handle the exceptional case if the pie isn't in the pies array
// or the happy path if such a pie is available

