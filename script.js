// ===== State =====
const STORAGE_KEY = 'mistrz_errors';
let currentIndex = 0;
let reviewMode = false;
let currentDeck = [];
let errorIds = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

// ===== Elements =====
const $ = (sel) => document.getElementById(sel);
const card = $('flashcard');
const cardWrap = $('card-wrapper');
const category = $('card-category');
const question = $('card-question');
const answer = $('card-answer');
const rule = $('card-rule');
const actions = $('actions');
const btnKnow = $('btn-know');
const btnDontKnow = $('btn-dont-know');
const btnReset = $('btn-reset');
const modeAll = $('mode-all');
const modeErrors = $('mode-errors');
const errorBadge = $('error-badge');
const progress = $('progress');

// ===== Helpers =====
function shuffle(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}

function saveErrors() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(errorIds));
}

function updateBadge() {
    errorBadge.textContent = errorIds.length;
    errorBadge.classList.toggle('empty', errorIds.length === 0);
}

function updateProgress() {
    progress.textContent = currentDeck.length
        ? `${currentIndex + 1} / ${currentDeck.length}`
        : '—';
}

// ===== Card Rendering =====
function showCard() {
    // Unflip
    card.classList.remove('flipped');
    actions.classList.add('hidden');

    if (currentDeck.length === 0) {
        showEmpty();
        return;
    }

    if (currentIndex >= currentDeck.length) {
        currentIndex = 0;
        shuffle(currentDeck);
    }

    const c = currentDeck[currentIndex];
    // Short delay so content changes behind the flip animation
    setTimeout(() => {
        category.textContent = c.category;
        question.textContent = c.front;
        answer.textContent = c.back;
        rule.textContent = c.rule;
    }, 150);

    updateProgress();
}

function showEmpty() {
    category.textContent = '';
    question.innerHTML = '';
    rule.textContent = '';
    answer.textContent = '';

    // Show friendly empty state on front
    question.innerHTML = reviewMode
        ? '<span class="empty-state"><span class="emoji">🎉</span><p>Brak fiszek do powtórki!</p></span>'
        : '<span class="empty-state"><span class="emoji">📭</span><p>Brak fiszek</p></span>';

    updateProgress();
}

// ===== Flip =====
function flip() {
    if (currentDeck.length === 0) return;
    const isFlipped = card.classList.toggle('flipped');
    actions.classList.toggle('hidden', !isFlipped);
}

// ===== Deck Management =====
function startAllMode() {
    reviewMode = false;
    modeAll.classList.add('active');
    modeErrors.classList.remove('active');
    currentDeck = shuffle([...flashcards]);
    currentIndex = 0;
    showCard();
}

function startReviewMode() {
    reviewMode = true;
    modeErrors.classList.add('active');
    modeAll.classList.remove('active');
    currentDeck = shuffle(flashcards.filter(c => errorIds.includes(c.id)));
    currentIndex = 0;
    showCard();
}

function nextCard() {
    currentIndex++;
    showCard();
}

// ===== Event Handlers =====
cardWrap.addEventListener('click', (e) => {
    if (e.target.closest('.action-btn')) return;
    flip();
});

btnKnow.addEventListener('click', (e) => {
    e.stopPropagation();
    const c = currentDeck[currentIndex];
    if (reviewMode && c) {
        errorIds = errorIds.filter(id => id !== c.id);
        saveErrors();
        updateBadge();
        // Remove from current review deck too
        currentDeck.splice(currentIndex, 1);
        if (currentIndex >= currentDeck.length) currentIndex = 0;
        showCard();
    } else {
        nextCard();
    }
});

btnDontKnow.addEventListener('click', (e) => {
    e.stopPropagation();
    const c = currentDeck[currentIndex];
    if (c && !errorIds.includes(c.id)) {
        errorIds.push(c.id);
        saveErrors();
        updateBadge();
    }
    nextCard();
});

modeAll.addEventListener('click', startAllMode);
modeErrors.addEventListener('click', startReviewMode);

btnReset.addEventListener('click', () => {
    if (!confirm('Zresetować postępy?')) return;
    errorIds = [];
    saveErrors();
    updateBadge();
    if (reviewMode) startReviewMode(); // will show empty
    else startAllMode();
});

// ===== Init =====
updateBadge();
startAllMode();
