import socket
from urllib.parse import urlparse
import dns.resolver

print("=== URL to IP Lookup Tool ===")
url_input = input("🔗 Lütfen bir URL girin (örnek: https://youtube.com): ")

# Girişin başında http/https yoksa varsayalım ki http://
if not url_input.startswith(("http://", "https://")):
    url_input = "http://" + url_input

try:
    # URL'den hostname’i ayıkla
    parsed_url = urlparse(url_input)
    hostname = parsed_url.hostname

    print(f"\n🔍 Hostname: {hostname}")

    # socket ile IP çözümlemesi
    ip_socket = socket.gethostbyname(hostname)
    print(f"📦 socket.gethostbyname ile IP: {ip_socket}")

    # dnspython ile gelişmiş çözümleme
    print("\n🌐 DNS kayıtları (A kaydı):")
    answers = dns.resolver.resolve(hostname, "A")
    for rdata in answers:
        print(f"➡️ {rdata.to_text()}")

except Exception as e:
    print("\n[!] Hata: URL çözümlenemedi.")
    print(f"Detay: {e}")

input("\n🟢 Çıkmak için Enter tuşuna bas...")
