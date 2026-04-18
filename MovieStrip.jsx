// ════════════════════════════════════════════════════════════════════════════
// MovieStrip.jsx — Horizontal scrollable row of movie poster cards (NEW in Lesson 6)
// ════════════════════════════════════════════════════════════════════════════

import { useState, useEffect, useRef } from 'react';
import { omdbDetails } from '../utils/api';
import { useApp } from '../context/AppContext';

// ──────────────────── LESSON 6 ────────────────────
// Build the scrollable movie poster strip.
// Props: movies — array of OMDb movie objects
// 1. Filter to only movies with a valid Poster
// 2. Pre-fetch full details in the background (so clicking feels instant)
// 3. Clicking a card → call omdbDetails() → call openMovie() from useApp()
// 4. Show left/right scroll arrows when there are more cards to scroll to



// ──────────────────── END ─────────────────────────
