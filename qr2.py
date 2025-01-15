import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=
                 qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)
qr.add_data("https://studio.youtube.com/channel/UCbCIC5zVlg6pHaOg5j9XiBQ/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D")
qr.make(fit=True)
img=qr.make_image(fill_color="red",black_color="white")
img.save("web_page.png")