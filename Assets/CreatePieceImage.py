from PIL import Image, ImageTk


def create_piece_image(piece_name: str, piece_radius: int):
    assets_path = "Assets\\"
    image_path = assets_path + f"{piece_name}.png"
    image = Image.open(image_path)
    image = image.resize((2 * piece_radius, 2 * piece_radius))
    return ImageTk.PhotoImage(image)
