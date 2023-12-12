from PIL import Image, ImageTk, ImageEnhance
import tkinter as tk
from tkinter import messagebox  # Import messagebox separately
import requests
from io import BytesIO

class ColorblindTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorblind Test")

        # List of image URLs and their corresponding numbers
        self.image_data = [
            {"url": "https://cdn-beaai.nitrocdn.com/DsHNrqyidSdrnEUwxpnDFmLjguAlTfrt/assets/images/optimized/rev-3b37200/colormax.org/wp-content/uploads/2015/08/colorblind-test-image6.jpg", "number": 73},
            {"url": "https://cdn-beaai.nitrocdn.com/DsHNrqyidSdrnEUwxpnDFmLjguAlTfrt/assets/images/optimized/rev-3b37200/colormax.org/wp-content/uploads/2015/08/colorblind-test-image1.jpg", "number": 7},
            {"url": "https://cdn-beaai.nitrocdn.com/DsHNrqyidSdrnEUwxpnDFmLjguAlTfrt/assets/images/optimized/rev-3b37200/colormax.org/wp-content/uploads/2015/08/colorblind-test-image10.jpg", "number": 12},
            {"url": "https://cdn-beaai.nitrocdn.com/DsHNrqyidSdrnEUwxpnDFmLjguAlTfrt/assets/images/optimized/rev-3b37200/colormax.org/wp-content/uploads/2015/08/colorblind-test-image11.jpg", "number": 29},
            {"url": "https://cdn-beaai.nitrocdn.com/DsHNrqyidSdrnEUwxpnDFmLjguAlTfrt/assets/images/optimized/rev-3b37200/colormax.org/wp-content/uploads/2015/08/colorblind-test-image3.jpg", "number": 26},
        ]

        self.current_image_index = 0

        # Create buttons to navigate through images
        self.prev_image_button = tk.Button(root, text="Previous Image", command=self.prev_image)
        self.prev_image_button.pack(side="left", padx=10)
        self.next_image_button = tk.Button(root, text="Next Image", command=self.next_image)
        self.next_image_button.pack(side="right", padx=10)

        # Create an entry for the user to input their guess
        self.guess_entry = tk.Entry(root, width=10)
        self.guess_entry.pack(pady=10)

        # Create a button to check the user's guess
        self.check_guess_button = tk.Button(root, text="Check Guess", command=self.check_guess)
        self.check_guess_button.pack(pady=10)

        self.load_current_image()

    def load_current_image(self):
        if self.image_data:
            image_url = self.image_data[self.current_image_index]["url"]
            self.original_image = self.load_image_from_url(image_url)

            if self.original_image:
                self.update_ui()

    def prev_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.image_data)
        self.load_current_image()

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_data)
        self.load_current_image()

    def load_image_from_url(self, url):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
            return image
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def update_ui(self):
        self.guess_entry.delete(0, tk.END)  # Clear the entry
        self.guess_entry.focus_set()  # Set focus to the entry
        self.display_image()

    def display_image(self):
        # Display the image in a label
        photo = ImageTk.PhotoImage(self.original_image)

        if hasattr(self, "image_label"):
            self.image_label.config(image=photo)
            self.image_label.image = photo
        else:
            self.image_label = tk.Label(root, image=photo)
            self.image_label.pack()

    def check_guess(self):
        try:
            user_guess = int(self.guess_entry.get())
            correct_number = self.image_data[self.current_image_index]["number"]

            if user_guess == correct_number:
                messagebox.showinfo("Guess Result", "Correct!")
            else:
                messagebox.showinfo("Guess Result", f"Incorrect. The correct number is {correct_number}")

            self.guess_entry.delete(0, tk.END)
            self.load_current_image()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorblindTestApp(root)
    root.mainloop()
