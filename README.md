# website-health-monitor

# 🛡️ Website Health Monitor

![DevOps](https://img.shields.io/badge/DevOps-Monitoring-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Online-brightgreen?style=for-the-badge)

## 📖 Sobre o Projeto
Script de monitoramento de disponibilidade (Uptime) e latência para aplicações web. Projetado para rodar em background, ele verifica periodicamente o status HTTP de uma lista de endpoints críticos, garantindo observabilidade básica de serviços.

## 🚀 Funcionalidades
- **Verificação de Status Code:** Identifica se o site está online (200 OK) ou com erro (404, 500).
- **Medidor de Latência:** Calcula o tempo de resposta em milissegundos.
- **Logs de Execução:** Gera output detalhado no console com timestamp.

## 🛠️ Tecnologias
- Python 3 standard libraries (Time, Datetime)
- Requests Library
- Tratamento de Exceções (Error Handling)

## ⚙️ Instalação
```bash
pip install requests
python monitor.py
