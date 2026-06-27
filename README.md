# 🔍 Data Exposure Demo

> **A security & privacy awareness demonstration** — showing how much information a website can silently collect about you from a *single click* on a link.

When you open *any* link, the website on the other side can read a surprising amount of data from your browser — **without hacking you at all**. This project visualises exactly that, in a dramatic "hacker terminal" style, to help people understand why they should be careful about which links they open.

---

## ⚠️ Disclaimer (Read First)

This project is built **strictly for educational and awareness purposes**.

- ✅ Use it on **your own devices**, or with people who have given you **clear permission** (demos, workshops, presentations).
- ❌ Do **not** use it to trick, scare, or collect data from people without their consent.
- The data shown is the same data **every website you visit can already access** — that's the whole point of the demo.

You are responsible for how you use this code.

---

## 📸 What it captures

The moment the page loads, it reads the following from the visitor's browser (no permission popup needed — browsers expose this by default):

| Data | Source |
|------|--------|
| 🌐 Public IP address | `api.ipify.org` |
| 💻 Operating system / platform | `navigator.platform` |
| 🖥️ Screen resolution | `window.screen` |
| 🎮 GPU model | WebGL renderer info |
| 🔋 Battery level + charging status | Battery API |
| ⚙️ CPU cores & RAM | `navigator.hardwareConcurrency` / `deviceMemory` |
| 👆 Touchscreen support | `navigator.maxTouchPoints` |

And **only after the user interacts** (clicks), with explicit permission:

| Data | Source |
|------|--------|
| 📍 GPS location (lat/long) | Geolocation API *(asks for permission)* |

All collected data is sent back to the Flask server and printed in the terminal.

---

## 🛠️ Tech Stack

- **Python + Flask** — backend server that serves the page and receives the data
- **Vanilla JavaScript** — client-side data collection + "Matrix rain" / glitch UI
- **ngrok** *(optional)* — to expose the local server publicly for live demos

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the server
```bash
python dashboard.py
```
The server starts at `http://localhost:8080`.

### 3. Open the demo page
Visit **`http://localhost:8080/log`** in a browser. Watch the terminal — the collected data will appear there.

### 4. (Optional) Share it live with ngrok
`ngrok.exe` is **not included** in this repo (it's a large third-party binary). Download it from [ngrok.com/download](https://ngrok.com/download), place it in the project folder, then run:
```bash
ngrok http 8080
```
ngrok gives you a public URL you can open on any device to test.

> **Note:** You also need a `scream.mp3` file in the folder for the audio effect (any short audio clip works).

---

## 📂 Project Structure

```
data-exposure-demo/
├── dashboard.py        # Flask server + the demo page
├── requirements.txt    # Python dependencies
├── scream.mp3          # Audio effect (add your own)
└── ngrok.exe           # Download separately (not committed)
```

---

## 💡 Why I built this

Most people click links without thinking about what the other side can see. This project makes the invisible *visible* — a hands-on way to teach friends, students, or clients about everyday digital privacy.

---

## 📜 License

MIT — see [LICENSE](LICENSE).
