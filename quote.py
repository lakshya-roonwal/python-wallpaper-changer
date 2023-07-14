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
