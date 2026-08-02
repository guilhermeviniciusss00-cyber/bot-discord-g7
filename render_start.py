"""
Ponto de entrada para o Render.
Sobe o Flask com Gunicorn E o bot Discord simultaneamente.
Mantém o processo principal vivo com health check para evitar sleep.
"""
import os
import sys
import time
import requests

def health_check():
    """Verifica se o servidor Flask ainda está respondendo"""
    try:
        port = int(os.environ.get("PORT", 5000))
        r = requests.get(f"http://localhost:{port}/", timeout=5)
        return r.status_code == 200
    except:
        return False

import subprocess

def main():
    print("🟢 RenderStart inicializando...")
    
    # Inicia o bot.py como um processo filho
    # Isso evita problemas de import circular e garante que o bot rode de forma independente
    process = subprocess.Popen([sys.executable, "bot.py"])
    
    print(f"🟢 Bot iniciado com PID: {process.pid}")
    
    # Loop principal: mantém o processo vivo e monitora o bot
    while True:
        time.sleep(60)
        if process.poll() is not None:
            print("⚠️ Bot parou de rodar! Reiniciando...")
            process = subprocess.Popen([sys.executable, "bot.py"])
        
        # O Render mantém o serviço vivo enquanto o processo principal estiver rodando
        # e respondendo a requisições HTTP (que o bot.py faz via Flask)

if __name__ == "__main__":
    main()
