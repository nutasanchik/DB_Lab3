from psycopg2 import Error
import model
import view
import datetime


class Controller:
    def __init__(self):
        self.v = view.View()
        self.m = model.Model()

    def print(self, table_name):
        t_name = self.v.valid.check_table_name(table_name)
        if t_name:
            if t_name == 'Cinema':
                self.v.print_cinema(self.m.print_cinema())
            elif t_name == 'Movie':
                self.v.print_movie(self.m.print_movie())
            elif t_name == 'Showtime':
                self.v.print_showtime(self.m.print_showtime())
            elif t_name == 'Ticket':
                self.v.print_ticket(self.m.print_ticket())

    def delete(self, table_name, value):
        t_name = self.v.valid.check_table_name(table_name)
        if t_name:
            k_val = self.v.valid.check_pk(value)
            count = 0
            if t_name == 'Cinema' and k_val:
                count = self.m.find_pk_cinema(k_val)
            elif t_name == 'Movie' and k_val:
                count = self.m.find_pk_movie(k_val)
            elif t_name == 'Showtime' and k_val:
                count = self.m.find_pk_showtime(k_val)
            elif t_name == 'Ticket' and k_val:
                count = self.m.find_pk_ticket(k_val)

            if count:
                if t_name == 'Movie':
                    count_c = self.m.find_fk_cinema(k_val)
                    if count_c:
                        self.v.cannot_delete()
                    else:
                        try:
                            self.m.delete_data_movie(k_val)
                        except (Exception, Error) as _ex:
                            self.v.sql_error(_ex)

                elif t_name == 'Movie':
                    count_s = self.m.find_fk_showtime(k_val)
                    if count_s:
                        self.v.cannot_delete()
                    else:
                        try:
                            self.m.delete_data_movie(k_val)
                        except (Exception, Error) as _ex:
                            self.v.sql_error(_ex)

                elif t_name == 'Showtime':
                    count_t = self.m.find_fk_ticket(k_val)
                    if count_t:
                        self.v.cannot_delete()
                    else:
                        try:
                            self.m.delete_data_showtime(k_val)
                        except (Exception, Error) as _ex:
                            self.v.sql_error(_ex)
                else:
                    try:
                        self.m.delete_data_cinema(k_val)
                    except (Exception, Error) as _ex:
                        self.v.sql_error(_ex)
            else:
                self.v.deletion_error()

    def update_cinema(self, key: str, name: str, id_movie: int):
        if self.v.valid.check_possible_keys('Cinema', 'id', key):
            count_c = self.m.find_pk_cinema(int(key))
            c_val = self.v.valid.check_pk(key)
        if self.v.valid.check_possible_keys('Movie', 'id', id_movie):
            count_m = self.m.find_pk_movie(int(id_movie))
            m_val = self.v.valid.check_pk(id_movie)

        if c_val and name and m_val:
            try:
                self.m.update_data_cinema(c_val, name, m_val)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.updation_error()

    def update_movie(self, key: str, title: str, description: str):
        if self.v.valid.check_possible_keys('Movie', 'id', key):
            count_m = self.m.find_pk_movie(int(key))
            m_val = self.v.valid.check_pk(key)

        if m_val and title and description:
            try:
                self.m.update_data_movie(m_val, title, description)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.updation_error()

    def update_showtime(self, key: str, timing: int, id_movie: int):
        if self.v.valid.check_possible_keys('Showtime', 'id', key):
            count_s = self.m.find_pk_showtime(int(key))
            s_val = self.v.valid.check_pk(key)
        if self.v.valid.check_possible_keys('Movie', 'id', id_movie):
            count_m = self.m.find_pk_movie(int(id_movie))
            m_val = self.v.valid.check_pk(id_movie)

        if s_val and timing and m_val:
            try:
                self.m.update_data_showtime(s_val, timing, m_val)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.updation_error()

    def update_ticket(self, key: str, name: str, date: str, price: int, id_showtime: int, row: int, place: int):
        if self.v.valid.check_possible_keys('Ticket', 'id', key):
            count_t = self.m.find_pk_ticket(int(key))
            t_val = self.v.valid.check_pk(key)
        if self.v.valid.check_possible_keys('Showtime', 'id', id_showtime):
            count_s = self.m.find_pk_showtime(int(id_showtime))
            s_val = self.v.valid.check_pk(id_showtime)

        if key and name and date and price and s_val and row and place:
            try:
                self.m.update_data_ticket(int(key), name, date, price, s_val, row, place)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.updation_error()

    def insert_cinema(self, key: str, name: str, id_movie: int):
        if self.v.valid.check_possible_keys('Cinema', 'id', key):
            count_c = self.m.find_pk_cinema(int(key))
            c_val = self.v.valid.check_pk(key)
        if self.v.valid.check_possible_keys('Movie', 'id', id_movie):
            count_m = self.m.find_pk_movie(int(id_movie))
            m_val = self.v.valid.check_pk(id_movie)

        if c_val and name and m_val:
            try:
                self.m.insert_data_cinema(c_val, name, m_val)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.insertion_error()

    def insert_movie(self, key: str, title: str, description: str):
        if self.v.valid.check_possible_keys('Movie', 'id', key):
            count_m = self.m.find_pk_movie(int(key))
            m_val = self.v.valid.check_pk(key)

        if m_val and title and description:
            try:
                self.m.insert_data_movie(m_val, title, description)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.insertion_error()

    def insert_showtime(self, key: str, timing: int, id_movie: int):
        if self.v.valid.check_possible_keys('Showtime', 'id', key):
            count_s = self.m.find_pk_showtime(int(key))
            s_val = self.v.valid.check_pk(key)
        if self.v.valid.check_possible_keys('Movie', 'id', id_movie):
            count_m = self.m.find_pk_movie(int(id_movie))
            m_val = self.v.valid.check_pk(id_movie)

        if s_val and timing and m_val:
            try:
                self.m.insert_data_showtime(s_val, timing, m_val)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.insertion_error()

    def update_ticket(self, key: str, name: str, date: str, price: int, id_showtime: int, row: int, place: int):
        if self.v.valid.check_possible_keys('Ticket', 'id', key):
            count_t = self.m.find_pk_ticket(int(key))
            t_val = self.v.valid.check_pk(key)
        if self.v.valid.check_possible_keys('Showtime', 'id', id_showtime):
            count_s = self.m.find_pk_showtime(int(id_showtime))
            s_val = self.v.valid.check_pk(id_showtime)

        if key and name and date and price and s_val and row and place:
            try:
                self.m.insert_data_ticket(int(key), name, date, price, s_val, row, place)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.insertion_error()

    def generate(self, table_name: str, n: int):
        t_name = self.v.valid.check_table_name(table_name)
        if t_name:
            if t_name == 'Cinema':
                self.m.cinema_data_generator(n)
            elif t_name == 'Movie':
                self.m.movie_data_generator(n)
            elif t_name == 'Showtime':
                self.m.showtime_data_generator(n)
            elif t_name == 'Ticket':
                self.m.ticket_data_generator(n)

    def search_two(self):
        result = self.m.search_data_two_tables()
        self.v.print_search(result)

    def search_three(self):
        result = self.m.search_data_three_tables()
        self.v.print_search(result)

    def search_all(self):
        result = self.m.search_data_all_tables()
        self.v.print_search(result)
