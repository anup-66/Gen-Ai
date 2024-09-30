// // document.getElementById('askButton').addEventListener('click', () => {
// //   const question = document.getElementById('question').value;
// //
// //   chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
// //     chrome.tabs.sendMessage(tabs[0].id, { action: "extractContent" }, (response) => {
// //       if (response && response.content) {
// //         fetch('http://localhost:5000/ask', {
// //           method: 'POST',
// //           headers: { 'Content-Type': 'application/json' },
// //           body: JSON.stringify({ content: response.content, question: question })
// //         })
// //         .then(res => res.json())
// //         .then(data => {
// //           document.getElementById('answer').innerText = data.answer;
// //         });
// //       }
// //     });
// //   });
// // });
// document.addEventListener('DOMContentLoaded', function() {
//   document.getElementById('askButton').addEventListener('click', () => {
//     const question = document.getElementById('question').value;
//
//     chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
//       chrome.tabs.sendMessage(tabs[0].id, { action: "extractContent" }, (response) => {
//         // if (chrome.runtime.lastError) {
//         //   console.error(chrome.runtime.lastError);
//         //   return;
//         // }
//         if (response && response.content) {
//           fetch('http://localhost:5000/ask', {
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify({ content: response.content, question: question })
//           })
//           .then(res => res.json())
//           .then(data => {
//             document.getElementById('answer').innerText = data.answer;
//           });
//         }
//       });
//     });
//   });
// })


document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('askButton').addEventListener('click', () => {
    const question = document.getElementById('question').value;
    console.log(question);

    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, { action: "extractContent" }, (response) => {
        if (response && response.content) {
          fetch('http://localhost:5000/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ content: response.content, question: question })
          })
          .then(res => res.json())
          .then(data => {
            document.getElementById('answer').innerText = data.answer;
          })
          .catch(error => {
            console.error('Error:', error);
            document.getElementById('answer').innerText = 'Error fetching answer';
          });
        } else {
          console.error('No content received');
          document.getElementById('answer').innerText = 'Error: No content received';
        }
      });
    });
  });
});
