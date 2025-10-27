function ordinal(n) {
  let suffix;
  switch (n) {
    case 1:
      suffix = "st";
      break;
    case 2:
      suffix = "nd";
      break;
    case 3:
      suffix = "rd";
      break;
    default:
      suffix = "th";
  }
  return n + suffix;
}

export function newPie(addedPie, piesLength) {
  console.log(
    `we baked you a ${addedPie} pie and it's the ${ordinal(piesLength)} pie`
  );
}

export function showPies(allPies, piesLength) {
  console.log(
    `we have ${piesLength} pie${
      piesLength != 1 ? "s" : ""
    } available:\n${allPies.join("\n")}`
  );
}
export function atePie(eatenPie) {}
export function noSuchPie(requestedPie) {}

