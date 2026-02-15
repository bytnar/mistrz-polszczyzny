# AGENTS.md

This document provides essential information for AI agents and developers working on the **Mistrz Polszczyzny 2026** codebase.

## 1. Project Overview

**Mistrz Polszczyzny 2026** is a static web application (HTML/CSS/JS) designed as a flashcard learning tool for Polish orthography and punctuation. It is a "vanilla" project with no build steps, frameworks, or package managers (npm/yarn are not used).

### Key Files
- `index.html`: Main application entry point.
- `style.css`: All styles, including dark mode and responsiveness.
- `script.js`: Application logic, state management, and LocalStorage handling.
- `data.js`: The generated database of flashcards (do not edit directly).
- `data_part1.js`: Source data for cards 1-180.
- `generate_full_data.py`: Python script that merges `data_part1.js` with internal data (cards 181-300) to generate `data.js`.

---

## 2. Build, Run, and Test Commands

Since this is a static site, there is no compile step for the application code.

### Running the Application
- Open `index.html` directly in a web browser.
- Alternatively, serve with a simple HTTP server:
  ```bash
  python3 -m http.server 8000
  ```

### Data Generation (Build Step)
The `data.js` file is a build artifact. If you need to modify flashcard content:
1. **Cards 1-180:** Edit `data_part1.js`.
2. **Cards 181-300:** Edit the lists (e.g., `chh_data`, `nie_data`) in `generate_full_data.py`.
3. **Regenerate:** Run the Python script:
   ```bash
   python3 generate_full_data.py
   ```
   *Note: This script reads `data_part1.js`, appends the extra cards, and overwrites `data.js`.*

### Testing
- **Manual Testing:** Open the app in a browser (mobile simulation recommended).
- **Functional Checks:**
  - Verify card flipping works.
  - Check "Umiem" vs "Powtórzę" logic.
  - Verify "Do powtórki" mode filters cards correctly.
  - Reload page to test `LocalStorage` persistence (progress should be saved).
  - Test "Resetuj postępy" button.
- **Linting:**
  - JS: No linter configured. Use standard ES6+ best practices.
  - Python: Follow PEP 8.
  - HTML/CSS: Ensure valid syntax and proper nesting.

---

## 3. Code Style & Conventions

### JavaScript (`script.js`)
- **Style:** Vanilla ES6+.
- **Indentation:** 4 spaces.
- **Semicolons:** Always use semicolons.
- **Variables:** Use `const` by default, `let` for mutable state. Avoid `var`.
- **Naming:** `camelCase` for variables and functions.
- **DOM Access:** Use the helper function `$` for `document.getElementById`.
  ```javascript
  const $ = (sel) => document.getElementById(sel);
  ```
- **State Management:**
  - State is stored in global variables (`currentIndex`, `errorIds`, `currentDeck`).
  - Persistence is handled via `localStorage` keys: `mistrz_errors`, `mistrz_state`.
  - Always call `saveState()` or `saveErrors()` after modifying state.
- **Error Handling:** Use `try...catch` blocks when interacting with `localStorage` or parsing JSON.

### CSS (`style.css`)
- **Architecture:** Plain CSS with CSS Variables (Custom Properties) for theming.
- **Indentation:** 4 spaces.
- **Theming:** Define colors in `:root`.
  - Use semantic names: `--bg`, `--surface`, `--accent`, `--text`.
- **Layout:** Flexbox is the primary layout engine.
- **Responsiveness:** Mobile-first approach. The `.app` container has a `max-width: 440px` to simulate a mobile app view on desktop.
- **Units:** Use `rem` for font sizes and `px` for borders/radius.

### HTML (`index.html`)
- **Structure:** Semantic HTML5 (`nav`, `main` implied by wrapper, `button`).
- **Indentation:** 4 spaces.
- **Attributes:** Use double quotes for attributes.
- **Accessibility:** Ensure buttons have readable text or `aria-label`.

### Python (`generate_full_data.py`)
- **Style:** PEP 8.
- **Indentation:** 4 spaces.
- **Encoding:** Always specify `encoding='utf-8'` when opening files.
- **Formatting:** Use f-strings for string interpolation.

---

## 4. Development Workflow

1. **Modify:** Make changes to `script.js`, `style.css`, or `index.html`.
2. **Data Updates:** If updating content, modify source files (`data_part1.js` or `generate_full_data.py`) and run the generation script.
3. **Verify:** Open `index.html` to verify changes visually and functionally.
4. **Commit:** Create concise, descriptive commit messages.

### Common Tasks

**Adding a new Flashcard:**
- DO NOT edit `data.js`.
- If it belongs to an existing category in `generate_full_data.py` (e.g., "Ortografia ch/h"), add it to the list there.
- If it's a new category or belongs to the first batch, check `data_part1.js`.
- Run `python3 generate_full_data.py`.

**Changing UI Colors:**
- Edit the `:root` variables in `style.css`.
- Test contrast ratios in both light (if added later) and dark modes (current default).

**Fixing a Logic Bug:**
- Check `script.js`.
- If related to state persistence, clear `localStorage` (`Application` tab in DevTools) to test a clean slate.

---

## 5. Security & Performance

- **Security:** Since this is a client-side app, ensure no sensitive data is ever expected to be stored. `localStorage` is for user progress only.
- **Performance:**
  - Assets are minimal.
  - Fonts are loaded from Google Fonts (Inter).
  - Ensure `data.js` doesn't grow exponentially; current size (300 cards) is negligible for modern browsers.
