import model
import view


def Start():
    phoneBook = view.CreatePhoneList()
    model.StartProgram(phoneBook)
