import tkinter as tk
from PIL import Image, ImageTk

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("Canvas")
        self._canvas = tk.Canvas(self.root, width=width, height=height)
        self._canvas.pack()
        
        self._images = {}  # keep references to images to avoid GC
        self._hidden = set()
        
        # Store clicks and keys for helper methods
        self._last_click = None
        self._new_clicks = []
        self._new_keys = []
        
        self._canvas.bind("<Button-1>", self._on_click)
        self._canvas.bind("<Key>", self._on_key_press)
        
        self._canvas.focus_set()
        
    # --- Create shapes ---
    
    def create_rectangle(self, left_x, top_y, right_x, bottom_y, color=None, outline=None):
        return self._canvas.create_rectangle(
            left_x, top_y, right_x, bottom_y,
            fill=color if color else "",
            outline=outline if outline else "black"
        )
        
    def create_oval(self, left_x, top_y, right_x, bottom_y, color=None, outline=None):
        return self._canvas.create_oval(
            left_x, top_y, right_x, bottom_y,
            fill=color if color else "",
            outline=outline if outline else "black"
        )
        
    def create_line(self, x1, y1, x2, y2, color=None):
        return self._canvas.create_line(
            x1, y1, x2, y2,
            fill=color if color else "black"
        )
        
    def create_text(self, x, y, text, font=None, font_size=None, color=None, anchor=None):
        font_setting = (font, int(font_size)) if font and font_size else None
        return self._canvas.create_text(
            x, y,
            text=text,
            font=font_setting,
            fill=color if color else "black",
            anchor=anchor if anchor else "nw"
        )
    
    def create_image(self, left_x, top_y, filename):
        image = Image.open(filename)
        photo = ImageTk.PhotoImage(image)
        img_id = self._canvas.create_image(left_x, top_y, image=photo, anchor="nw")
        self._images[img_id] = photo  # keep reference
        return img_id
    
    def create_image_with_size(self, left_x, top_y, width, height, filename):
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        img_id = self._canvas.create_image(left_x, top_y, image=photo, anchor="nw")
        self._images[img_id] = photo
        return img_id
    
    def create_polygon(self, *coordinates, color=None, outline=None):
        return self._canvas.create_polygon(
            *coordinates,
            fill=color if color else "",
            outline=outline if outline else "black"
        )
    
    # --- Modify shapes ---
    
    def move(self, object_id, dx, dy):
        self._canvas.move(object_id, dx, dy)
    
    def moveto(self, object_id, new_x, new_y):
        coords = self._canvas.coords(object_id)
        if coords:
            current_x = coords[0]
            current_y = coords[1]
            dx = new_x - current_x
            dy = new_y - current_y
            self.move(object_id, dx, dy)
    
    def delete(self, object_id):
        if object_id in self._images:
            del self._images[object_id]
        self._canvas.delete(object_id)
    
    def set_hidden(self, object_id, is_hidden):
        if is_hidden:
            self._canvas.itemconfigure(object_id, state='hidden')
            self._hidden.add(object_id)
        else:
            self._canvas.itemconfigure(object_id, state='normal')
            self._hidden.discard(object_id)
    
    def change_text(self, object_id, new_text):
        self._canvas.itemconfigure(object_id, text=new_text)
    
    # --- Canvas helpers ---
    
    def get_mouse_x(self):
        return self._canvas.winfo_pointerx() - self._canvas.winfo_rootx()
    
    def get_mouse_y(self):
        return self._canvas.winfo_pointery() - self._canvas.winfo_rooty()
    
    def get_last_click(self):
        result = self._last_click
        self._last_click = None
        return result
    
    def get_new_mouse_clicks(self):
        clicks = self._new_clicks.copy()
        self._new_clicks.clear()
        return clicks
    
    def get_last_key_press(self):
        if self._new_keys:
            return self._new_keys[-1]
        return None
    
    def get_new_key_presses(self):
        keys = self._new_keys.copy()
        self._new_keys.clear()
        return keys
    
    def coords(self, object_id):
        return self._canvas.coords(object_id)
    
    def get_left_x(self, object_id):
        coords = self._canvas.coords(object_id)
        if coords:
            return min(coords[::2])
        return None
    
    def get_top_y(self, object_id):
        coords = self._canvas.coords(object_id)
        if coords:
            return min(coords[1::2])
        return None
    
    def get_object_width(self, object_id):
        coords = self._canvas.coords(object_id)
        if not coords:
            return 0
        xs = coords[::2]
        return max(xs) - min(xs)
    
    def get_object_height(self, object_id):
        coords = self._canvas.coords(object_id)
        if not coords:
            return 0
        ys = coords[1::2]
        return max(ys) - min(ys)
    
    def set_color(self, object_id, color):
        self._canvas.itemconfigure(object_id, fill=color)
    
    def set_outline_color(self, object_id, color):
        self._canvas.itemconfigure(object_id, outline=color)
    
    def clear(self):
        self._canvas.delete("all")
        self._images.clear()
        self._hidden.clear()
    
    def wait_for_click(self):
        self._last_click = None
        while self._last_click is None:
            self._canvas.update()
        return self._last_click
    
    # --- Internal event handlers ---
    
    def _on_click(self, event):
        click = {'x': event.x, 'y': event.y}
        self._last_click = click
        self._new_clicks.append(click)
    
    def _on_key_press(self, event):
        self._new_keys.append(event.keysym)
    
    # --- To run the tkinter main loop ---
    
    def run(self):
        self.root.mainloop()
