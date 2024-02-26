from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize a 5x5 grid with all cells initially not lit
grid = [[False] * 5 for _ in range(5)]


@app.route("/")
def index():
    grid_text = [[""] * 5 for _ in range(5)]
    with open("grid-text.txt", encoding="utf-8") as f:
        for line_number, line in enumerate(f.readlines()):
            if line_number >= 25:
                break
            col = line_number % 5
            row = line_number // 5
            grid_text[row][col] = line.strip()
    return render_template("index.html", grid=grid, grid_text=grid_text)


@socketio.on("toggle_cell")
def toggle_cell(data):
    row = data["row"]
    col = data["col"]
    grid[row][col] = not grid[row][col]
    emit("update_grid", {"row": row, "col": col, "lit": grid[row][col]}, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=22708, debug=True)
