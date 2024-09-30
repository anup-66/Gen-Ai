
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "extractContent") {
    // const content = document.body.innerText || document.body.textContent;
    const importantTags = ['main', 'article', 'section', 'div', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'];
    let content = '';

    importantTags.forEach(tag => {
      document.querySelectorAll(tag).forEach(element => {
        // Check if the element is visible
        if (element.offsetParent !== null && element.innerText.trim().length > 0) {
          content += element.innerText.trim() + '\n\n';
        }
      });
    });
    sendResponse({ content: content });
  }
});
