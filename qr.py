
#Simple qr code 

import qrcode as qr
#make method creates the qr
img=qr.make("https://studio.youtube.com/channel/UCbCIC5zVlg6pHaOg5j9XiBQ/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D")
# save method saves the qr
img.save("chetan_youtube.png")
