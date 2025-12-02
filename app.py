import requests
import time
from datetime import datetime

SITES_PARA_MONITORAR = [
    "https://www.google.com",
    "https://github.com",
    "https://www.ifood.com.br"
]

def verificar_site(url):
    try:
        inicio = time.time()
        resposta = requests.get(url, timeout=5)
        fim = time.time()
        tempo_resposta = round(fim - inicio, 3)
        
        if resposta.status_code == 200:
            return "ONLINE", tempo_resposta
        else:
            return f"ERRO {resposta.status_code}", tempo_resposta
    except requests.exceptions.RequestException:
        return "OFFLINE", 0

def main():
    print(f"🛡️  INICIANDO MONITORAMENTO - {datetime.now()}")
    print("-" * 50)
    
    for site in SITES_PARA_MONITORAR:
        status, tempo = verificar_site(site)
        cor = "✅" if status == "ONLINE" else "❌"
        print(f"{cor} {site} | Status: {status} | Latência: {tempo}s")

if __name__ == "__main__":
    main()