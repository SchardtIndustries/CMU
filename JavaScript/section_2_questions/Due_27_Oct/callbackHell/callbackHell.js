import * as readline from "node:readline";
import { stdin as input, stdout as output } from "node:process";
import * as controller from "./contoller.js";

const rl = readline.createInterface({ input, output });

function welcome() {
  rl.question("Welcome to the pie cli, press any key to contine", (_ans) => {
    interact();
  });
}
welcome();

function cleanInput(input) {
  return input.trim().toLowerCase();
}

function interact() {
  rl.question(
    "Would you like to BAKE a pie, VIEW all pies, or EAT a pie?\n",
    (answer) => {
      const cleanedInput = cleanInput(answer);
      switch (cleanedInput[0]) {
        case "b":
          bakeInteraction();
          break;
        case "v":
          controller.showPies(() => {
            interact();
          });
          break;
        case "e":
          eatInteraction();
          break;
        default:
          console.log("I didn't understand the input");
          interact();
      }
    }
  );
}

function bakeInteraction() {
  rl.question("What kind of pie will you bake?\n", (answer) => {
    const freshPie = cleanInput(answer);
    controller.addPie(freshPie, () => interact());
  });
}

function eatInteraction() {
  controller.showPies(() => {
    rl.question("So thems the pies, which will you have?\n", (answer) => {
      const chosenPie = cleanInput(answer);
      controller.eatPie(chosenPie, () => {
        interact();
      });
    });
  });
}
