# List Item HTML

In this activity we will render an unordered list in the DOM to hold each element in the `todos` array.

## Instructions

Open [index.js](Unsolved/index.js) and add code to the `renderTodos` function to accomplish the following:

1. In `index.html`, there is a DOM element with an `id` of `todo-list`. In `index.js`, store a reference to the DOM element into a variable named `todoList`. Accomplish this using the `document.querySelector` method. 

2. Using a for-loop, iterate through each object in the `todos` array.

3. On each iteration of the loop, use `document.createElement` to create a new `todoListItem`.

4. Set the `innerHTML` property of each `todoListItem` equal to the `text` property of the "current" `todo` item from the list.

5. Finally, use `appendChild`  to add the `todoListItem` as a child of the `todoList` element.

## Hints

* Check out [MDN's Docs on Element.innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)

* Check out [MDN's Docs on document.querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)

* Check out [MDN's Docs on document.createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
