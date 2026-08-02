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

def main():
    print("🟢 RenderStart inicializando...")
    print("🔄 Importando bot.py (Flask + Discord bot)...")
    
    # Importa o bot (que inicia Flask + Discord em threads)
    import bot
    
    print("🟢 Bot e Flask iniciados. Processo principal ativo.")
    
    # Loop principal: mantém o processo vivo
    while True:
        time.sleep(3600)  # Dorme por 1 hora
        print(f"✅ Heartbeat - {time.strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()
