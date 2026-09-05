# 🛡️ FastAPI Cyber Range Protocol (PoC)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688?logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight, high-performance **Cyber Range Laboratory Prototype** built with **FastAPI**. This project serves as a Proof of Concept (PoC) for an integrated cybersecurity training platform designed to bridge the gap between offensive exploration and defensive mitigation.

---

## 📌 Executive Summary

Many security research papers focus on isolated vulnerability testing without providing a unified, hands-on environment for comprehensive learning. This project addresses that gap by introducing a modular, web-based simulation lab. 

The current initial release features a baseline module for **Server-Side Template Injection (SSTI)**, demonstrating how user inputs interact with template engines without input sanitization.

---

## ✨ Features & Architecture

* **High-Performance Core:** Built on top of **FastAPI** for low-latency request handling and dynamic route management.
* **Modular Design:** Built to easily accommodate future vulnerability modules (e.g., SQLi, Path Traversal, SSRF) alongside security mitigation mechanisms.
* **Initial Module — SSTI Baseline:** 
  * Unfiltered user input processing via Jinja2 rendering.
  * Ideal for understanding primary template injection vectors before encountering Web Application Firewall (WAF) filters.

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI (Python)
* **Template Engine:** Jinja2
* **Server:** Uvicorn
* **Frontend:** HTML5, CSS3 / Jinja2 Templates
