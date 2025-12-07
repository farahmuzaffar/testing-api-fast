# Tasks: Physical AI & Humanoid Robotics Course Book

**Input**: Design documents from `specs/002-robotics-course-spec/`

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 [P] Initialize Docusaurus project in `book/`
- [ ] T002 [P] Create directory structure for docs in `book/docs/`
- [ ] T003 [P] Configure `docusaurus.config.js` with book title and navigation

---

## Phase 2: Foundational Writing (Blocking Prerequisites)

- [ ] T004 Write the book Overview and Motivation in `book/docs/overview.md`
- [ ] T005 Write the course Learning Outcomes in `book/docs/learning-outcomes.md`

---

## Phase 3: User Story 1 - Curriculum Team Review (Content Creation)

### Module Content
- [ ] T006 [US1] [P] Write Module 1 (ROS 2) content in `book/docs/modules/ros2.md`
- [ ] T007 [US1] [P] Write Module 2 (Gazebo/Unity) content in `book/docs/modules/gazebo-unity.md`
- [ ] T008 [US1] [P] Write Module 3 (NVIDIA Isaac) content in `book/docs/modules/nvidia-isaac.md`
- [ ] T009 [US1] [P] Write Module 4 (VLA) content in `book/docs/modules/vla.md`

### High-Level Structure
- [ ] T010 [US1] Write the simulation-to-real workflow explanation in `book/docs/sim-to-real.md`
- [ ] T011 [US1] Write the on-prem vs. cloud trade-offs in `book/docs/on-prem-vs-cloud.md`
- [ ] T012 [US1] Write the risks and assumptions in `book/docs/risks.md`

---

## Phase 4: User Story 2 - Instructor Preparation (Practical Details)

### Weekly Plan & Assessments
- [ ] T013 [US2] Create the 13-week roadmap in `book/docs/weekly-plan.md`
- [ ] T014 [US2] Detail the assessments in `book/docs/assessments.md`
- [ ] T015 [US2] Describe the capstone project in `book/docs/capstone.md`

### Hardware & Lab
- [ ] T016 [US2] Document the hardware tiers in `book/docs/hardware.md`
- [ ] T017 [US2] Describe the lab architecture in `book/docs/lab-architecture.md`

---

## Phase 5: Polish & Cross-Cutting Concerns

- [ ] T018 [P] Review all content for technical accuracy
- [ ] T019 [P] Edit for clarity, consistency, and flow
- [ ] T020 [P] Generate PDF version of the book
- [ ] T021 Run `quickstart.md` validation

---

## Dependencies & Execution Order

- **Phase 1 (Setup)** must be completed before all other phases.
- **Phase 2 (Foundational Writing)** must be completed before Phases 3 and 4.
- **Phase 3 (User Story 1)** and **Phase 4 (User Story 2)** can be worked on in parallel.
- **Phase 5 (Polish)** is the final phase.
