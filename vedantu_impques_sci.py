#run this in one code space on colab
import requests
from PIL import Image
from io import BytesIO

# List of image URLs
image_urls = [
    f"https://www.vedantu.com/content-images/cbse/important-questions-class-9-science-chapter-12/{i}.webp" #you can find by inspecting the page
    for i in range(1, 21) #change upper limit according to the number of pages
]

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
    output_path = "Class9_Science_Important_Questions.pdf" #change accordingly
    images[0].save(output_path, save_all=True, append_images=images[1:])
    print(f"✅ PDF saved as: {output_path}")
else:
    print("No images downloaded. Check the URLs or your internet connection.")


#run this next
from google.colab import files
files.download("Class9_Science_Important_Questions.pdf")
