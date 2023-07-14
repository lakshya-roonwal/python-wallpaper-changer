import ctypes
import requests
import time
import quote
from PIL import Image, ImageDraw, ImageFont

def create_wall(quotation,auth,anime):
    # Create a blank image with white background
    width = 1920
    height = 1080
    background_color = (0, 0, 0)
    image = Image.new('RGB', (width, height), background_color)

    # Set the font properties
    font_size = 60
    font_color = (255, 237, 0)
    font_path = 'Montserrat-SemiBold.ttf'  # Replace with the actual path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Define the quote
    quote=quotation+"\n"+"-"+auth+"("+anime+")"
    # Calculate the text size and position
    text_width, text_height = font.getmask(quote).getbbox()[2:]
    text_x = 1920//9
    text_y = 1080//7

    # Draw the text on the image
    draw = ImageDraw.Draw(image)
    draw.text((text_x, text_y), quote, font=font, fill=font_color)

    # Save the image
    image.save('bg.jpg')


# Also not needed for now

# def download_image(url, save_path):
    # response = requests.get(url)
    # if response.status_code == 200:
    #     with open(save_path, 'wb') as file:
    #         file.write(response.content)
    #     print("Image downloaded successfully.")
    #     time.sleep(2)
    # else:
    #     print("Failed to download image.")

# Now Needed for now
# def random_image():
#     access_key = "7jNqrJPWTmJhIQAy3bE8WSx0M6UDN7MI-LttDno5LYk"
#     url = "https://api.unsplash.com/photos/random"
#     params = {
#         "client_id": access_key,
#         "query": "landscape",
#         "orientation": "landscape",
#         "featured": "true",
#         "count": 1,
#         "w": 1920,
#         "h": 1080
#     }

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         image_url = data[0]['urls']['regular']
#         print(image_url)
#         return(image_url)
#     else:
#         print("Error occurred:", response.text)

def set_wallpaper(image_path):
    # Choose the appropriate function based on the operating system
    if ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3):
        print("Wallpaper changed successfully!")
    else:
        print("Failed to change wallpaper.")

def add_newlines(text):
    words = text.split()
    words_with_newlines = [words[i:i+8] for i in range(0, len(words), 8)]
    lines = [' '.join(line) for line in words_with_newlines]
    result = '\n'.join(lines)
    return result

def get_quote():
    url = "https://kyoko.rei.my.id/api/quotes.php"

    try:
        response = requests.get(url)
        data = response.json()
        return ([data['apiResult'][0]['english'],data['apiResult'][0]['character'],data['apiResult'][0]['anime']])
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", str(e))

quotetext=get_quote();
create_wall(add_newlines(quotetext[0]),quotetext[1],quotetext[2]);

# Provide the desired file path to save the image
save_path = "L:/Lakshya/Code/python/FUN-PROJECTS\wall-changer/bg.jpg"  # Replace with the desired file path



set_wallpaper(save_path)









