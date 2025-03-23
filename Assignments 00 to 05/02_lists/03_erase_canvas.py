import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    eraser_coords = canvas.coords(eraser)
    overlapping = canvas.find_overlapping(*eraser_coords)
    for item in overlapping:
        if item != eraser:
            canvas.itemconfig(item, fill="white")

def move_eraser(event, canvas, eraser):
    canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
    erase_objects(canvas, eraser)

def main():
    root = tk.Tk()
    root.title("Canvas Eraser")
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    # Draw grid
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

    # Create eraser (pink rectangle)
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

    # Bind mouse movement
    canvas.bind("<Motion>", lambda e: move_eraser(e, canvas, eraser))

    root.mainloop()

if __name__ == '__main__':
    main()
