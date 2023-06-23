import View
import Model
import Text


def start():
    while True:
        select = View.menu()
        match select:
            case 1:
                if Model.open_file():
                    View.print_message(Text.load_succesful)
                else:
                    View.print_message(Text.error_load)
            case 2:
                if Model.save_file():
                    View.print_message(Text.save_succesful)
                else:
                    View.print_message(Text.error_save)
            case 3:
                View.show_contacts(Model.phone_book, Text.empty_book)
            case 4:
                new = View.add_contact()
                Model.add_contact(new)
                View.print_message(Text.add_succesful(new.get('name')))
            case 5:
                word = View.search_word()
                result = Model.search(word)
                View.show_contacts(result, Text.empty_search(word))
            case 6:
                word = View.search_word()
                result = Model.search(word)

                if len(result)>0:
                    Model.change(result, View.add_contact())
                else:
                    View.print_message(Text.print_errors)
            case 7:
                word = View.search_word()
                result = Model.search(word)
                Model.delete(result)
                View.show_del(result, Text.del_mess(word))

            case 8:
                View.print_message()
                break
