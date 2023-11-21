from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image

def select_image():
	global panelA, name_label, size_label, resolution_label, depth_label, compression_label

	path = filedialog.askopenfilename(filetypes=(("PNG", "*.png"), ("JPG", "*.jpg"), ("GIF", "*.gif"), ("TIF", "*.tif"), ("BMP", "*.bmp"), ("PCX", "*.pcx")))

	if len(path) > 0:
		image = Image.open(path)

		name = path.split("/")[-1]
		width, height = image.size
		resolution = image.info.get("dpi")
		depth = len(image.mode) * 8
		compression = image.info.get("compression")

		name_text = "Name: " + str(name)
		size_text = "Size: " + str(width) + "x" + str(height) + "p"
		if resolution:
			resolution_text = "Resolution: " + str(resolution[0]) + "dpi"
		else:
			resolution_text = "Resolution not set."
		depth_text = "Depth: " + str(depth) + " bit"
		if compression:
			compression_text = "Compression: " + str(compression)
		else:
			compression_text = "Compression not set."


		height = (height / width) * 400
		width = 400
		image = ImageTk.PhotoImage(image.resize((int(width), int(height))))

		if panelA is None:
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)

			name_label = Label(window, text=name_text)
			name_label.pack(side="top", padx=10, pady=5)

			size_label = Label(window, text=size_text)
			size_label.pack(side="top", padx=10, pady=5)

			resolution_label = Label(window, text=resolution_text)
			resolution_label.pack(side="top", padx=10, pady=5)

			depth_label = Label(window, text=depth_text)
			depth_label.pack(side="top", padx=10, pady=5)

			compression_label = Label(window, text=compression_text)
			compression_label.pack(side="top", padx=10, pady=5)
		else:
			panelA.configure(image=image)
			name_label.configure(text=name_text)
			size_label.configure(text=size_text)
			resolution_label.configure(text=resolution_text)
			depth_label.configure(text=depth_text)
			compression_label.configure(text=compression_text)

			panelA.image = image
			name_label.text = name_text
			size_label.text = size_text
			resolution_label.text = resolution_text
			depth_label.text = depth_text
			compression_label.text = compression_text

window = Tk()
panelA = None
panelB = None
window.title("Images")
btn = Button(window, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
window.mainloop()