# AI Hack Toolkit
## Overview
An AI-driven modular toolkit for ethical hacking, built during Week 10 of the grind routine: AI & Automation in Hacking.  
Focus: AI Evasion Model for bypassing defenses (trained to 85%+ accuracy).  
Mindset: 'AI hacks AI' – Automates recon, scanning, exploitation, and evasion.

## Modules
- **ReconModule**: ML-powered OSINT/vuln prediction using Scikit-Learn.
- **ScanModule**: Threaded scanning with evasion delays (AI predicts stealth).
- **ExploitModule**: Automated exploits (e.g., telnet brute-force via pexpect).
- **EvasionModule**: ML classifier for polymorphic evasion (fools AI IDS).
- **Hub**: State machine orchestrates the pipeline.

## Usage
1. Install deps: `pip install scikit-learn transitions pexpect`.
2. Run: `python3 hub.py` (set target IP).
3. Train models in evasion.py for custom accuracy.

## Win Check (Week 10 Day 6)
- Integrated toolkit on HTB target (10.129.208.46).
- Evasion accuracy: 85%.
- Mindset: 'One win this week' – AI automation fuels the fire.

## Future
- Week 11: Post-exploitation hardening.
- Grey ops integration for real-world testing.

*Ethical use only. OPSEC first.*
