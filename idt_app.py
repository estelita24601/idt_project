from controller.idt_controller import Controller
from model.idt_model import Model
from view.idt_view import View


def main():
    v = View()
    m = Model()
    c = Controller(m, v)
    
    c.start()


if __name__ == "__main__":
    main()
