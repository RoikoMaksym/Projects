import requests

def demo_requests():
    # Створює HTTP-запит, не надсилаючи його в інтернет.
    request = requests.Request("GET", "https://example.com").prepare()
    print("Метод:", request.method)
    print("URL:", request.url)
