/**
 * Initializes the page by setting up event listeners and loading initial data.
 */
document.addEventListener("DOMContentLoaded", () => {
    // Load existing notices and polls
    loadNotices();
    loadPolls();
  
    // Setup event handlers for forms
    document
      .getElementById("createNoticeForm")
      .addEventListener("submit", handleNoticeSubmit);
    document
      .getElementById("createPollForm")
      .addEventListener("submit", handlePollSubmit);
    document
      .getElementById("createIssueForm")
      .addEventListener("submit", handleIssueSubmit);
  
    // Initialize Pomodoro Timer and chat functionality
    initializePomodoroTimer();
    initializeChat();
  
    /**
     * Handles the submission of the notice creation form.
     * Submits notice data to the server and updates the notice list.
     * @param {Event} event - The form submit event.
     */
    async function handleNoticeSubmit(event) {
      event.preventDefault();
      const title = document.getElementById("title").value;
      const message = document.getElementById("message").value;
  
      const response = await fetch("http://127.0.0.1:8000/api/notice/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, message }),
      });
  
      if (response.ok) {
        const notice = await response.json();
        addNoticeToList(notice);
        document.getElementById("createNoticeForm").reset();
      }
    }
  
    /**
     * Handles the submission of the poll creation form.
     * Submits poll data to the server and updates the poll list.
     * @param {Event} event - The form submit event.
     */
    async function handlePollSubmit(event) {
      event.preventDefault();
      const title = document.getElementById("pollTitle").value;
      const optionsText = document
        .getElementById("pollOptions")
        .value.split(",")
        .map((option) => option.trim());
      const options = optionsText.map((optionText) => ({
        option_text: optionText,
      }));
  
      const response = await fetch("http://127.0.0.1:8000/api/poll/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, options }),
      });
  
      if (response.ok) {
        const poll = await response.json();
        addPollToList(poll);
        document.getElementById("createPollForm").reset();
      }
    }
  
    /**
     * Handles the submission of the issue creation form.
     * Submits issue data to the server and updates the issue list.
     * @param {Event} event - The form submit event.
     */
    async function handleIssueSubmit(event) {
      event.preventDefault();
      const title = document.getElementById("issueTitle").value;
      const description = document.getElementById("issueDescription").value;
  
      const response = await fetch("http://127.0.0.1:8000/api/issues/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, description }),
      });
  
      if (response.ok) {
        const issue = await response.json();
        addIssueToList(issue);
        document.getElementById("createIssueForm").reset();
      }
    }
  
    /**
     * Initializes the Pomodoro Timer functionality.
     */
    function initializePomodoroTimer() {
      let timer;
      let minutes = 25;
      let seconds = 0;
  
      /**
       * Updates the timer display on the page.
       */
      function updateTimerDisplay() {
        document.getElementById("timerDisplay").textContent = `${String(
          minutes
        ).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
      }
  
      /**
       * Starts the Pomodoro timer.
       */
      function startTimer() {
        if (timer) clearInterval(timer);
        timer = setInterval(() => {
          if (seconds === 0) {
            if (minutes === 0) {
              clearInterval(timer);
              alert("Pomodoro session ended!");
              return;
            }
            minutes--;
            seconds = 59;
          } else {
            seconds--;
          }
          updateTimerDisplay();
        }, 1000);
      }
  
      /**
       * Resets the Pomodoro timer based on the selected timer type.
       */
      function resetTimer() {
        clearInterval(timer);
  
        const timerType = document.getElementById("timerType").value;
        switch (timerType) {
          case "short":
            minutes = 5;
            break;
          case "long":
            minutes = 15;
            break;
          case "work":
          default:
            minutes = 25;
            break;
        }
        seconds = 0;
        updateTimerDisplay();
      }
  
      // Event listeners for timer controls
      document.getElementById("timerType").addEventListener("change", resetTimer);
      document.getElementById("startTimer").addEventListener("click", startTimer);
      document.getElementById("resetTimer").addEventListener("click", resetTimer);
  
      // Initialize timer display on page load
      updateTimerDisplay();
    }
  
    /**
     * Initializes the chat functionality.
     */
    function initializeChat() {
      const fab = document.querySelector(".fab");
      const chatPopup = document.getElementById("chatPopup");
      const closeChat = document.getElementById("closeChat");
      const sendMessageButton = document.getElementById("sendMessage");
      const chatInput = document.getElementById("chatInput");
      const chatHistory = document.getElementById("chatHistory");
  
      fab.addEventListener("click", () => {
        chatPopup.style.display = "flex";
      });
  
      closeChat.addEventListener("click", () => {
        chatPopup.style.display = "none";
      });
  
      sendMessageButton.addEventListener("click", sendMessage);
      chatInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") sendMessage();
      });
  
      /**
       * Sends a message to the chat API and displays the response.
       */
      async function sendMessage() {
        const message = chatInput.value.trim();
        if (message === "") return;
  
        displayMessage("You", message, "user");
        chatInput.value = "";
  
        try {
          const response = await fetch("http://127.0.0.1:8000/api/chat/", {
            method: "POST",
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
              "X-CSRFToken": getCookie("csrftoken"),
            },
            body: new URLSearchParams({ user_input: message }),
          });
  
          if (response.ok) {
            const data = await response.json();
            displayMessage("Bot", data.response, "bot");
          } else {
            displayMessage(
              "Bot",
              "Sorry, something went wrong. Please try again later.",
              "bot"
            );
          }
        } catch (error) {
          console.error("Error:", error);
          displayMessage(
            "Bot",
            "Sorry, something went wrong. Please try again later.",
            "bot"
          );
        }
      }
  
      /**
       * Displays a chat message in the chat history.
       * @param {string} sender - The sender of the message (e.g., "You" or "Bot").
       * @param {string} message - The message content.
       * @param {string} type - The type of message ("user" or "bot").
       */
      function displayMessage(sender, message, type) {
        const messageElement = document.createElement("li");
        messageElement.className = type;
        messageElement.textContent = `${sender}: ${message}`;
        chatHistory.appendChild(messageElement);
        chatHistory.scrollTop = chatHistory.scrollHeight;
      }
    }
  
    /**
     * Loads notices from the API and adds them to the notice list.
     */
    async function loadNotices() {
      const response = await fetch("http://127.0.0.1:8000/api/notice/");
      const notices = await response.json();
      notices.forEach(addNoticeToList);
    }
  
    /**
     * Loads polls from the API and adds them to the poll list.
     */
    async function loadPolls() {
      const response = await fetch("http://127.0.0.1:8000/api/poll/");
      const polls = await response.json();
      polls.forEach(addPollToList);
    }
  
    /**
     * Adds a notice to the list displayed on the page.
     * @param {Object} notice - The notice object to add.
     */
    function addNoticeToList(notice) {
      const noticeList = document.getElementById("noticeList");
      const listItem = document.createElement("li");
      listItem.className = "notice-card";
      listItem.innerHTML = `<h2>${notice.title}</h2><p>${notice.message}</p><p><small>${new Date(notice.created_at).toLocaleString()}</small></p>`;
      noticeList.appendChild(listItem);
    }
  
    /**
     * Adds a poll to the list displayed on the page.
     * @param {Object} poll - The poll object to add.
     */
    function addPollToList(poll) {
      const pollList = document.getElementById("pollList");
      const pollDiv = document.createElement("div");
      pollDiv.className = "poll-item";
      pollDiv.innerHTML = `<h3>${poll.title}</h3><ul>${poll.options
        .map((option) => `<li>${option.option_text} (${option.votes} votes)</li>`)
        .join("")}</ul>`;
      pollList.appendChild(pollDiv);
    }
  
    /**
     * Adds an issue to the list displayed on the page.
     * @param {Object} issue - The issue object to add.
     */
    function addIssueToList(issue) {
      const issueList = document.getElementById("issueList");
      const listItem = document.createElement("li");
      listItem.innerHTML = `<h2>${issue.title}</h2><p>${issue.description}</p><p><small>${new Date(issue.created_at).toLocaleString()}</small></p>`;
      issueList.appendChild(listItem);
    }
  
    /**
     * Retrieves the value of a specific cookie by name.
     * @param {string} name - The name of the cookie.
     * @returns {string|null} - The cookie value or null if not found.
     */
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
  
    // Weather API endpoint and fetch call
    const apiUrl =
      "https://api.openweathermap.org/data/2.5/weather?q=Ranchi&appid=771adaa3d4dc34c12b39933918248ec1&units=metric";
  
    /**
     * Fetches and displays weather data on the page.
     */
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => {
        const place = data.name;
        const temperature = data.main.temp;
        const weather = data.weather[0].description;
        const iconCode = data.weather[0].icon;
  
        const iconUrl = `http://openweathermap.org/img/wn/${iconCode}@2x.png`;
  
        const weatherContent = `
          <div class="weather-info">
              <img src="${iconUrl}" alt="${weather}" class="weather-icon">
              <p>${place}</p>
              <p>${temperature}°C</p>
              <p>${weather}</p>
          </div>
        `;
  
        document.getElementById("weatherContent").innerHTML = weatherContent;
      })
      .catch((error) => {
        console.error("Error fetching weather data:", error);
        document.getElementById("weatherContent").innerHTML =
          "<p>Failed to load weather data.</p>";
      });
  });
  