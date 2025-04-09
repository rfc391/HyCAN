
# 🚀 HyCAN: Hydrogen Catalyst and Nanomaterials

![HyCAN Banner](https://img.shields.io/badge/status-active-brightgreen) ![MIT License](https://img.shields.io/github/license/rfc391/HyCAN) ![CI/CD](https://github.com/rfc391/HyCAN/actions/workflows/main.yml/badge.svg)

> Cutting-edge platform for clean hydrogen innovation, AI-powered nanomaterial analytics, and real-time monitoring.

---

## 🧠 Project Overview

HyCAN is an open-source AI-enhanced hydrogen research platform integrating:
- Advanced synthesis and reaction monitoring
- Nanomaterial classification and simulation
- Real-time dashboards for analytics
- A modular, cross-platform architecture

![Architecture](docs/architecture/hycan_architecture.png)

---

## 🔧 Features

- ⚛️ Hydrogen simulation & catalyst design
- 🤖 AI/ML models for prediction and automation
- 📈 Interactive visual dashboards
- 📊 Data ingestion, transformation, and analysis
- 🧬 Bioinformatics tools for synthetic biology workflows
- 🐳 Dockerized, scriptable, and field-deployable

---

## 💻 Installation

### 🔁 Cross-platform Installers
| Platform | Installer |
|---------|-----------|
| Ubuntu/Debian | `./build/hycan-x.x.x.deb` |
| Windows | `./build/HyCAN-Setup-x.x.x.exe` |
| Linux (Portable) | `./build/HyCAN-x86_64.AppImage` |

### 🐳 Docker
```bash
docker build -t hycan:latest .
docker-compose up --build
```

### 🧪 Manual
```bash
git clone https://github.com/rfc391/HyCAN.git
cd HyCAN
pip install -r requirements.txt
python main.py
```

---

## ⚡ Quick Start

```bash
hycan-cli --simulate data/example_data.csv --model core/anomaly_detection.py
```

Use the GUI dashboard:
```bash
hycan-cli --dashboard
```

---

## 📂 Folder Guide

| Folder | Description |
|--------|-------------|
| `core/` | AI/ML models & training logic |
| `services/` | Microservices & APIs |
| `frontend/` | Web interface files |
| `config/` | YAML/INI configs for modules |
| `visualization/` | Notebooks, dashboards, and plots |
| `tests/` | All test scripts using PyTest |
| `docs/` | User and developer documentation |

---

## 🧪 Testing

```bash
black . --check
flake8 .
pytest tests/
```

---

## 🛠️ Developer Guide

- Auto-build: GitHub Actions for `.deb`, `.exe`, `.AppImage`
- Documentation: `mkdocs serve`
- Web Dashboard: Svelte/JS frontend (served via Flask or FastAPI)

---

## 🧾 License

This project is under the [MIT License](LICENSE).

---

## 🤝 Contributing

We welcome PRs and new feature suggestions. See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md).
