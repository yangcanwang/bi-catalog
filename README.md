# bi-catalog

# CMA CGM US — Active BI Catalog Discovery Tool

A smart, AI-powered report discovery tool I built for CMA CGM US business teams. Instead of searching by keyword, users describe what they need in plain language and the tool matches them to the right report — or routes them into a new report request if nothing exists.

---

## Why I built this

I maintain a catalog of reports and dashboards built for the business as part of the BI NORTAM team. When teams have a reporting need, they should be able to search the catalog first to see if something already exists — avoiding duplicate requests and saving everyone time.

The current search tool has two core limitations I wanted to solve:

- **Search is text-based and not effective enough.** Users select a department, type keywords, and hope they match a report title exactly. But a report title can only hold so many words, and users often don't know the right terminology. Someone searching "why did East Coast volume drop" will never find a report titled "Trade Lane Performance by Origin Port" — even if it answers their question perfectly.
- **Search and request submission are two completely separate processes.** Most users forget to search first. Those who do search, find nothing, and then want to submit a request have to start over in a different tool entirely — with no connection between what they already described and the form they now need to fill out.

---

## What this tool does

It replaces keyword search with an AI-driven discovery experience that understands what a user is looking for — not just whether their words match a title.

**1. Understands intent, not just words**
I feed the AI three layers of information per report:
- The SQL query — so it learns the actual data scope, department codes, booking prefixes, filters, and limitations of each report
- The report description and business use cases — so it understands what the report truly covers and can match it to a user's need even when the wording is completely different
- Basic metadata — report title, department, owner, refresh frequency, and report link

**2. Asks follow-up questions to sharpen vague requests**
If a user's input is unclear, the tool asks one targeted clarifying question before returning results — for example: *"Are you trying to track delivery delays, analyze carrier costs, or monitor fulfillment volume?"* — rather than surfacing poor matches.

**3. Returns a ranked shortlist, not a single answer**
Each result is displayed as a report card showing a plain-English description, a match reason explaining why it was surfaced, the report owner's contact information, and a direct link to open the report.

**4. Pre-fills the new report request form**
If no existing report matches, users are routed directly into a request form pre-filled with everything they already provided — their department, description, and filters — saving time and ensuring the BI team receives structured, high-quality intake.

---

## How it works

```
User enters catalog
        ↓
Selects filters + describes need
        ↓
AI asks one follow-up question if input is unclear
        ↓
Ranked results shortlist returned
        ↓
   ┌────────────────────────────────────────────┐
   │ Match found → user opens report directly    │
   │ Wants to discuss → contacts report owner    │
   │ No match → request form, pre-filled by AI   │
   └────────────────────────────────────────────┘
```

---

## What feeds the AI

To generate meaningful, searchable content for each report, I collect the following from report stakeholders:

- **Report description** — what the report tracks and covers
- **Who uses it and how often** — role and frequency
- **A specific use case** — a real situation where someone relied on this report

In parallel, I work with the DEV team to collect the underlying SQL query for each report. Together these inputs allow the AI to match user intent to the right report — not just keywords to titles.

---

## Tech stack

- **Python** — core language
- **Streamlit** — UI framework
- **Hosted on** Streamlit Community Cloud

---

## Project structure

```
bi-catalog/
├── app.py           # Main application and all screen logic
├── data/
│   └── reports.py   # Report catalog data and follow-up questions
├── requirements.txt # Python dependencies
└── README.md
```

---

## Contact

Built and maintained by [your name] — BI NORTAM team. Feel free to reach out at [your email] with any questions or feedback.
