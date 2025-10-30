import { faker } from "@faker-js/faker";
import arrayShuffle from "array-shuffle";
import fs from "fs";

const allStudents = [];
for (let i = 0; i < 35; i++) {
  allStudents.push(faker.person.fullName());
}
const drops = allStudents.slice(0, 5);
const adds = allStudents.slice(-3);
const consistent = allStudents.slice(5, -3);

function formatList(students) {
  return students.join("\n");
}
function writeError(err) {
  if (err) console.error(err);
}
fs.writeFile("dropsKey", formatList(drops), writeError);
fs.writeFile("addsKey", formatList(adds), writeError);
fs.writeFile(
  "before",
  formatList(arrayShuffle(drops.concat(consistent))),
  writeError
);
fs.writeFile(
  "after",
  formatList(arrayShuffle(adds.concat(consistent))),
  writeError
);
