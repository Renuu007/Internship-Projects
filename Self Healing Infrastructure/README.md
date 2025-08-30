# Self Healing Infrastructure

This project demonstrates a self-healing infrastructure using Prometheus, Alertmanager, and Ansible. It automatically detects failures (such as a downed Nginx service) and triggers automated recovery actions.

## Features
- **Monitoring:** Prometheus monitors the health of services.
- **Alerting:** Alertmanager sends alerts based on Prometheus rules.
- **Automated Recovery:** Alerts trigger a webhook that runs Ansible playbooks to recover failed services (e.g., restart Nginx).
- **Containerized:** All components run in Docker containers for easy deployment.

## Project Structure
```
Self Healing Infrastructure/
├── alert.rules.yml         # Prometheus alerting rules
├── alertmanager.yml        # Alertmanager configuration
├── docker-compose.yml      # Docker Compose setup for all services
├── Dockerfile              # Dockerfile for custom webhook app
├── project.txt             # Project notes or documentation
├── prometheus.yml          # Prometheus configuration
├── requirements.txt        # Python dependencies for webhook app
├── webhook_app.py          # Flask app to receive alerts and trigger playbooks
└── playbooks/
    └── recover_nginx.yml   # Ansible playbook to recover Nginx
```

## How It Works
1. **Prometheus** scrapes metrics and applies alerting rules from `alert.rules.yml`.
2. **Alertmanager** receives alerts and sends a webhook to the Flask app (`webhook_app.py`).
3. The **Flask webhook app** triggers the appropriate Ansible playbook (e.g., `recover_nginx.yml`) to recover the failed service.
4. All components are orchestrated using **Docker Compose**.

## Getting Started
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Renuu007/Internship-Projects
   cd "Self Healing Infrastructure"
   ```
2. **Build and start the services:**
   ```sh
   docker-compose up --build
   ```
3. **Test the setup:**
   - Stop the Nginx service to simulate a failure.
   - Prometheus detects the failure and triggers an alert.
   - The webhook app runs the Ansible playbook to recover Nginx.

## Requirements
- Docker & Docker Compose
- Python 3.x (for running the webhook app locally)
- Ansible (for running playbooks)

## Configuration
- **Prometheus:** `prometheus.yml`, `alert.rules.yml`
- **Alertmanager:** `alertmanager.yml`
- **Webhook App:** `webhook_app.py`, `requirements.txt`
- **Ansible Playbooks:** `playbooks/recover_nginx.yml`

## License
This project is for educational purposes.
