import requests
from PIL import Image
from io import BytesIO

status_code = 201
# burada hangi değeri verirsek o değere ait resmi kayıt eder


url = f"https://http.cat/{status_code}"

try: 
    response = requests.get(url)
    response.raise_for_status()  
    
    img_data = response.content
    
    
    image = Image.open(BytesIO(img_data))
    image.show()  
    image.save(f"http_cat_{status_code}.jpg")  

    print(f"HTTP {status_code} resim alındı ve kayıt edildi")

except requests.exceptions.RequestException as e:
    print(f"yanlış bir değer girdiniz {e}")
