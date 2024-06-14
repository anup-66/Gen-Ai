// Extract text content from the web page
function extractContent() {
  return document.body.innerText;
}

// Listen for messages from the background script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "extractContent") {
    const content = extractContent();
    sendResponse({ content: content });
  }
});
