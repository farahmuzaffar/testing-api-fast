---
id: 1
title: Create Specification for Robotics Course
stage: spec
date: 2025-12-07
surface: agent
model: Gemini
feature: robotics-course-spec
branch: 002-robotics-course-spec
user: farahmuzaffar
command: /sp.specify
labels: ["specification", "robotics", "course"]
links:
  spec: specs/002-robotics-course-spec/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/002-robotics-course-spec/spec.md
 - specs/002-robotics-course-spec/checklists/requirements.md
tests:
 - none
---

## Prompt

/sp.specify Target audience: University curriculum teams evaluating a capstone course in Physical AI & Humanoid Robotics. Goal: Produce a structured course specification describing the full quarter: modules, weekly plan, learning outcomes, hardware, simulation pipeline, and capstone. Success Criteria The specification must: Clearly define the course theme: Physical AI & Humanoid Robotics (embodied intelligence). Cover the 4 modules: ROS 2, Gazebo + Unity, NVIDIA Isaac, Vision-Language-Action (VLA). Include learning outcomes, weekly breakdown, assessments, and capstone. Document hardware needs (RTX workstations, Jetson kits, RealSense, robot options). Explain simulation-to-real flow using ROS 2, Gazebo, Isaac, and Jetson. Provide concise tables for lab architecture and hardware tiers. Markdown format, professional tone, structured sections. Constraints Length: ~1500–2500 words. No code or vendor marketing. Focus on course structure, not ethical concerns. Decisions to Document Why ROS 2 is chosen. Why Digital Twin simulation is required. Why NVIDIA Isaac is used for perception/manipulation. How VLA models integrate with ROS 2 actions. On-prem vs cloud simulation tradeoffs. Choice of workstation, Jetson, and robot tier. Required Content Include: Overview, motivation (why Physical AI matters). All four modules with key concepts. Weekly plan (Weeks 1–13). Assessments (ROS project, Gazebo sim, Isaac perception, capstone). Hardware tables: workstation specs, Jetson kit, robot tiers. Cloud option using AWS g5/g6. Latency caveat and offline deployment flow. Final Deliverable Generate a Markdown specification containing: Overview Learning outcomes Module descriptions Weekly roadmap Assessments + Capstone Hardware & Lab architecture On-prem vs cloud option Risks & assumptions Final summary

## Response snapshot

I have created the feature specification for the "Physical AI & Humanoid Robotics Course". The specification is located at `specs/002-robotics-course-spec/spec.md`. I have also created a quality checklist and validated the specification against it. The specification is now ready for the next phase: `/sp.plan`.

## Outcome

- ✅ Impact: A detailed feature specification for the robotics course was created.
- 🧪 Tests: none
- 📁 Files: 2 files created.
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: The user provided a very detailed prompt, which made it easy to generate a comprehensive specification.

## Evaluation notes (flywheel)

- Failure modes observed: The `create-new-feature.ps1` script failed initially due to incorrect parameter passing.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Ensure that long string parameters are always quoted when calling shell scripts.
