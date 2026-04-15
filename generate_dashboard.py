#!/usr/bin/env python3
"""
Ciridae Command Center — Dashboard Generator
Run: python3 generate_dashboard.py
Opens dashboard at http://localhost:8000
"""

import os
import http.server
import threading
import webbrowser

# ── OUTPUT FOLDER ──────────────────────────────
OUT = "ciridae-dashboard"
os.makedirs(OUT, exist_ok=True)

# ══════════════════════════════════════════════
# INDEX.HTML
# ══════════════════════════════════════════════
HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Ciidae — Command Center</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
</head>
<body>
<div class="app">
  <div class="app-bg"></div>

  <aside class="sidebar">
    <div class="brand">
      <div class="brand-row">
        <svg class="logo-mark" viewBox="0 0 100 95" fill="white">
          <path d="M50 3C51 18 63 20 90 30 76 37 70 48 74 82 62 68 54 65 30 82 34 48 28 37 10 30 37 20 49 18 50 3Z"/>
        </svg>
        <span class="brand-name">Ciidae</span>
      </div>
      <div class="client-pill">
        <div class="cl">Active client</div>
        <div class="cn">Apex Restoration Group</div>
      </div>
    </div>

    <nav>
      <div class="nl">Platform</div>
      <a class="ni active" data-view="overview">
        <svg class="ic" viewBox="0 0 16 16" fill="currentColor"><rect x="1" y="1" width="6" height="6" rx="1.5"/><rect x="9" y="1" width="6" height="6" rx="1.5"/><rect x="1" y="9" width="6" height="6" rx="1.5"/><rect x="9" y="9" width="6" height="6" rx="1.5"/></svg>
        Overview
      </a>
      <a class="ni" data-view="locations">
        <svg class="ic" viewBox="0 0 16 16" fill="currentColor"><circle cx="8" cy="5" r="3"/><path d="M2 14c0-2.2 2.7-4 6-4s6 1.8 6 4H2z"/></svg>
        Locations <span class="badge">6</span>
      </a>
      <a class="ni" data-view="rebuttals">
        <svg class="ic" viewBox="0 0 16 16" fill="currentColor"><path d="M2 3h12v2H2zm0 4h8v2H2zm0 4h10v2H2z"/></svg>
        Rebuttals <span class="badge">14</span>
      </a>
      <a class="ni" data-view="pipeline">
        <svg class="ic" viewBox="0 0 16 16" fill="currentColor"><path d="M1 3h14v2H1zm2 4h10v2H3zm2 4h6v2H5z"/></svg>
        Job Pipeline
      </a>
      <div class="nl">Intelligence</div>
      <a class="ni" data-view="knowledge">
        <svg class="ic" viewBox="0 0 16 16" fill="currentColor"><path d="M8 1a5 5 0 100 10A5 5 0 008 1zm0 2a3 3 0 110 6A3 3 0 018 3zM6 13h4v2H6z"/></svg>
        Knowledge Base
      </a>
      <div class="nl">Equity</div>
      <a class="ni" data-view="equity">
        <svg class="ic" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><polyline points="2,12 6,7 9,10 14,4"/></svg>
        Value Tracker
      </a>
    </nav>

    <div class="sf">
      <div class="fl">Deployment Phase</div>
      <div class="chips">
        <span class="chip cd">WD ✓</span>
        <span class="chip cd">SC ✓</span>
        <span class="chip ca">CC →</span>
      </div>
    </div>
  </aside>

  <main class="main">
    <header class="topbar">
      <div>
        <div class="tt" id="view-title">Portfolio Overview</div>
        <div class="ts">Apex Restoration Group · 6 locations · Month 14</div>
      </div>
      <div class="tr">
        <select class="psel">
          <option>Last 30 days</option>
          <option>Last 90 days</option>
          <option>Since deployment</option>
        </select>
        <div class="live"><div class="ld"></div><span class="lt">All systems live</span></div>
      </div>
    </header>

    <div class="content">

      <!-- OVERVIEW -->
      <section class="view active" id="view-overview">
        <div class="mrow">
          <div class="mc hl-or"><div class="ml">Portfolio Revenue</div><div class="mv or">$21.9M</div><div class="md up">↑ +$2.7M vs. pre-deployment</div></div>
          <div class="mc hl-bl"><div class="ml">EBITDA</div><div class="mv bl">$3.5M</div><div class="md up">↑ 16% margin (was 9%)</div></div>
          <div class="mc"><div class="ml">Cash Collection Cycle</div><div class="mv bl">41 days</div><div class="md up">↓ from 74 days at entry</div></div>
          <div class="mc hl-or"><div class="ml">Value Created</div><div class="mv or">$17.6M</div><div class="md dm">vs. $8.6M entry valuation</div></div>
        </div>
        <div class="g2">
          <div class="panel"><div class="ph"><span class="pt">Revenue &amp; EBITDA Trend</span><span class="tor">+14% since deployment</span></div><div class="cw" style="height:165px"><canvas id="c-rev" role="img" aria-label="Revenue and EBITDA trend over 14 months">Revenue $19.2M to $21.9M; EBITDA $1.73M to $3.5M.</canvas></div></div>
          <div class="panel">
            <div class="ph"><span class="pt">System Metrics</span></div>
            <div class="sm2">
              <div class="smc"><div class="sl">Rebuttal Approval</div><div class="sv bl">81%</div></div>
              <div class="smc"><div class="sl">Avg Response Time</div><div class="sv">11 min</div></div>
              <div class="smc"><div class="sl">Active Jobs</div><div class="sv">47</div></div>
              <div class="smc"><div class="sl">KB Strategies</div><div class="sv or">312</div></div>
            </div>
            <div class="plbl">EBITDA margin toward 18% target</div>
            <div class="pbar"><div class="pfill" style="width:89%"></div></div>
            <div class="pends"><span>Current 16%</span><span>Target 18%</span></div>
          </div>
        </div>
        <div class="panel"><div class="ph"><span class="pt">Deployment Phases</span></div>
          <div class="phr">
            <div class="phb phbd"><div class="phn">Phase 01</div><div class="phname">WD</div><div class="phs" style="color:#4a5668">Complete · all 6 locations</div></div>
            <div class="phb phbd"><div class="phn">Phase 02</div><div class="phname">SC</div><div class="phs" style="color:#4a5668">Complete · live in production</div></div>
            <div class="phb phba"><div class="phn">Phase 03</div><div class="phname">CC</div><div class="phs" style="color:#c49f75">Active · month 10 of ongoing</div></div>
          </div>
        </div>
      </section>

      <!-- LOCATIONS -->
      <section class="view" id="view-locations">
        <div class="mrow">
          <div class="mc hl-bl"><div class="ml">Locations Live</div><div class="mv bl">6 / 6</div></div>
          <div class="mc hl-or"><div class="ml">Top Margin</div><div class="mv or">19.2%</div><div class="md dm">Dallas North</div></div>
          <div class="mc"><div class="ml">Needs Attention</div><div class="mv" style="color:#E05050">12.8%</div><div class="md dm">Fort Worth</div></div>
          <div class="mc"><div class="ml">Avg Cash Cycle</div><div class="mv bl">41 days</div></div>
        </div>
        <div class="panel"><div class="ph"><span class="pt">Location Performance</span></div>
          <table class="tbl">
            <thead><tr><th>Location</th><th class="r">Revenue</th><th class="r">EBITDA</th><th class="r">Margin</th><th class="r">Cash Cycle</th><th class="r">Status</th></tr></thead>
            <tbody>
              <tr><td><div class="lc"><span class="ln">L1</span>Dallas North</div></td><td class="r fw">$4.1M</td><td class="r dm">$788K</td><td class="r" style="color:#c49f75">19.2%</td><td class="r" style="color:#c49f75">36d</td><td class="r"><span class="pill pbl">Live</span></td></tr>
              <tr><td><div class="lc"><span class="ln">L2</span>Dallas South</div></td><td class="r fw">$3.8M</td><td class="r dm">$684K</td><td class="r" style="color:#c49f75">18.0%</td><td class="r" style="color:#c49f75">39d</td><td class="r"><span class="pill pbl">Live</span></td></tr>
              <tr><td><div class="lc"><span class="ln">L3</span>Plano</div></td><td class="r fw">$3.6M</td><td class="r dm">$612K</td><td class="r" style="color:#c49f75">17.0%</td><td class="r" style="color:#c49f75">41d</td><td class="r"><span class="pill pbl">Live</span></td></tr>
              <tr><td><div class="lc"><span class="ln">L4</span>Arlington</div></td><td class="r fw">$3.4M</td><td class="r dm">$544K</td><td class="r" style="color:#d4b08a">16.0%</td><td class="r" style="color:#d4b08a">44d</td><td class="r"><span class="pill pbl">Live</span></td></tr>
              <tr><td><div class="lc"><span class="ln">L5</span>Irving</div></td><td class="r fw">$3.5M</td><td class="r dm">$525K</td><td class="r" style="color:#d4b08a">15.0%</td><td class="r" style="color:#d4b08a">43d</td><td class="r"><span class="pill pbl">Live</span></td></tr>
              <tr><td><div class="lc"><span class="ln">L6</span>Fort Worth</div></td><td class="r fw">$3.5M</td><td class="r dm">$448K</td><td class="r" style="color:#E05050">12.8%</td><td class="r" style="color:#E05050">52d</td><td class="r"><span class="pill por">Optimizing</span></td></tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- REBUTTALS -->
      <section class="view" id="view-rebuttals">
        <div class="mrow">
          <div class="mc hl-bl"><div class="ml">Approval Rate</div><div class="mv bl">81%</div><div class="md up">↑ from ~52% pre-deployment</div></div>
          <div class="mc"><div class="ml">Avg Response Time</div><div class="mv">11 min</div><div class="md up">↓ from 3 hrs manual</div></div>
          <div class="mc hl-or"><div class="ml">$ Recovered MTD</div><div class="mv or">$184K</div><div class="md up">↑ +$62K vs. baseline</div></div>
          <div class="mc"><div class="ml">Active Rebuttals</div><div class="mv">14</div></div>
        </div>
        <div class="g2">
          <div class="panel"><div class="ph"><span class="pt">Active Rebuttal Queue</span></div>
            <table class="tbl">
              <thead><tr><th>Job ID</th><th>Property</th><th>Insurer</th><th class="r">Disputed</th><th class="r">Status</th></tr></thead>
              <tbody>
                <tr><td class="dsm">#R-1142</td><td>2847 Oak Ridge Dr</td><td class="dm">State Farm</td><td class="r fw">$18.4K</td><td class="r"><span class="pill pbl">Won</span></td></tr>
                <tr><td class="dsm">#R-1148</td><td>114 Creekside Blvd</td><td class="dm">Allstate</td><td class="r fw">$22.1K</td><td class="r"><span class="pill por">Round 3</span></td></tr>
                <tr><td class="dsm">#R-1151</td><td>910 Westpark Commons</td><td class="dm">USAA</td><td class="r fw">$31.8K</td><td class="r"><span class="pill pgr">Sent</span></td></tr>
                <tr><td class="dsm">#R-1154</td><td>432 Maple Creek Ct</td><td class="dm">Farmers</td><td class="r fw">$14.7K</td><td class="r"><span class="pill pyw">Drafting</span></td></tr>
                <tr><td class="dsm">#R-1157</td><td>7701 Heritage Trail</td><td class="dm">Liberty</td><td class="r fw">$9.2K</td><td class="r"><span class="pill pgr">Sent</span></td></tr>
              </tbody>
            </table>
          </div>
          <div class="panel"><div class="ph"><span class="pt">Approval Rate by Insurer</span></div><div class="cw" style="height:200px"><canvas id="c-ins" role="img" aria-label="Approval rates by insurer">State Farm 88%, USAA 84%, Allstate 79%, Farmers 76%, Liberty 71%.</canvas></div></div>
        </div>
      </section>

      <!-- PIPELINE -->
      <section class="view" id="view-pipeline">
        <div class="mrow">
          <div class="mc hl-bl"><div class="ml">Active Jobs</div><div class="mv bl">47</div></div>
          <div class="mc hl-or"><div class="ml">Pipeline Value</div><div class="mv or">$2.1M</div></div>
          <div class="mc"><div class="ml">Avg Job Value</div><div class="mv">$44.7K</div></div>
          <div class="mc"><div class="ml">Est. Close MTD</div><div class="mv bl">$680K</div></div>
        </div>
        <div class="panel" style="margin-bottom:12px"><div class="ph"><span class="pt">Pipeline by Stage</span></div><div class="cw" style="height:150px"><canvas id="c-pipe" role="img" aria-label="Pipeline stages">Scoping 12, Estimating 9, Submitted 11, In rebuttal 8, Approved 7.</canvas></div></div>
        <div class="panel"><div class="ph"><span class="pt">Jobs Requiring Attention</span><span class="tor">3 flagged</span></div>
          <table class="tbl">
            <thead><tr><th>Job ID</th><th>Issue</th><th>Value</th><th>Action</th><th>Location</th></tr></thead>
            <tbody>
              <tr><td class="dsm">#J-881</td><td>5th round — adjuster stalling</td><td class="fw">$38.2K</td><td style="color:#E05050">Escalate</td><td class="dm">Fort Worth · L6</td></tr>
              <tr><td class="dsm">#J-874</td><td>Missing supplement docs</td><td class="fw">$24.5K</td><td style="color:#C8A840">Action needed</td><td class="dm">Irving · L5</td></tr>
              <tr><td class="dsm">#J-869</td><td>74 days unpaid — send demand</td><td class="fw">$19.1K</td><td style="color:#E05050">Overdue</td><td class="dm">Dallas South · L2</td></tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- KNOWLEDGE BASE -->
      <section class="view" id="view-knowledge">
        <div class="mrow">
          <div class="mc hl-or"><div class="ml">Strategies Encoded</div><div class="mv or">312</div></div>
          <div class="mc hl-bl"><div class="ml">Avg Win Rate</div><div class="mv bl">81%</div></div>
          <div class="mc"><div class="ml">Cross-Loc Deploys</div><div class="mv">148</div><div class="md dm">strategies shared</div></div>
          <div class="mc"><div class="ml">Newest Strategy</div><div class="mv" style="font-size:16px">2h ago</div></div>
        </div>
        <div class="panel"><div class="ph"><span class="pt">Top Performing Rebuttal Strategies</span></div>
          <table class="tbl">
            <thead><tr><th>Category</th><th>Strategy</th><th class="r">Win Rate</th><th class="r">Uses</th></tr></thead>
            <tbody>
              <tr><td><span class="kbt">Contents</span></td><td class="dm">Per-room ACV formula with waste allowance trigger</td><td class="r" style="color:#c49f75;font-weight:600">94%</td><td class="r dm">48×</td></tr>
              <tr><td><span class="kbt">Drywall</span></td><td class="dm">ASTM C840 taping standard — adjuster omit counter</td><td class="r" style="color:#c49f75;font-weight:600">88%</td><td class="r dm">61×</td></tr>
              <tr><td><span class="kbt">Paint</span></td><td class="dm">Two-coat standard with existing surface guidance</td><td class="r" style="color:#c49f75;font-weight:600">85%</td><td class="r dm">73×</td></tr>
              <tr><td><span class="kbt">Carpet</span></td><td class="dm">Pad replacement + waste allowance when removal required</td><td class="r" style="color:#d4b08a;font-weight:600">79%</td><td class="r dm">39×</td></tr>
              <tr><td><span class="kbt">Supplement</span></td><td class="dm">Texture match + uniform appearance flagging protocol</td><td class="r" style="color:#d4b08a;font-weight:600">76%</td><td class="r dm">55×</td></tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- EQUITY -->
      <section class="view" id="view-equity">
        <div class="g2">
          <div class="panel">
            <div class="eqc"><div class="eqv">$1.84M</div><div class="eql">Ciidae equity value — 7% stake</div></div>
            <div class="eqr"><span class="eqk">Entry platform value</span><span class="eqval">$8.6M</span></div>
            <div class="eqr"><span class="eqk">Current platform value</span><span class="eqval bl">$26.2M</span></div>
            <div class="eqr"><span class="eqk">Ciidae stake</span><span class="eqval">7%</span></div>
            <div class="eqr"><span class="eqk">Cash deployed</span><span class="eqval">$95K</span></div>
            <div class="eqr"><span class="eqk">Cash-on-cash return</span><span class="eqval or">19.4×</span></div>
            <div class="eqr"><span class="eqk">Months active</span><span class="eqval">14</span></div>
          </div>
          <div class="panel"><div class="ph"><span class="pt">Value Creation Drivers</span></div><div class="cw" style="height:200px"><canvas id="c-val" role="img" aria-label="Value creation breakdown">Entry $8.6M + Revenue $3.4M + Margin $7.1M + Multiple $6.5M = $26.2M.</canvas></div></div>
        </div>
        <div class="panel" style="margin-top:12px"><div class="ph"><span class="pt">Equity Scaling — Next Acquisitions</span><span class="tbl2">19× cash-on-cash today</span></div><div class="cw" style="height:145px"><canvas id="c-scale" role="img" aria-label="Equity scaling">$1.84M at 6 locations to $5.8M at 18 locations.</canvas></div></div>
      </section>

    </div>
  </main>
</div>
<script src="app.js"></script>
</body>
</html>"""

# ══════════════════════════════════════════════
# STYLE.CSS
# ══════════════════════════════════════════════
CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --or: #c49f75; --or2: #d4b08a;
  --bl: #394351; --bl2: #4a5668;
  --bg: #05070E; --bg2: rgba(8,11,22,.82);
  --bd: rgba(255,255,255,.07);
  --font: "Trebuchet MS", Helvetica, sans-serif;
}
html, body { height: 100%; overflow: hidden; }
body { background: var(--bg); color: #fff; font-family: var(--font); -webkit-font-smoothing: antialiased; }

.app { display: flex; height: 100vh; position: relative; overflow: hidden; }
.app-bg { position: absolute; inset: 0; z-index: 0;
  background:
    radial-gradient(ellipse 48% 38% at 10% 18%, rgba(196,159,117,.28) 0%, transparent 56%),
    radial-gradient(ellipse 55% 45% at 78% 60%, rgba(57,67,81,.35) 0%, transparent 58%),
    radial-gradient(ellipse 85% 75% at 50% 50%, rgba(5,8,28,.88) 0%, transparent 100%),
    #05070E; }

.sidebar { width: 214px; flex-shrink: 0; background: rgba(3,4,10,.92); border-right: 0.5px solid var(--bd); display: flex; flex-direction: column; padding: 22px 0; position: relative; z-index: 2; overflow-y: auto; }
.brand { padding: 0 18px 18px; border-bottom: 0.5px solid var(--bd); margin-bottom: 14px; }
.brand-row { display: flex; align-items: center; gap: 9px; margin-bottom: 10px; }
.logo-mark { width: 22px; height: 22px; flex-shrink: 0; }
.brand-name { font-family: 'Syne', var(--font); font-size: 13px; font-weight: 800; letter-spacing: .22em; color: #fff; text-transform: uppercase; }
.client-pill { background: rgba(196,159,117,.1); border: 0.5px solid rgba(196,159,117,.25); border-radius: 6px; padding: 6px 10px; }
.cl { font-size: 9px; color: rgba(255,255,255,.3); letter-spacing: .1em; text-transform: uppercase; margin-bottom: 2px; }
.cn { font-size: 12px; color: var(--or); font-weight: 600; }
.nl { font-size: 9px; letter-spacing: .22em; color: rgba(255,255,255,.18); text-transform: uppercase; padding: 0 18px; margin: 12px 0 5px; }
.ni { display: flex; align-items: center; gap: 9px; padding: 8px 16px; cursor: pointer; font-size: 12.5px; color: rgba(255,255,255,.38); text-decoration: none; transition: all .12s; margin: 1px 8px; border-radius: 7px; border: 0.5px solid transparent; }
.ni:hover { color: rgba(255,255,255,.72); background: rgba(255,255,255,.04); }
.ni.active { color: var(--or); background: rgba(196,159,117,.1); border-color: rgba(196,159,117,.22); }
.ic { width: 13px; height: 13px; flex-shrink: 0; opacity: .55; }
.ni.active .ic { opacity: 1; }
.badge { margin-left: auto; background: rgba(57,67,81,.4); color: var(--bl2); font-size: 9.5px; padding: 1px 6px; border-radius: 8px; }
.sf { margin-top: auto; padding: 14px 18px 0; border-top: 0.5px solid var(--bd); }
.fl { font-size: 9px; letter-spacing: .18em; color: rgba(255,255,255,.18); text-transform: uppercase; margin-bottom: 8px; }
.chips { display: flex; gap: 5px; }
.chip { font-size: 9px; padding: 3px 8px; border-radius: 4px; font-weight: 600; letter-spacing: .05em; }
.cd { background: rgba(57,67,81,.3); color: var(--bl2); border: 0.5px solid rgba(57,67,81,.4); }
.ca { background: rgba(196,159,117,.15); color: var(--or); border: 0.5px solid rgba(196,159,117,.28); }

.main { flex: 1; display: flex; flex-direction: column; overflow: hidden; position: relative; z-index: 2; }
.topbar { padding: 16px 24px; border-bottom: 0.5px solid var(--bd); display: flex; align-items: center; justify-content: space-between; flex-shrink: 0; background: rgba(3,5,12,.65); }
.tt { font-family: 'Syne', var(--font); font-size: 14px; font-weight: 700; color: #fff; letter-spacing: .07em; text-transform: uppercase; }
.ts { font-size: 11px; color: rgba(255,255,255,.28); margin-top: 3px; }
.tr { display: flex; align-items: center; gap: 12px; }
.psel { background: rgba(255,255,255,.05); border: 0.5px solid rgba(255,255,255,.1); border-radius: 6px; color: rgba(255,255,255,.5); font-size: 11.5px; font-family: var(--font); padding: 5px 11px; cursor: pointer; outline: none; }
.live { display: flex; align-items: center; gap: 6px; }
.ld { width: 6px; height: 6px; border-radius: 50%; background: var(--or); }
.lt { font-size: 11px; color: rgba(255,255,255,.32); }

.content { flex: 1; overflow-y: auto; padding: 20px 24px; }
.content::-webkit-scrollbar { width: 4px; }
.content::-webkit-scrollbar-thumb { background: rgba(255,255,255,.1); border-radius: 2px; }
.view { display: none; }
.view.active { display: block; }

.mrow { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 10px; margin-bottom: 14px; }
.mc { background: var(--bg2); border: 0.5px solid var(--bd); border-radius: 9px; padding: 13px 15px; }
.mc.hl-or { border-color: rgba(196,159,117,.3); background: rgba(196,159,117,.07); }
.mc.hl-bl { border-color: rgba(57,67,81,.5); background: rgba(57,67,81,.18); }
.ml { font-size: 9.5px; color: rgba(255,255,255,.28); letter-spacing: .13em; text-transform: uppercase; margin-bottom: 6px; }
.mv { font-size: 22px; font-weight: 700; font-family: 'Syne', var(--font); color: #fff; line-height: 1; }
.mv.or { color: var(--or); } .mv.bl { color: var(--bl2); }
.md { font-size: 10.5px; margin-top: 5px; } .md.up { color: var(--or2); } .md.dm { color: rgba(255,255,255,.28); }

.panel { background: var(--bg2); border: 0.5px solid var(--bd); border-radius: 9px; padding: 15px; }
.ph { display: flex; justify-content: space-between; align-items: center; margin-bottom: 13px; }
.pt { font-size: 10.5px; color: rgba(255,255,255,.38); letter-spacing: .14em; text-transform: uppercase; }
.tor { font-size: 9.5px; background: rgba(196,159,117,.14); color: var(--or); padding: 2px 8px; border-radius: 4px; border: 0.5px solid rgba(196,159,117,.22); }
.tbl2 { font-size: 9.5px; background: rgba(57,67,81,.3); color: var(--bl2); padding: 2px 8px; border-radius: 4px; border: 0.5px solid rgba(57,67,81,.4); }
.g2 { display: grid; grid-template-columns: minmax(0,1.6fr) minmax(0,1fr); gap: 12px; margin-bottom: 12px; }

.sm2 { display: grid; grid-template-columns: 1fr 1fr; gap: 7px; margin-bottom: 11px; }
.smc { background: rgba(255,255,255,.04); border-radius: 7px; padding: 9px 11px; }
.sl { font-size: 9.5px; color: rgba(255,255,255,.26); margin-bottom: 3px; }
.sv { font-size: 15px; font-weight: 700; font-family: 'Syne', var(--font); color: #fff; }
.sv.or { color: var(--or); } .sv.bl { color: var(--bl2); }

.plbl { font-size: 10px; color: rgba(255,255,255,.26); margin-bottom: 5px; }
.pbar { height: 4px; background: rgba(255,255,255,.07); border-radius: 2px; }
.pfill { height: 4px; border-radius: 2px; background: var(--or); }
.pends { display: flex; justify-content: space-between; font-size: 10px; color: rgba(255,255,255,.26); margin-top: 4px; }

.phr { display: flex; gap: 10px; }
.phb { flex: 1; border-radius: 8px; padding: 12px 13px; }
.phbd { background: rgba(57,67,81,.15); border: 0.5px solid rgba(57,67,81,.35); }
.phba { background: rgba(196,159,117,.07); border: 0.5px solid rgba(196,159,117,.28); }
.phn { font-size: 9px; color: rgba(255,255,255,.22); letter-spacing: .16em; text-transform: uppercase; margin-bottom: 3px; }
.phname { font-family: 'Syne', var(--font); font-size: 12px; font-weight: 800; color: #fff; margin-bottom: 2px; letter-spacing: .06em; text-transform: uppercase; }
.phs { font-size: 11px; }

.tbl { width: 100%; border-collapse: collapse; }
.tbl th { text-align: left; padding: 6px 8px; font-size: 9.5px; letter-spacing: .12em; text-transform: uppercase; color: rgba(255,255,255,.22); border-bottom: 0.5px solid rgba(255,255,255,.08); font-weight: 400; }
.tbl td { padding: 8px 8px; font-size: 12px; color: rgba(255,255,255,.72); border-bottom: 0.5px solid rgba(255,255,255,.04); }
.tbl tbody tr:last-child td { border-bottom: none; }
.tbl td.r, .tbl th.r { text-align: right; }
.tbl td.fw { font-weight: 600; color: #fff; }
.tbl td.dm { color: rgba(255,255,255,.4); }
.tbl td.dsm { font-size: 10.5px; color: rgba(255,255,255,.28); }
.lc { display: flex; align-items: center; gap: 8px; }
.ln { width: 22px; height: 22px; border-radius: 5px; background: rgba(196,159,117,.13); color: var(--or); font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.pill { font-size: 9.5px; padding: 2px 8px; border-radius: 4px; display: inline-block; }
.pbl { background: rgba(57,67,81,.3); color: var(--bl2); border: 0.5px solid rgba(57,67,81,.4); }
.por { background: rgba(196,159,117,.14); color: var(--or); border: 0.5px solid rgba(196,159,117,.22); }
.pgr { background: rgba(100,120,160,.15); color: #8AA0C8; border: 0.5px solid rgba(100,120,160,.2); }
.pyw { background: rgba(180,140,60,.12); color: #C8A840; border: 0.5px solid rgba(180,140,60,.2); }
.kbt { font-size: 9.5px; padding: 2px 8px; border-radius: 4px; background: rgba(57,67,81,.28); color: var(--bl2); border: 0.5px solid rgba(57,67,81,.4); display: inline-block; }

.eqc { text-align: center; padding: 18px 0 14px; }
.eqv { font-family: 'Syne', var(--font); font-size: 44px; font-weight: 800; color: var(--or); line-height: 1; }
.eql { font-size: 10px; color: rgba(255,255,255,.26); letter-spacing: .16em; text-transform: uppercase; margin-top: 5px; }
.eqr { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 0.5px solid rgba(255,255,255,.05); font-size: 12px; }
.eqr:last-child { border-bottom: none; }
.eqk { color: rgba(255,255,255,.34); }
.eqval { color: #fff; font-weight: 600; }
.eqval.or { color: var(--or); } .eqval.bl { color: var(--bl2); }
.cw { position: relative; }
"""

# ══════════════════════════════════════════════
# APP.JS
# ══════════════════════════════════════════════
JS = """
// ── NAVIGATION
const titles = {
  overview: 'Portfolio Overview', locations: 'Location Performance',
  rebuttals: 'Rebuttal Engine', pipeline: 'Job Pipeline',
  knowledge: 'Knowledge Base', equity: 'Value Tracker'
};
document.querySelectorAll('.ni').forEach(function(item) {
  item.addEventListener('click', function() {
    const id = this.getAttribute('data-view');
    document.querySelectorAll('.view').forEach(function(v) { v.classList.remove('active'); });
    document.querySelectorAll('.ni').forEach(function(n) { n.classList.remove('active'); });
    document.getElementById('view-' + id).classList.add('active');
    this.classList.add('active');
    document.getElementById('view-title').textContent = titles[id];
  });
});

// ── CHART HELPERS
const gc = { color: 'rgba(255,255,255,0.05)' };
const tc = { color: 'rgba(255,255,255,0.32)', font: { size: 10, family: '"Trebuchet MS", Helvetica, sans-serif' } };
const base = { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: gc, ticks: tc }, y: { grid: gc, ticks: tc } } };

// ── REVENUE CHART
new Chart(document.getElementById('c-rev'), {
  type: 'line',
  data: {
    labels: ['M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11','M12','M13','M14'],
    datasets: [
      { label: 'Revenue ($M)', data: [19.2,19.4,19.7,19.9,20.1,20.3,20.5,20.7,20.9,21.1,21.3,21.5,21.7,21.9], borderColor: '#c49f75', backgroundColor: 'rgba(196,159,117,.07)', fill: true, tension: 0.4, pointRadius: 2 },
      { label: 'EBITDA ($M)', data: [1.73,1.82,1.95,2.06,2.18,2.28,2.45,2.62,2.8,2.98,3.1,3.22,3.38,3.5], borderColor: '#394351', backgroundColor: 'rgba(57,67,81,.12)', fill: true, tension: 0.4, pointRadius: 2 }
    ]
  },
  options: Object.assign({}, base, {
    plugins: { legend: { display: true, position: 'top', labels: { color: 'rgba(255,255,255,.42)', font: { size: 10 }, boxWidth: 8, boxHeight: 8 } } },
    scales: { x: { grid: gc, ticks: tc }, y: { grid: gc, ticks: Object.assign({}, tc, { callback: function(v) { return '$' + v + 'M'; } }) } }
  })
});

// ── INSURER CHART
new Chart(document.getElementById('c-ins'), {
  type: 'bar',
  data: { labels: ['State Farm','USAA','Allstate','Farmers','Liberty'], datasets: [{ data: [88,84,79,76,71], backgroundColor: ['#394351','#394351','#c49f75','#c49f75','#c49f75'], borderRadius: 4 }] },
  options: { indexAxis: 'y', responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } },
    scales: { x: { grid: gc, ticks: Object.assign({}, tc, { callback: function(v) { return v + '%'; } }), max: 100 }, y: { grid: { display: false }, ticks: tc } } }
});

// ── PIPELINE CHART
new Chart(document.getElementById('c-pipe'), {
  type: 'bar',
  data: { labels: ['Scoping','Estimating','Submitted','In rebuttal','Approved'], datasets: [{ data: [12,9,11,8,7], backgroundColor: ['#394351','#394351','#c49f75','#c49f75','#d4b08a'], borderRadius: 4 }] },
  options: { indexAxis: 'y', responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } },
    scales: { x: { grid: gc, ticks: tc }, y: { grid: { display: false }, ticks: tc } } }
});

// ── VALUE DRIVERS CHART
new Chart(document.getElementById('c-val'), {
  type: 'bar',
  data: { labels: ['Entry value','Revenue lift','Margin expansion','Multiple expansion'], datasets: [{ data: [8.6,3.4,7.1,6.5], backgroundColor: ['rgba(255,255,255,.1)','#c49f75','#d4b08a','#394351'], borderRadius: 4 }] },
  options: Object.assign({}, base, { scales: { x: { grid: { display: false }, ticks: tc }, y: { grid: gc, ticks: Object.assign({}, tc, { callback: function(v) { return '$' + v + 'M'; } }) } } })
});

// ── SCALING CHART
new Chart(document.getElementById('c-scale'), {
  type: 'line',
  data: {
    labels: ['6 loc','8 loc','10 loc','12 loc','15 loc','18 loc'],
    datasets: [
      { label: 'Ciidae equity', data: [1.84,2.4,3.1,3.8,4.8,5.8], borderColor: '#c49f75', backgroundColor: 'rgba(196,159,117,.08)', fill: true, tension: 0.4, pointRadius: 3 },
      { label: 'Platform value', data: [26.2,32,40,52,62,74], borderColor: '#394351', backgroundColor: 'rgba(57,67,81,.1)', fill: true, tension: 0.4, pointRadius: 3, yAxisID: 'y2' }
    ]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: { legend: { display: true, position: 'top', labels: { color: 'rgba(255,255,255,.42)', font: { size: 10 }, boxWidth: 8, boxHeight: 8 } } },
    scales: {
      x: { grid: gc, ticks: tc },
      y: { grid: gc, ticks: Object.assign({}, tc, { callback: function(v) { return '$' + v + 'M'; } }), position: 'left' },
      y2: { grid: { display: false }, ticks: Object.assign({}, tc, { callback: function(v) { return '$' + v + 'M'; } }), position: 'right' }
    }
  }
});
"""

# ══════════════════════════════════════════════
# WRITE FILES
# ══════════════════════════════════════════════
with open(os.path.join(OUT, "index.html"), "w") as f:
    f.write(HTML)
with open(os.path.join(OUT, "style.css"), "w") as f:
    f.write(CSS)
with open(os.path.join(OUT, "app.js"), "w") as f:
    f.write(JS)

print(f"Files written to /{OUT}/")
print("  index.html")
print("  style.css")
print("  app.js")

# ══════════════════════════════════════════════
# LOCAL SERVER
# ══════════════════════════════════════════════
PORT = 8000
os.chdir(OUT)

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def open_browser():
    import time
    time.sleep(0.5)
    webbrowser.open(f"http://localhost:{PORT}")

print(f"\\nServer running at http://localhost:{PORT}")
print("Press Ctrl+C to stop\\n")

threading.Thread(target=open_browser, daemon=True).start()
http.server.HTTPServer(("", PORT), Handler).serve_forever()
