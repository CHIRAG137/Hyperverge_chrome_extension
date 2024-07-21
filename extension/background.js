/**
 * Handles the `onInstalled` event of the Chrome extension.
 * This event is fired when the extension is installed or updated.
 *
 * When the extension is installed or updated, a new tab is created with a specific URL.
 */
chrome.runtime.onInstalled.addListener(() => {
    // Create a new tab with the URL of the API endpoint for notices
    chrome.tabs.create({ url: "http://127.0.0.1:8000/api/notice/" });
});
