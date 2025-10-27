# Callback Hell in the Pie CLI

We're taking control flow back to days before ES6 introduced promises.

You are given a pie CLI app with two features already implemented: baking and viewing pies.
Your task is to implement a feature to allow users to EAT a pie.
You're given function signatures for the functions you're expected to implement in the controller, model, and view modules.

- Follow the calling conventions and flow demonstrated in the other features
- You must handle the case where the requested pie is not available by
  1. Using an error first callback to pass the error between the modules
  1. invoking view.noSuchPie if there is an error
  1. invoking view.atePie if the pie is available to be eaten
- This is ✨callback hell✨, so Promises and async/await are _strictly_ forbidden!
