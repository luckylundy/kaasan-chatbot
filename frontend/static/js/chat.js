function addMessage(message, isUser = false) {
  const messagesDiv = document.getElementById("chat-messages");
  const messageDiv = document.createElement("div");
  messageDiv.className = `message ${isUser ? "user" : "bot"}`;
  messageDiv.textContent = message;
  messagesDiv.appendChild(messageDiv);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();

  if (message === "") return;

  // ユーザーのメッセージを表示
  addMessage(message, true);
  input.value = "";

  try {
    const response = await fetch("/send_message", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message }),
    });

    const data = await response.json();

    // ボットの返答を表示
    addMessage(data.response);
  } catch (error) {
    console.error("Error:", error);
    addMessage("申し訳ありません。エラーが発生しました。");
  }
}

// Enterキーでメッセージを送信
document
  .getElementById("user-input")
  .addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      sendMessage();
    }
  });
