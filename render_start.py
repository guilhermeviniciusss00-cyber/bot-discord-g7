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
        r = requests.get("http://localhost:5000/", timeout=5)
        return r.status_code == 200
    except:
        return False

def main():
    print("🟢 RenderStart inicializando...")
    print("🔄 Importando bot.py (Flask + Discord bot)...")
    
    # Importa o bot (que inicia Flask + Discord em threads)
    import bot
    
    print("🟢 Bot e Flask iniciados. Processo principal ativo.")
    
    # Loop principal: mantém o processo vivo e faz health check
    while True:
        time.sleep(300)  # Verifica a cada 5 minutos
        
        if not health_check():
            print("⚠️ Flask não está respondendo! Forçando restart do serviço...")
            os._exit(1)  # Exit code 1 faz o Render reiniciar automaticamente
        
        print(f"✅ Health check OK - {time.strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()
