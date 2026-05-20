# Bhatera Roll-Up Platform

## Author

Sohan Bhattacharyya — Finance and Business Analytics, University of Pittsburgh
Internship experience: Assured Guaranty, PE Gate, Pacific Red Holdings

---

A full-stack operational dashboard built around an AI roll-up platform model. Designed to show what real-time portfolio management looks like when an AI operating layer is deployed across a PE-backed acquisition portfolio using a three-phase system — Workflow Redesign, System Construction, and Command and Control.

---

## What It Does

The platform gives PE sponsors and operators a single window into everything the system is generating — revenue performance, rebuttal outcomes, job pipeline, compounding knowledge, and equity value — across every location in the portfolio simultaneously.

The mock client is **Apex Restoration Group**, a 6-location water, fire, and mold remediation business backed by a lower-middle-market PE firm. The data reflects a 14-month post-deployment snapshot.

---

## The Seven Views

### Overview
Portfolio-level performance summary. Four metric cards showing revenue, EBITDA, margin, and active locations — each with a delta versus pre-deployment. Dual-axis line chart tracking revenue and EBITDA growth over 14 months. EBITDA by Quarter bar chart with automatic color coding based on whether margin crosses the 15 percent target threshold.

### Locations
Site-by-site breakdown. Horizontal bar chart showing EBITDA margin per location with programmatic color coding — gold above 17 percent, blue between 13 and 17, red below 13. Revenue contribution donut chart showing portfolio concentration. Site Performance table with VS Target column showing the gap between actual margins and the PE acquisition model.

### Rebuttals
Insurance claim rebuttal tracking. Approval rate up from ~52 percent to 81 percent, response time down from 3 hours to 11 minutes. Grouped bar chart showing submitted versus approved by month. Status Breakdown chart. By Category table showing win rates and review flags across Pricing, Scope Change, Timeline, Contract Terms, and Service Level.

### Pipeline
Active job tracking from scoping through cash collection. Deals by Stage funnel chart. Monthly Closings trend. Active Deals table with stage pills, rep assignment, estimated close date, and Hot/Active/Review status flags.

### Knowledge Base
The compounding intellectual asset. 156 encoded articles across 12 categories, 3,402 monthly views growing 22 percent month over month. Monthly Views bar chart with trend line overlay. Top Articles horizontal bar chart. Recent Articles table with category pills, author, view count, and In Review status for documents being actively updated.

### Value Tracker
Equity position in the portfolio. Hero number — $1.84 million current equity value from a 7 percent stake against $95,000 cash deployed. 19.4x MOIC in 14 months. Value Creation Drivers bar chart breaking down the $17.6 million in value created across revenue growth, EBITDA expansion, multiple expansion, and debt paydown. Equity Scaling line chart projecting equity value from $1.84 million today to $5.8 million across six additional acquisitions.

### Deal Flow
M&A acquisition pipeline. 8 active targets, $142 million total pipeline value, $4.2 million projected equity across LOI and closed stages. Target Companies table showing entry EV, post-system EV, equity percentage, and deal stage for each target. Post-system EV projections apply the same value creation framework proven at Apex — 14 percent revenue lift, margin expansion from 9 to 16 percent, multiple expansion from 5x to 7.5x.

---

## The Three Phases

Every screen in the platform references three operational phases shown as chips in the bottom left corner.

**WD — Workflow Redesign**
Maps how work actually happens across people, systems, and handoffs. Workflows are redesigned around AI so software can execute end to end.

**SC — System Construction**
The actual software is built and deployed — unified data, encoded business logic, AI reasoning, integration with existing tools.

**CC — Command and Control**
The system runs in production with ongoing responsibility for performance. This is the phase that justifies equity over fees.

In Apex's case — WD done, SC done, CC active.

---

## The Equity Model

Traditional consulting charges a fee and exits. This platform is built around a different model — equity is taken instead of full fees and earned through the CC phase. When you're responsible for ongoing performance across a portfolio, a fee doesn't reflect that relationship. Equity does.

The Value Tracker makes that math visible. $95,000 deployed. $1.84 million in equity value. 19.4x return in 14 months. Scales to $5.8 million across six additional acquisitions on the same system with near-zero marginal deployment cost.

---

## How It Was Built

**Stack**
- HTML, CSS, JavaScript — no frameworks
- Chart.js 4.4.1 via CDN for all charts
- Syne (Google Fonts) for headings and numbers
- Trebuchet MS for body text
- Python for file generation and local server

**File structure**
bhatera-dashboard/
├── index.html              # All views and HTML structure
├── style.css               # Full design system
├── app.js                  # Navigation logic and all Chart.js instances
└── generate_dashboard.py   # Python script that generates files and serves locally

**Running locally**
```bash
python3 generate_dashboard.py
```
Opens automatically at `http://localhost:8000`

Or if you already have the files:
```bash
cd bhatera-dashboard
python3 -m http.server 8000
```

**Design system**
- Background: `#05070E` with layered radial gradients
- Gold accent: `#c49f75` — value creation, active states, positive metrics
- Blue accent: `#1a3a5c` — neutral, completed, operational metrics
- Red: `#E05050` — attention required
- All chart colors reference the same palette
- Half-pixel borders throughout for precision at high-DPI screens

---

## The Business Context

Roll-up strategies have become one of the most common value creation playbooks in private equity — acquiring fragmented, operationally similar businesses, consolidating them under one platform, and driving margin expansion through standardization. In practice, the execution gap between the acquisition model and actual performance is where most roll-ups struggle. Margins projected at underwriting rarely materialize because there is no system enforcing the operational improvements. Everything depends on key people, manual processes, and inconsistent workflows across locations.

This platform is built around the idea that AI can serve as the operating layer that closes that gap. By redesigning workflows around software, encoding institutional knowledge into a compounding knowledge base, and maintaining ongoing operational control across every location, the system creates measurable financial value — revenue lift, margin expansion, and multiple expansion — that compounds as the portfolio scales. Rather than charging a consulting fee and exiting, the model is built around taking equity and earning it through ongoing performance. The result is a platform that scales like software, not services — near-zero marginal cost per new acquisition on a system already proven across the existing portfolio.
