# 📱 Panorra post trail — Interactive Design Showcase

Interactive UI/UX prototype and design showcase for **Panorra post trail**. Built with lightweight, responsive HTML5, Tailwind CSS, Alpine.js, and Phosphor Icons for seamless client demonstration and developer handoff.

---

## 🚀 Live Demo for Client

- **Live URL**: [https://harundev0.github.io/panorra-post-trail/](https://harundev0.github.io/panorra-post-trail/)
- **Repository**: [https://github.com/harundev0/panorra-post-trail](https://github.com/harundev0/panorra-post-trail)

---

## 🌟 Screens & Prototype Catalog

| Screen | Description | File |
| :--- | :--- | :--- |
| **📱 Showcase Hub** | Unified responsive shell with tab switching and full-page preview | `index.html` |
| **✨ Main Interactive UI** | Full end-to-end user journey with interactive states | `pages/tourmkr_ui.html` |
| **1️⃣ Step 1: Select Tour** | Tour list selection, loading skeletons, and empty state | `pages/tourmkr_states_step1.html` |
| **2️⃣ Step 2: Content & Details** | 360 Scene vs Route Map dual preview with waypoints list & fixed bottom actions | `pages/tourmkr_states_step2.html` |
| **3️⃣ Step 3: Confirmation** | Post review, author metadata, tags, and fixed publish action bar | `pages/tourmkr_states_step3.html` |
| **🗺️ Map Focus State** | Fullscreen 1:1 route map with elevation graph, stats pills, and bottom tabs | `pages/tourmkr_states_map_focus.html` |
| **📄 Post Detail 360** | Side-by-side 360 panorama view with hotspots, action buttons & details sheet | `pages/tourmkr_post_detail.html` |

---

## 🛠️ Tech Stack & Architecture

- **Tailwind CSS** (v3 via CDN with custom opacity tokens & dark mode)
- **Alpine.js** (Reactive client state management, modal popups, and tab toggling)
- **Phosphor Icons** (High-quality, flexible iconography)
- **Zero-Dependency Node Server** (`server.js`) for local instant staging on ports `8080` & `3000`

---

## 💻 Local Quick Start

To run the showcase locally:

```bash
# Clone the repository
git clone https://github.com/harundev0/tourmkr-mobile.git
cd tourmkr-mobile

# Run the local server
npm start
# or: node server.js
```

Open your browser and navigate to:
👉 **[http://localhost:8080](http://localhost:8080)** (or **http://localhost:3000**)

---

## 📁 Project Structure

```text
├── index.html                   # Showcase hub with interactive iframe stage
├── server.js                    # Zero-dependency local HTTP static server
├── package.json                 # Scripts and package metadata
├── .github/
│   └── workflows/
│       └── deploy.yml           # Automated GitHub Pages CI/CD workflow
├── pages/
│   ├── tourmkr_ui.html
│   ├── tourmkr_states_step1.html
│   ├── tourmkr_states_step2.html
│   ├── tourmkr_states_step3.html
│   ├── tourmkr_states_map_focus.html
│   └── tourmkr_post_detail.html
├── screenshots/                 # High-resolution prototype captures
└── designs/                     # Design specs and exported references
```

---

&copy; 2026 Tourmkr. Designed and built for seamless client presentation.
