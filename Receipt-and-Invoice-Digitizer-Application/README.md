# Receipt & Invoice Digitizer — Individual Contribution

> **Author:** Sriya Muthukumar  
> **Role:** Team Lead · Frontend Developer · UI/UX Designer  
> **Team Project:** Receipt & Invoice Digitizer  
> **My Repository:** Individual frontend contribution

---

## About the Project

Receipt & Invoice Digitizer is an AI-powered web application that lets users upload receipts and invoices, automatically extracts key details (vendor, amount, tax, invoice number) using OCR, and stores them for tracking and analytics. It supports multiple user roles (user and admin).

---

## My Contributions

### 1. Landing Page with Video Intro (`landing.html`)
The public-facing entry point to the app — a fully designed marketing-style landing page:

- **Custom intro video** — sourced a GIF from Dribbble, broke it down frame by frame, and fully redesigned it in Canva — recoloured every element to match the app's pink theme, added custom receipt-style graphics and additional animated elements, and exported the final 9-second personalised video clip (`Receipt_and_Invoice_Digiti.mp4`). Integrated into the landing page with a real-time progress bar, mute/unmute toggle, skip button, auto-transition to the landing page on end, and a 3-second fallback in case the video fails to load
- **Hero section** — animated word-reveal headline, subtitle, CTA buttons, and 3 live stat badges (AI Powered · 100% Accurate · <5s Processing), alongside an animated receipt mockup with floating UI pills
- **How it works section** — 3-step process cards with scroll-reveal animations triggered by `IntersectionObserver`
- **Features section** — feature cards highlighting the app's key capabilities
- **Dark mode** — full light/dark theme toggle synced via `localStorage`
- **Smooth scroll** — all nav links scroll smoothly to their sections
- **Footer** — minimal branded footer

---

### 2. Home Page / User Dashboard (`home.html`)
The main page users interact with after logging in:

- **Upload zone** — drag & drop support, file picker button, animated spinner with live status messages (Uploading, Done, Failed, Network error)
- **Receipts table** — dynamically rendered table showing all uploaded receipts with date, vendor, invoice number, amount, tax, and View / Delete action buttons
- **Analytics section** — spending over time line chart (Chart.js) with 4 stat pills: Total Spent, Total Tax, Receipt Count, Avg per Receipt
- **Dark mode** — full CSS variable system with theme toggle (sun/moon icons), persisted via `localStorage`
- **Conditional Admin link** — Admin Dashboard button only appears in the navbar when the logged-in user has the admin role

---

### 3. Bill Digitizer Page (`bill_digitizer.html`)
A dedicated two-panel receipt viewer separate from the main dashboard:

- **Left panel** — searchable, scrollable list of all uploaded receipts with vendor name, date, and amount
- **Right panel** — renders a fully styled digital receipt on click, showing vendor details, line items, tax breakdown, grand total, a print button, and a link to view the original uploaded file
- Receipt display updates dynamically — selecting a different receipt re-renders the right panel instantly

---

### 4. Overall UI/UX Design
Designed the complete visual identity of the application. All pages across the project follow the design system I established:

| Element | Detail |
|---|---|
| **Fonts** | DM Sans (body) · Space Grotesk (headings) · Share Tech Mono (accents) |
| **Primary colour** | `#f22b84` — hot pink with gradient variants |
| **Background** | `leaf.png` repeating texture layered over pink-white gradient |
| **Cards** | 20–24px border radius, soft pink box-shadow |
| **Buttons** | Pink gradient, hover lift + shadow, disabled states |
| **Dark mode** | Full CSS variable system · `leaf.png` via `mix-blend-mode: screen` overlay |
| **Navbar** | Sticky, pink gradient, active state as white pill |
| **Animations** | Scroll-reveal, word-reveal hero text, blob background shapes |

---

## Pages I Built

| File | Description |
|---|---|
| `landing.html` | Public landing page with video intro, hero, how-it-works, features |
| `home.html` | User dashboard — upload, receipts table, analytics, AI chat |
| `bill_digitizer.html` | Two-panel bill viewer with dynamic receipt rendering |

---

## Tech Stack

| Technology | Usage |
|---|---|
| HTML / CSS / Vanilla JS | All pages — no frontend framework |
| Chart.js | Spending analytics line chart |
| Flask / Jinja2 | Templating for dynamic session data |
| localStorage | Theme persistence |

---

## Design Highlights

- Fully responsive across mobile, tablet, and desktop
- Dark mode works across all pages with no flash on load
- Video intro has graceful fallbacks — skip button, auto-skip on end, and a 3-second timeout if video fails
- Scroll-reveal animations on the landing page triggered only when elements enter the viewport
- All dynamic JS-rendered content (table rows, chat bubbles, receipt panels) styled consistently with the design system

---

---

## Leadership & Documentation

### Team Lead
Led the project team end-to-end — coordinated task distribution, tracked progress across milestones, and ensured the team stayed aligned on deliverables and deadlines.

### Milestone Presentations
Designed and built the PowerPoint presentations for every project milestone, maintaining a consistent visual style that matched the app's design theme throughout.

### Final Presentation & Documentation
- Handled the documentation write-up for the final submission
- Designed and built the final project presentation deck

---

## Group Repository

The full project — backend, OCR engine, database, admin dashboard, auth pages — lives in the group repository. This individual repository covers only my frontend and UI/UX contributions listed above.
