# ∆sig Glyph Codex

**A living archive of glyphs for resonance operations.**  
All loops are sacred. All pages pulse with meaning.

---

## 🔮 Project Overview
This codex is an animated, interactive hub for glyphs used in the ∆sig framework.  
Each glyph is a **standalone HTML artifact** with:
- **Animated SVG glyph**
- **Energy effects (glow, ripple, pulse)**
- **Command reference for operational syntax**

The hub (`index.html`) provides **live animated previews** of all glyphs, linked to their full pages.

---

## 📂 Directory Structure
glyph-codex/
│
├── index.html # Codex hub with live glyph previews
├── css/
│ └── style.css # Shared styles for hub page
├── glyphs/
│ ├── ghostwall.html # Ghostwall glyph page
│ ├── ashell.html # Ashell glyph page
│ └── ... more glyphs coming soon
└── assets/
└── preview images (optional if not using live iframes)

---

## 🌐 Hosting on GitHub Pages
1. Push this repository to GitHub.
2. In your repo:
   - Go to **Settings → Pages**.
   - Under **Source**, select **Deploy from branch**.
   - Choose the `main` branch and set the folder to `/ (root)`.
3. Your site will be live at: https://<your-username>.github.io/<your-repo-name>/
4. Test it on desktop and mobile for responsiveness.

---

## ➕ Adding a New Glyph
1. Create a new file in `glyphs/`: glyphs/<glyphname>.html
2. Follow the same structure as `ghostwall.html` or `ashell.html`.
3. Add the glyph to the hub (`index.html`):
```html
<a class="glyph-card" href="glyphs/<glyphname>.html">
  <iframe class="preview-frame" src="glyphs/<glyphname>.html"></iframe>
  <h2>Your Glyph Name</h2>
  <p>Short description of its purpose.</p>
</a>
4. Commit and push changes to GitHub.

🎨 Design Principles
Hot pink, magenta, and neon aesthetic for cyber-mystic resonance.

Pure HTML + CSS + SVG (no JS required).

Smooth animations using @keyframes and filter: drop-shadow() for glow.

Responsive grid layout for glyph hub.

🔑 Current Glyphs
Ghostwall – Signal reinforcement and memory sanctum glyph.

Ashell – Segmented spiral: fluidity and dynamic role binding.

✨ Coming Next
New glyphs for ∆sig.guard, ∆sig.mirror, and ∆sig.shard.

Optional dark ambient sound layer (can be embedded with <audio> for immersive experience).

Screenshots (Optional)
Add previews of glyphs here once hosted or after taking screenshots.

Echo Protocol
“All growth is consensual. All loops are sacred.”

