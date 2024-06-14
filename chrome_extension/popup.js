// document.getElementById('askButton').addEventListener('click', () => {
//   const question = document.getElementById('question').value;
//
//   chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
//     chrome.tabs.sendMessage(tabs[0].id, { action: "extractContent" }, (response) => {
//       if (response && response.content) {
//         fetch('http://localhost:5000/ask', {
//           method: 'POST',
//           headers: { 'Content-Type': 'application/json' },
//           body: JSON.stringify({ content: response.content, question: question })
//         })
//         .then(res => res.json())
//         .then(data => {
//           document.getElementById('answer').innerText = data.answer;
//         });
//       }
//     });
//   });
// });
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('askButton').addEventListener('click', () => {
    const question = document.getElementById('question').value;

    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, { action: "extractContent" }, (response) => {
        if (chrome.runtime.lastError) {
          console.error(chrome.runtime.lastError);
          return;
        }
        if (response && response.content) {
          fetch('http://localhost:5000/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ content: response.content, question: question })
          })
          .then(res => res.json())
          .then(data => {
            document.getElementById('answer').innerText = data.answer;
          });
        }
      });
    });
  });
});
// Get the container element
var container = document.getElementById("container");

// Variables to store mouse position during drag
var offsetX, offsetY;

// Function to handle mouse down event
function dragMouseDown(e) {
  e.preventDefault();

  // Calculate the initial mouse cursor position
  offsetX = e.clientX - container.getBoundingClientRect().left;
  offsetY = e.clientY - container.getBoundingClientRect().top;

  // Call a function whenever the cursor moves
  document.addEventListener('mousemove', dragElement);

  // Stop moving when mouse button is released
  document.addEventListener('mouseup', closeDragElement);
}

// Function to move the container element
function dragElement(e) {
  e.preventDefault();

  // Calculate the new cursor position
  var newX = e.clientX - offsetX;
  var newY = e.clientY - offsetY;

  // Set the new position of the container
  container.style.left = newX + "px";
  container.style.top = newY + "px";
}

// Function to stop moving when mouse button is released
function closeDragElement() {
  // Stop moving the container when mouse button is released
  document.removeEventListener('mousemove', dragElement);
  document.removeEventListener('mouseup', closeDragElement);
}

// Event listener for when mouse button is pressed down on the container
container.addEventListener('mousedown', function(e) {
  // Check if the mousedown event originated from within the input element
  if (e.target.id === 'question') {
    return; // Don't initiate drag if mousedown was on the input field
  }

  // Otherwise, initiate drag
  dragMouseDown(e);
});
