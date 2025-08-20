#run this in one code space on colab
import requests
from PIL import Image
from io import BytesIO

# Generate image URLs dynamically (01 to 16)
base_url = "https://cdn1.byjus.com/wp-content/uploads/2019/06/NCERT-Exemplar-solution-class-9-Science-Chapter-15-part-{:02d}.jpg"
image_urls = [base_url.format(i) for i in range(1, 17)]

images = []
for idx, url in enumerate(image_urls, start=1):
    print(f"Downloading page {idx}...")
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content)).convert("RGB")
        images.append(img)
    else:
        print(f"❌ Failed to download {url}")

if images:
    output_path = "Class9_Science_Exemplar_Ch15.pdf"
    images[0].save(output_path, save_all=True, append_images=images[1:])
    print(f"✅ PDF saved as: {output_path}")
else:
    print("No images downloaded. Check the URLs or your internet connection.")


#run this next
from google.colab import files
files.download("Class9_Science_Exemplar_Ch15.pdf")
