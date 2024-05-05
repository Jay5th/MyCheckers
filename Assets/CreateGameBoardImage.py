from PIL import Image, ImageTk


def create_game_board_image(size):
    assets_path = "C:\\Users\\japhe\\OneDrive\\Desktop\\Program Projects\\GitHubCheckers\\Assets\\"
    image_path = assets_path + "GameBoard.png"
    image = Image.open(image_path)
    image = image.resize(size)
    return ImageTk.PhotoImage(image)
