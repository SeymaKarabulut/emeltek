from ultralytics import YOLO

# Modeli yükle
model = YOLO('best (4).pt')

# Videoyu işleyip ekranda göster ve sonuçları kaydet
model.predict(source="video2.mp4", save=True, show=True)
