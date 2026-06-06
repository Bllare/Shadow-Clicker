# Shadow Clicker 🌑

Shadow Clicker is a modern Windows auto clicker built with **PySide6** that can send clicks either normally or directly to a target window using native Windows messages — allowing automation **without moving your mouse cursor**.

Perfect for gaming, testing, automation, and repetitive tasks.

## ⬇️ Download

**Latest Release:**

[⬇️ Download Shadow Clicker](https://github.com/Bllare/Shadow-Clicker/releases/latest/download/ShadowClicker.exe)

---

## ✨ Features

### 🖱️ Click Modes

- **Normal Clicker**
  - Uses standard mouse input.
- **Inside Clicker (HWND)**
  - Sends clicks directly to a target window using native Windows APIs.
  - Your real cursor stays exactly where it is.
  - Great for background clicking.

### 🎯 Click Options

- Left mouse button
- Right mouse button
- Middle mouse button
- Single click
- Double click

### ⏱️ Fully Configurable Intervals

Set delays using:

- Minutes
- Seconds
- Milliseconds

Supports extremely fast clicking as well as long interval automation.

### 🔁 Repeat Modes

- Repeat a specific number of times
- Repeat until manually stopped

### ⌨️ Global Hotkeys

- Custom global hotkey
- Toggle mode
- Hold-to-click mode

No need to keep the application focused.

### 📍 Cursor Position

- Click at the current cursor location
- Pick custom screen coordinates
- Manual X / Y coordinate editing

### ✋ Hold Mode

Instead of repeatedly clicking, Shadow Clicker can hold the selected mouse button for a configurable duration.

### 🕵️ Undetect Options

Optional human-like behavior:

- Mouse shake (jitter)
- Random click delay

Useful for making click patterns less robotic.

### 🎨 Modern Interface

- Clean dark UI
- Lightweight
- Built with PySide6
- Easy to configure

---

## 📸 Preview

![Shadow Clicker](https://github.com/user-attachments/assets/3be8f521-aa3c-4db6-97b5-e4cf5c87c80a)

---

## 🚀 Installation

### Run from Source

```bash
git clone https://github.com/Bllare/Shadow-Clicker.git

cd Shadow-Clicker

pip install -r requirements.txt

python main.py
