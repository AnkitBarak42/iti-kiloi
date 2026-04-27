# ITI Kiloi — Placement Management System

A complete online placement management system for ITI Kiloi, built as a Streamlit web app.

---


## 🚀 Deploy on Streamlit Cloud (Free)

### Step 1 — GitHub pe upload karein

1. [github.com](https://github.com) pe jaayein aur **Sign Up / Login** karein (free)
2. **New Repository** banayein → naam dein: `iti-kiloi`
3. Is folder ke **sab files** GitHub repo mein upload karein:
   - `app.py`
   - `index.html`
   - `requirements.txt`
   - `.streamlit/config.toml`
   - Sab `icon-*.png` files

### Step 2 — Streamlit Cloud pe deploy karein

1. [share.streamlit.io](https://share.streamlit.io) pe jaayein
2. GitHub account se **Login** karein
3. **"New app"** click karein
4. Repository select karein: `iti-kiloi`
5. Main file: `app.py`
6. **Deploy!** click karein

✅ Kuch minutes mein aapka app online ho jayega!
   Link milega: `https://your-name-iti-kiloi.streamlit.app`

---

## 💻 Local Chalane ke liye

```bash
pip install streamlit
streamlit run app.py
```

---

## 📱 Features

- 🔐 Role-based login (Admin / Staff)
- 🎓 Student records — add, edit, delete, view
- 📊 Dashboard with live placement stats
- 📋 Reports — trade-wise & session-wise
- 🕵️ Activity Log — who did what, when
- 📥 Import CSV / Export Excel + PDF
- 💾 JSON Backup & Restore
- 🖨️ Print-ready reports

## 💾 Data Storage

Data browser ke localStorage mein save hota hai — ek browser mein data permanently stored rahta hai.
Agar multiple computers pe same data chahiye, to **JSON Backup** export karke dusre computer mein **Restore** karein.

---

## 🔑 Default Login

- **Admin:** `admin` / `admin123`
- **Staff 1:** `staff1` / `staff123`

> ⚠️ Deployment ke baad Users page mein jaake password zaroor badlein!
