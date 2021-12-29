import controller as con
import sys

c = con.Controller()

try:
    command = sys.argv[1]
except IndexError:
    c.v.no_command()
else:
    if command == 'print_table':
        try:
            name = sys.argv[2]
        except IndexError:
            c.v.argument_error()
        else:
            c.print(name)

    elif command == 'delete_record':
        try:
            args = {"name": sys.argv[2], "key": sys.argv[3]}
        except IndexError:
            c.v.argument_error()
        else:
            c.delete(args["name"], args["key"])

    elif command == 'update_record':
        try:
            args = {"table": sys.argv[2], "key": sys.argv[3]}
            if args["table"] == 'Cinema':
                args["name"], args["id_movie"] = sys.argv[4], sys.argv[5]
            elif args["table"] == 'Movie':
                args["title"], args["description"] = sys.argv[4], sys.argv[5]
            elif args["table"] == 'Showtime':
                args["timing"], args["id_movie"] = sys.argv[4], sys.argv[5]
            elif args["table"] == 'Ticket':
                args["name"], args["date"], args["price"], args["id_showtime"], args["row"], args["place"] = \
                    sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9]
            else:
                c.v.wrong_table()
        except IndexError:
            c.v.argument_error()
        else:
            if args["table"] == 'Cinema':
                c.update_cinema(args["key"], args["name"], args["id_movie"])
            elif args["table"] == 'Movie':
                c.update_movie(args["key"], args["title"], args["description"])
            elif args["table"] == 'Showtime':
                c.update_showtime(args["key"], args["timing"], args["id_movie"])
            elif args["table"] == 'Ticket':
                c.update_ticket(args["key"], args["name"], args["date"], args["price"], args["id_showtime"],
                                args["row"], args["place"])

    elif command == 'insert_record':
        try:
            args = {"table": sys.argv[2], "key": sys.argv[3]}
            if args["table"] == 'Cinema':
                args["name"], args["id_movie"] = sys.argv[4], sys.argv[5]
            elif args["table"] == 'Movie':
                args["title"], args["description"] = sys.argv[4], sys.argv[5]
            elif args["table"] == 'Showtime':
                args["timing"], args["id_movie"] = sys.argv[4], sys.argv[5]
            elif args["table"] == 'Ticket':
                args["name"], args["date"], args["price"], args["id_showtime"], args["row"], args["place"] = \
                    sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9]
            else:
                c.v.wrong_table()
        except IndexError:
            c.v.argument_error()
        else:
            if args["table"] == 'Cinema':
                c.insert_cinema(args["key"], args["name"], args["id_movie"])
            elif args["table"] == 'Movie':
                c.insert_movie(args["key"], args["title"], args["description"])
            elif args["table"] == 'Showtime':
                c.insert_showtime(args["key"], args["timing"], args["id_movie"])
            elif args["table"] == 'Ticket':
                c.insert_ticket(args["key"], args["name"], args["date"], args["price"], args["id_showtime"],
                                args["row"], args["place"])

    elif command == 'test':
        print(not c.m.find_product(13))
    elif command == 'generate_randomly':
        try:
            args = {"name": sys.argv[2], "n": int(sys.argv[3])}
        except (IndexError, Exception):
            print(Exception, IndexError)
        else:
            c.generate(args["name"], args["n"])

    elif command == 'search_records':
        while True:
            search_num = c.v.get_search_num()
            try:
                search_num = int(search_num)
            except ValueError:
                c.v.invalid_search_num()
            else:
                if search_num in [2, 3, 4]:
                    break
                else:
                    c.v.invalid_search_num()
        if search_num == 2:
            c.search_two()
        elif search_num == 3:
            c.search_three()
        elif search_num == 4:
            c.search_all()

    elif command == 'help':
        c.v.print_help()
    else:
        c.v.wrong_command()