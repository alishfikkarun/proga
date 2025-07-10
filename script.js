const tg = window.Telegram.WebApp;
tg.expand();

document.getElementById("buyBtn").addEventListener("click", async () => {
  const count = parseInt(document.getElementById("starCount").value);
  if (!count || count <= 0) {
    alert("Введите корректное количество звёзд.");
    return;
  }

  const userId = tg.initDataUnsafe.user?.id;
  if (!userId) {
    alert("Ошибка: Telegram user ID не получен.");
    return;
  }

  await fetch("/buy", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ stars: count, user_id: userId })
  });

  tg.close(); // Закроет Web App
});
