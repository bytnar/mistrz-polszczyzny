# AGENTS.md

This document provides essential information for AI agents and developers working on the **Mistrz Polszczyzny 2026** codebase.

## 1. Project Overview

**Mistrz Polszczyzny 2026** is a static web application (HTML/CSS/JS) designed as a flashcard learning tool for Polish orthography and punctuation. It is a "vanilla" project with no build steps, frameworks, or package managers (npm/yarn are not used).

### Key Files
- `index.html`: Main application entry point.
- `style.css`: All styles, including dark mode and responsiveness.
- `script.js`: Application logic, state management, and LocalStorage handling.
- `data.js`: Database of flashcards (400 cards). Edit directly.

---

## 2. Build, Run, and Test Commands

Since this is a static site, there is no compile step for the application code.

### Running the Application
- Open `index.html` directly in a web browser.
- Alternatively, serve with a simple HTTP server:
  ```bash
  python3 -m http.server 8000
  ```

### Data Editing
Edit `data.js` directly — it contains all 400 cards. After editing, verify:
```bash
node -e "console.log(require('./data.js').length)"
```

### Testing
- **Automated Testing:** Playwright-based tests in `test_app.py`. Run with:
  ```bash
  make test        # Run in headless mode (default)
  make test-visible # Run with visible browser for debugging
  ```
  Tests cover: initial load, card flip, button actions, review mode, persistence, reset, and mode switching.
- **CI/CD:** GitHub Actions workflow in `.github/workflows/headless-tests.yml` runs tests automatically on push/PR to main/master.
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

1. **Modify:** Make changes to `script.js`, `style.css`, `index.html`, or `data.js`.
2. **Verify:** Open `index.html` to verify changes visually and functionally.
3. **Commit:** Create concise, descriptive commit messages.

### Common Tasks

**Adding a new Flashcard:**
- Edit `data.js` directly — add the new card with the next available `id`.
- Verify the word exists via `https://sjp.pwn.pl/so/{word}`.
- Run validation: `node -e "console.log(require('./data.js').length)"`.

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
  - Ensure `data.js` doesn't grow exponentially; current size (400 cards) is negligible for modern browsers.
