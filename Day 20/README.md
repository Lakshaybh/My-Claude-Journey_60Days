# Day 20 — Face Puzzle Game 🧩

**Challenge:** ABTalks AI Challenge — 60 Days of Building with AI
**Day:** 20 / 60
**Date:** 20 June 2025

---

## What I Built

A browser-based face puzzle game — fully self-contained in a **single HTML file** with no frameworks or backend.

You snap your face (or upload a photo), it gets sliced into puzzle pieces, scrambled, and you drag them back into the right order as fast as you can.

### Features
- 📷 **Live webcam capture** — front-facing camera, snap directly in browser
- 🖼️ **Local photo upload** — drag & drop or browse from your folder
- 🧩 **Three difficulty levels** — 3×3 (9 pieces), 4×4 (16 pieces), 5×5 (25 pieces)
- 🖱️ **Drag & drop controls** — full mouse and touch support
- ⏱️ **Live timer** — mm:ss.t format, starts the moment puzzle begins
- 🔢 **Move counter** — tracks every swap you make
- ✅ **Correct piece tracker** — green border on correctly placed pieces
- 🏆 **Leaderboard** — top 5 best times saved to localStorage
- 🎨 **Light theme UI** — warm orange & pink gradient design with floating animations

---

## What I Learned

**Canvas API**
Drawing, cropping, and slicing images programmatically using `drawImage()` — no library needed.

**getUserMedia & webcam access**
Requesting camera permissions, handling denial gracefully, and snapping a video frame onto a canvas.

**Drag & Drop from scratch**
Building mouse + touch drag logic without any library — managing `mousedown`, `mousemove`, `mouseup` and their touch equivalents with proper offset calculations.

**Game state management**
Tracking piece positions, detecting swaps, checking win conditions — all in plain JS without any framework.

**Fisher-Yates shuffle**
Implementing a proper randomised shuffle that guarantees the puzzle is always solvable.

**File handling in the browser**
`FileReader`, `drag-and-drop` file events, and rendering a local image file onto a canvas — all without uploading to any server.

**UI/UX without a framework**
Building a polished, responsive, animated interface using only CSS variables, gradients, keyframes, and flexbox/grid.

---

## File

| File | Description |
|------|-------------|
| `face-puzzle.html` | Complete game — open directly in any browser |

---

> *"The silly ideas are always the ones that teach the most."*
