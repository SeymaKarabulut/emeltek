import requests
from PIL import Image, ImageDraw

# Roboflow model tahmin endpoint'i için URL oluşturun
api_key = "CgDvA5myuyvQv6MCfOjy"  # Buraya Roboflow API anahtarınızı ekleyin
model_url = "https://detect.roboflow.com/gozluk2egitim/1"  # Proje adı ve versiyonu ekleyin

# Görüntü dosyanız
image_path = "dene.jpg"

# İstek parametrelerini belirleyin
params = {
    "api_key": api_key,
    "confidence": 0.4,  # Confidence değeri
    "overlap": 0.3      # Overlap değeri (IOU)
}

# Görüntüyü okuma ve istek gönderme
with open(image_path, "rb") as image_file:
    response = requests.post(model_url, params=params, files={"file": image_file})

# Yanıtı kontrol edin
predictions = response.json()

# Orijinal görüntüyü açın
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# Tahmin kutularını çizin
for prediction in predictions['predictions']:
    x, y, width, height = prediction['x'], prediction['y'], prediction['width'], prediction['height']
    class_name = prediction['class']

    # Koordinatları hesaplayın
    left = x - width / 2
    top = y - height / 2
    right = x + width / 2
    bottom = y + height / 2

    # Dikdörtgen çizin ve sınıf adını yazdırın
    draw.rectangle([left, top, right, bottom], outline="red", width=3)
    draw.text((left, top), class_name, fill="red")

# Tahmin edilen görüntüyü kaydedin
output_image_path = "prediction.jpg"
image.save(output_image_path)

print(f"Prediction image saved as {output_image_path}")


