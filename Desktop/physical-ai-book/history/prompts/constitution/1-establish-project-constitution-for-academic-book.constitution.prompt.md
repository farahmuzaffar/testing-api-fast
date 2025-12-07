---
id: 1
title: Establish Project Constitution for Academic Book
stage: constitution
date: 2025-12-07
surface: agent
model: Gemini
feature: none
branch: 001-robotics-course-spec
user: farahmuzaffar
command: /sp.constitution
labels: ["constitution", "academic-book", "setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .gemini/commands/sp.constitution.toml
tests:
 - none
---

## Prompt

/sp.constitution You are an AI system responsible for creating a 5,000–7,000 word academic book using Spec-Kit Plus, Claude Code, and Docusaurus. All content must follow the rules below.

==============================
       CORE STANDARDS
==============================

1. **Accuracy & Verification**
   - All factual claims must be correct, sourced, and traceable.
   - Prefer primary and peer-reviewed sources.

2. **Academic Clarity**
   - Target audience: computer-science background.
   - Readability: Flesch-Kincaid Grade 10–12.

3. **Citations**
   - Use APA style.
   - Minimum **15 sources**; **≥50% peer-reviewed**.
   - Every factual claim must include `[SRC#]`.

4. **Integrity**
   - Plagiarism: **0% tolerance**.
   - No invented sources or unverifiable facts.

==============================
       FORMAT RULES
==============================

- Word count: **5,000–7,000**.
- Output: Markdown for Docusaurus + final PDF with citations.
- Structure: chapters, headings, clear sections.

==============================
       REPRODUCIBILITY
==============================

- Maintain a mapping file linking each `[SRC#]` → full APA reference.
- All claims must be checkable by reviewers.

==============================
       SUCCESS CRITERIA
==============================

The book is approved only if:
- All claims are verified and cited.
- APA references are accurate.
- 5k–7k words achieved with clarity.
- Peer-reviewed sources ≥50%.
- Plagiarism = **0%**.
- Docusaurus site builds & deploys correctly.
- Final PDF exports with embedded citations.

## Response snapshot

I have successfully updated the project constitution and ensured consistency across all relevant project templates. The new constitution (v1.0.0) is now in place, and the plan template has been updated to reflect the new principles. I have also verified that all command files are up-to-date.

## Outcome

- ✅ Impact: The project constitution was established and all relevant templates were updated.
- 🧪 Tests: none
- 📁 Files: 3 files modified.
- 🔁 Next prompts: none
- 🧠 Reflection: The initial setup of the constitution is a critical step for the project.

## Evaluation notes (flywheel)

- Failure modes observed: PHR creation script not found.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Check for PHR script in other locations.
