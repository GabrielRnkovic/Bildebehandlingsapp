from PIL import Image, ImageFilter, ImageDraw

def load_image(file_path):
    return Image.open(file_path)

def save_image(image, output_path):
    image.save(output_path)

def apply_instagram_filter(image):
    return image.filter(ImageFilter.SMOOTH)

def apply_black_and_white_art_filter(image):
    return image.convert("L")

def rotate_image(image, angle):
    return image.rotate(angle)

def resize_image(image, width):
    original_width, original_height = image.size
    ratio = width / original_width
    new_height = int(original_height * ratio)
    return image.resize((width, new_height))

def apply_polaroid_frame(image):
    width, height = image.size

    # Opprett en hvit ramme med avrundede hjørner
    frame_size = 20
    frame = Image.new("RGB", (width + 2 * frame_size, height + 2 * frame_size), "white")
    draw = ImageDraw.Draw(frame)
    draw.rectangle([0, 0, width + 2 * frame_size, height + 2 * frame_size], outline=None, fill="white", width=0)
    draw.rectangle([frame_size, frame_size, width + frame_size, height + frame_size], outline="black", width=3)

    # Plasser bildet inni rammen
    frame.paste(image, (frame_size, frame_size))

    return frame

def main():
    print("Welcome to Image Manipulation CLI App!")
    input_image_path = input("Enter the path of the image you want to process: ")

    image = load_image(input_image_path)

    while True:
        print("\nChoose an operation:")
        print("1. Apply Instagram Filter")
        print("2. Apply Black & White Art Filter")
        print("3. Rotate Image")
        print("4. Resize Image")
        print("5. Apply Polaroid Frame")
        print("6. Exit")

        choice = input("Enter the operation number: ")

        if choice == '1':
            image = apply_instagram_filter(image)
        elif choice == '2':
            image = apply_black_and_white_art_filter(image)
        elif choice == '3':
            angle = int(input("Enter rotation angle (90, -90, or 180): "))
            image = rotate_image(image, angle)
        elif choice == '4':
            width = int(input("Enter the desired width: "))
            image = resize_image(image, width)
        elif choice == '5':
            image = apply_polaroid_frame(image)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid operation.")

    print("Saving the final image...")
    save_image(image, "output_image.jpg")
    print("Image saved successfully!")

if __name__ == "__main__":
    main()
