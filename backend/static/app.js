const tokenKey = "fluentspeak_access";
const refreshKey = "fluentspeak_refresh";
const conversationKey = "fluentspeak_conversation";

function authHeaders() {
  const access = localStorage.getItem(tokenKey);
  return access ? { Authorization: `Bearer ${access}` } : {};
}

async function apiFetch(url, options = {}) {
  const response = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...authHeaders(),
      ...(options.headers || {}),
    },
  });

  if (response.status === 401) {
    localStorage.removeItem(tokenKey);
    localStorage.removeItem(refreshKey);
    if (!window.location.pathname.startsWith("/auth")) {
      window.location.href = "/auth/";
    }
  }

  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || response.statusText);
  }

  return response.status === 204 ? null : response.json();
}

function setStatus(message) {
  const status = document.getElementById("auth-status");
  if (status) {
    status.textContent = message;
  }
}

async function bootstrapAuthPage() {
  const loginForm = document.getElementById("login-form");
  const registerForm = document.getElementById("register-form");
  if (!loginForm || !registerForm) return;

  loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const payload = Object.fromEntries(new FormData(loginForm).entries());
    try {
      const data = await apiFetch("/api/v1/auth/login", {
        method: "POST",
        body: JSON.stringify(payload),
      });
      localStorage.setItem(tokenKey, data.access);
      localStorage.setItem(refreshKey, data.refresh);
      window.location.href = "/dashboard/";
    } catch (error) {
      setStatus("Login failed. Check your email and password.");
    }
  });

  registerForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const payload = Object.fromEntries(new FormData(registerForm).entries());
    try {
      const data = await apiFetch("/api/v1/auth/register", {
        method: "POST",
        body: JSON.stringify(payload),
      });
      localStorage.setItem(tokenKey, data.access);
      localStorage.setItem(refreshKey, data.refresh);
      window.location.href = "/dashboard/";
    } catch (error) {
      setStatus("Registration failed. Try a different email.");
    }
  });
}

async function logout() {
  const refresh = localStorage.getItem(refreshKey);
  if (refresh) {
    try {
      await apiFetch("/api/v1/auth/logout", {
        method: "POST",
        body: JSON.stringify({ refresh }),
      });
    } catch (error) {
      // Ignore logout errors and clear local state anyway.
    }
  }
  localStorage.removeItem(tokenKey);
  localStorage.removeItem(refreshKey);
  localStorage.removeItem(conversationKey);
  window.location.href = "/auth/";
}

async function ensureConversation(topicId) {
  if (topicId) {
    const created = await apiFetch("/api/v1/conversations", {
      method: "POST",
      body: JSON.stringify({ topic_id: topicId }),
    });
    localStorage.setItem(conversationKey, created.conversation_id);
    return created.conversation_id;
  }

  const cachedConversation = localStorage.getItem(conversationKey);
  if (cachedConversation) {
    return cachedConversation;
  }

  const conversations = await apiFetch("/api/v1/conversations");
  if (conversations.length > 0) {
    localStorage.setItem(conversationKey, conversations[0].id);
    return conversations[0].id;
  }

  return null;
}

function renderStatList(root, items) {
  root.innerHTML = items
    .map(
      (item) => `
        <article class="stat-card">
          <strong>${item.value}</strong>
          <span>${item.label}</span>
        </article>
      `
    )
    .join("");
}

async function renderDashboard() {
  const summary = document.getElementById("dashboard-summary");
  const topics = document.getElementById("topics-list");
  const scenarios = document.getElementById("scenario-list");
  const title = document.getElementById("dashboard-title");
  const subtitle = document.getElementById("dashboard-subtitle");
  if (!summary || !topics || !scenarios) return;

  const [me, topicList, conversationList] = await Promise.all([
    apiFetch("/api/v1/me"),
    apiFetch("/api/v1/topics"),
    apiFetch("/api/v1/conversations"),
  ]);

  const profile = me.profile || {};
  if (title) {
    title.textContent = `Good to see you, ${profile.full_name || me.email.split("@")[0]}.`;
  }
  if (subtitle) {
    subtitle.textContent = "Choose a topic, start a scenario, and keep your streak moving.";
  }

  renderStatList(summary, [
    { value: profile.level || "beginner", label: "level" },
    { value: profile.daily_goal || 10, label: "daily goal" },
    { value: conversationList.length, label: "conversations" },
    { value: "Live", label: "correction" },
  ]);

  topics.innerHTML = topicList
    .slice(0, 8)
    .map(
      (topic, index) => `
        <article class="card topic-card">
          <div>
            <span class="topic-chip">${topic.category || "topic"}</span>
            <h3>${topic.title}</h3>
            <p>${topic.description || "Practice this topic with guided English conversation."}</p>
          </div>
          <button type="button" data-topic-id="${topic.id}">Start lesson</button>
        </article>
      `
    )
    .join("");

  scenarios.innerHTML = [
    { title: "Job interview", description: "Answer practice questions with confidence." },
    { title: "Airport", description: "Check in, ask for help, and get through security." },
    { title: "Business meeting", description: "Discuss updates and present ideas." },
  ]
    .map(
      (item) => `
        <article class="scenario-card card">
          <h3>${item.title}</h3>
          <p>${item.description}</p>
        </article>
      `
    )
    .join("");

  topics.querySelectorAll("[data-topic-id]").forEach((button) => {
    button.addEventListener("click", async () => {
      const conversationId = await ensureConversation(button.dataset.topicId);
      if (conversationId) {
        localStorage.setItem(conversationKey, conversationId);
        window.location.href = `/chat/?conversation=${conversationId}`;
      }
    });
  });
}

async function renderChat() {
  const thread = document.getElementById("chat-thread");
  const form = document.getElementById("chat-form");
  const currentLesson = document.getElementById("current-lesson");
  const correction = document.getElementById("feedback-correction");
  const optimized = document.getElementById("feedback-optimized");
  const vocab = document.getElementById("feedback-vocab");
  if (!thread || !form) return;

  const params = new URLSearchParams(window.location.search);
  const requestedConversation = params.get("conversation");
  const conversationId = requestedConversation || localStorage.getItem(conversationKey) || (await ensureConversation(null));

  if (!conversationId) {
    thread.innerHTML = `<article class="message assistant"><div class="message-header"><span>Coach</span></div><p>Create a conversation from the dashboard to begin.</p></article>`;
    return;
  }

  localStorage.setItem(conversationKey, conversationId);

  const [conversations, conversationData] = await Promise.all([
    apiFetch("/api/v1/conversations"),
    apiFetch(`/api/v1/conversations/${conversationId}`),
  ]);

  const selectedConversation = conversations.find((item) => item.id === conversationId) || conversationData;
  if (currentLesson) {
    currentLesson.textContent = selectedConversation.title || selectedConversation.topic?.title || "Practice session";
  }

  const renderThread = () => {
    const messages = conversationData.messages || [];
    thread.innerHTML = messages
      .map(
        (message) => `
          <article class="message ${message.role === "user" ? "user" : "assistant"}">
            <div class="message-header">
              <span>${message.role === "user" ? "You" : "Coach"}</span>
              <span>Turn ${message.turn_number}</span>
            </div>
            <p>${message.content}</p>
          </article>
        `
      )
      .join("");
  };

  renderThread();

  const latestAssistant = (conversationData.messages || []).filter((message) => message.role === "assistant").at(-1);
  if (latestAssistant && latestAssistant.feedback) {
    correction.textContent = latestAssistant.feedback.correction || "No correction yet.";
    optimized.textContent = latestAssistant.feedback.optimized_response || "No optimized response yet.";
    vocab.textContent = latestAssistant.feedback.next_question || "No next question yet.";
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const messageInput = form.querySelector('input[name="message"]');
    const text = messageInput.value.trim();
    if (!text) return;

    await apiFetch(`/api/v1/conversations/${conversationId}/turns`, {
      method: "POST",
      body: JSON.stringify({ message: text }),
    });

    messageInput.value = "";
    window.location.reload();
  });
}

async function renderVocabulary() {
  const root = document.getElementById("vocabulary-list");
  const summary = document.getElementById("vocabulary-summary");
  if (!root) return;

  const data = await apiFetch("/api/v1/vocabulary/learned");
  const mastered = data.filter((item) => item.mastered).length;
  if (summary) {
    renderStatList(summary, [
      { value: data.length, label: "learned" },
      { value: mastered, label: "mastered" },
      { value: data.reduce((total, item) => total + (item.times_seen || 0), 0), label: "seen" },
    ]);
  }

  root.innerHTML = data.length
    ? data
        .map(
          (item) => `
            <article class="word-card card">
              <div>
                <span class="topic-chip">${item.vocabulary.difficulty || "word"}</span>
                <strong>${item.vocabulary.word}</strong>
                <p>${item.vocabulary.definition || "Saved from a conversation."}</p>
              </div>
              <div class="word-actions">
                <button type="button" class="primary" data-master-word="${item.id}">${item.mastered ? "Mastered" : "Mark mastered"}</button>
                <button type="button" data-delete-word="${item.id}">Remove</button>
              </div>
            </article>
          `
        )
        .join("")
    : `<article class="card word-card"><strong>No vocabulary yet</strong><p>Once you practice a few turns, your new words will show up here.</p></article>`;

  root.querySelectorAll("[data-master-word]").forEach((button) => {
    button.addEventListener("click", async () => {
      await apiFetch(`/api/v1/vocabulary/learned/${button.dataset.masterWord}/master`, { method: "POST" });
      window.location.reload();
    });
  });

  root.querySelectorAll("[data-delete-word]").forEach((button) => {
    button.addEventListener("click", async () => {
      await apiFetch(`/api/v1/vocabulary/learned/${button.dataset.deleteWord}`, { method: "DELETE" });
      window.location.reload();
    });
  });
}

async function renderProgress() {
  const root = document.getElementById("progress-summary");
  const timeline = document.getElementById("progress-timeline");
  if (!root) return;

  const data = await apiFetch("/api/v1/me/progress");
  renderStatList(root, [
    { value: data.conversations_completed, label: "conversations" },
    { value: data.words_learned, label: "words learned" },
    { value: data.current_streak, label: "streak" },
    { value: `${data.total_minutes}m`, label: "practice time" },
  ]);

  if (timeline) {
    timeline.innerHTML = [
      { title: "Keep the streak alive", detail: "Open one practice session today." },
      { title: "Review 3 words", detail: "Mark mastered words from vocabulary." },
      { title: "Start a scenario", detail: "Try a roleplay instead of a topic." },
    ]
      .map(
        (item) => `
          <article class="step-card">
            <strong></strong>
            <div>
              <h3 style="margin:0 0 4px;">${item.title}</h3>
              <span>${item.detail}</span>
            </div>
          </article>
        `
      )
      .join("");
  }
}

document.addEventListener("DOMContentLoaded", async () => {
  const logoutButton = document.querySelector("[data-action='logout']");
  if (logoutButton) {
    logoutButton.addEventListener("click", logout);
  }

  await bootstrapAuthPage();
  await renderDashboard();
  await renderVocabulary();
  await renderProgress();
  await renderChat();
});
