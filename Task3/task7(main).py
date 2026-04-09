import logic
from ui import MainWindow


def main():
    app = MainWindow(logic)
    app.run()


if __name__ == "__main__":
    main()