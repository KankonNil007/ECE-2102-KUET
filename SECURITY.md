# Security & Safety Policy

## 🛡️ Supported Versions

The following table outlines the security and maintenance status for releases of this project:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

---

## 🔒 Reporting a Vulnerability

We take security and experimental reproducibility seriously. If you discover a vulnerability, security flaw, or electrical safety concern within this repository or firmware, please follow these steps:

1. **Do not create a public issue** to report security vulnerabilities.
2. Contact the maintainer privately via email at:
   - **Email:** [kankonnil@gmail.com](mailto:kankonnil@gmail.com)
3. Include relevant details in your report:
   - Nature of the vulnerability / security concern
   - Steps to reproduce or hardware conditions leading to the issue
   - Potential impact
4. You will receive an acknowledgment within 48 to 72 hours, along with an expected timeline for remediation.

---

## ⚡ Hardware & Electrical Safety Notice

This repository documents an **academic electronics prototype** for course **ECE 2102** at **Khulna University of Engineering & Technology (KUET)**:

1. **Low-Voltage Operation:** All circuit stages operate strictly from a regulated 5V DC supply (or USB power via the Arduino Uno). **Never** connect this circuit to AC mains voltages or unisolated high-voltage sources.
2. **Current Limiting:** Ensure proper current-limiting resistors are always placed in series with the infrared LED and indicator LEDs to prevent overheating and component failure.
3. **Common Ground Integrity:** When connecting the analog circuit to an Arduino analog pin (`A0`), verify common ground (`GND`) connection before powering on to prevent floating voltage potentials.
4. **Not a Medical Device:** This system is an educational engineering demonstration of Photoplethysmography (PPG). It is **not** medically certified (FDA/CE or equivalent) and must **never** be used for clinical diagnosis, critical patient monitoring, or life-support applications.

