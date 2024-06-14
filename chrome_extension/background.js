chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: extractContent
  }, (results) => {
    if (results && results[0] && results[0].result) {
      const content = results[0].result;
      console.log('Page content:', content);
      // Send the content to your server or LLM for processing
    }
  });
});

