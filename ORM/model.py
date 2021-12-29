import datetime
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, select, and_
from sqlalchemy.orm import relationship
from db import Orders, Session, engine


def recreate_database():
    Orders.metadata.drop_all(engine)
    Orders.metadata.create_all(engine)


class Cinema(Orders):
    __tablename__ = 'Cinema'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    id_movie = Column(Integer, ForeignKey('Movie.id'))
    movies = relationship("Movie")

    def __init__(self, key, name, id_movie):
        self.id = key
        self.name = name
        self.id_movie = id_movie

    def __repr__(self):
        return "{:>10}{:>15}{:>10}" \
            .format(self.id, self.name, self.id_movie)


class Movie(Orders):
    __tablename__ = 'Movie'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    def __init__(self, key, title, description):
        self.id = key
        self.title = title
        self.description = description

    def __repr__(self):
        return "{:>10}{:>15}{:>50}" \
            .format(self.id, self.title, self.description)


class Showtime(Orders):
    __tablename__ = 'Showtime'
    id = Column(Integer, primary_key=True)
    timing = Column(Float)
    id_movie = Column(Integer, ForeignKey('Movie.id'))
    movies = relationship("Movie")

    def __init__(self, key, timing, id_movie):
        self.id = key
        self.timing = timing
        self.id_movie = id_movie

    def __repr__(self):
        return "{:>10}{:>15}{:>10}" \
            .format(self.id, self.timing, self.id_movie)


class Ticket(Orders):
    __tablename__ = 'Ticket'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)
    price = Column(Integer)
    id_showtime = Column(Integer, ForeignKey('Showtime.id'))
    showtimes = relationship("Showtime")
    row = Column(Integer)
    place = Column(Integer)

    def __init__(self, key, name, date, price, id_showtime, row, place):
        self.id = key
        self.name = name
        self.date = date
        self.price = price
        self.id_showtime = id_showtime
        self.row = row
        self.place = place

    def __repr__(self):
        return "{:>10}{:>15}{:>15}{:>10}{:>10}{:>10}{:>10}" \
            .format(self.id, self.name, self.date, self.price, self.id_showtime, self.row, self.place)


class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    def find_pk_cinema(self, key_value: int):
        return self.session.query(Cinema).filter_by(id=key_value).first()

    def find_fk_cinema(self, key_value: int):
        return self.session.query(Cinema).filter_by(id_movie=key_value).first()

    def find_pk_movie(self, key_value: int):
        return self.session.query(Movie).filter_by(id=key_value).first()

    def find_pk_showtime(self, key_value: int):
        return self.session.query(Showtime).filter_by(id=key_value).first()

    def find_fk_showtime(self, key_value: int):
        return self.session.query(Showtime).filter_by(id_movie=key_value).first()

    def find_pk_ticket(self, key_value: int):
        return self.session.query(Ticket).filter_by(id=key_value).first()

    def find_fk_ticket(self, key_value: int):
        return self.session.query(Ticket).filter_by(id_showtime=key_value).first()

    def print_cinema(self):
        return self.session.query(Cinema).order_by(Cinema.id.asc()).all()

    def print_movie(self):
        return self.session.query(Movie).order_by(Movie.id_order.asc()).all()

    def print_showtime(self):
        return self.session.query(Showtime).order_by(Showtime.id_catalog.asc()).all()

    def print_ticket(self):
        return self.session.query(Ticket).order_by(Ticket.id_shop.asc()).all()

    def delete_data_cinema(self, key) -> None:
        self.session.query(Cinema).filter_by(id=key).delete()
        self.session.commit()

    def delete_data_movie(self, key) -> None:
        self.session.query(Movie).filter_by(id=key).delete()
        self.session.commit()

    def delete_data_showtime(self, key) -> None:
        self.session.query(Showtime).filter_by(id=key).delete()
        self.session.commit()

    def delete_data_ticket(self, key) -> None:
        self.session.query(Ticket).filter_by(id=key).delete()
        self.session.commit()

    def update_data_cinema(self, key: int, name: str, id_movie: int) -> None:
        self.session.query(Cinema).filter_by(id=key) \
            .update({Cinema.name: name, Cinema.id_movie: id_movie})
        self.session.commit()

    def update_data_movie(self, key: int, title: str, description: str) -> None:
        self.session.query(Movie).filter_by(id=key) \
            .update({Movie.title: title, Movie.description: description})
        self.session.commit()

    def update_data_showtime(self, key: int, timing: float, id_movie: int) -> None:
        self.session.query(Showtime).filter_by(id=key) \
            .update({Showtime.timing: timing, Showtime.id_movie: id_movie})
        self.session.commit()

    def update_data_ticket(self, key: int, name: str, date: str, price: int, id_showtime: int,
                           row: int, place: int) -> None:
        self.session.query(Ticket).filter_by(id=key) \
            .update({Ticket.name: name, Ticket.date: date, Ticket.price: price, Ticket.id_showtime: id_showtime,
                     Ticket.row: row, Ticket.place: place})
        self.session.commit()

    def insert_data_cinema(self, key: int, name: str, id_movie: int) -> None:
        cinema = Cinema(key=key, name=name, id_movie=id_movie)
        self.session.add(cinema)
        self.session.commit()

    def insert_data_movie(self, key: int, title: str, description: str) -> None:
        movie = Movie(key=key, title=title, description=description)
        self.session.add(movie)
        self.session.commit()

    def insert_data_showtime(self, key: int, timing: float, id_movie: int) -> None:
        showtime = Showtime(key=key, timing=timing, id_movie=id_movie)
        self.session.add(showtime)
        self.session.commit()

    def insert_data_ticket(self, key: int, name: str, date: str, price: int, id_showtime: int,
                           row: int, place: int) -> None:
        ticket = Ticket(key=key, name=name, date=date, price=price, id_showtime=id_showtime, row=row, place=place)
        self.session.add(ticket)
        self.session.commit()

    def cinema_data_generator(self, times: int) -> None:
        for i in range(times):
            self.connection.execute("insert into public.\"Cinema\""
                         "select (SELECT MAX(id)+1 FROM public.\"Cinema\"), "
                         "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) \
                         FROM generate_series(1, FLOOR(RANDOM()*(10-4)+4):: integer)), ''), "
                         "(SELECT id FROM public.\"Movie\" LIMIT 1 OFFSET "
                         "(round(random() *((SELECT COUNT(id) FROM public.\"Movie\")-1))));")

    def movie_data_generator(self, times: int) -> None:
        for i in range(times):
            self.connection.execute("insert into public.\"Movie\" "
                         "select (SELECT (MAX(id)+1) FROM public.\"Movie\"), "
                         "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) \
                         FROM generate_series(1, FLOOR(RANDOM()*(10-4)+4):: integer)), ''), "
                         "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) \
                         FROM generate_series(1, FLOOR(RANDOM()*(10-4)+4):: integer)), ''); ")

    def showtime_data_generator(self, times: int) -> None:
        for i in range(times):
            self.connection.execute("insert into public.\"Showtime\" "
                         "select (SELECT MAX(id)+1 FROM public.\"Showtime\"), "
                         "FLOOR(RANDOM()*(100000-1)+1),"
                         "(SELECT id FROM public.\"Movie\" LIMIT 1 OFFSET "
                         "(round(random() *((SELECT COUNT(id) FROM public.\"Movie\")-1))));")

    def ticket_data_generator(self, times: int) -> None:
        for i in range(times):
            self.connection.execute("insert into public.\"Ticket\" "
                         "select (SELECT MAX(id)+1 FROM public.\"Ticket\"), "
                         "array_to_string(ARRAY(SELECT chr((97 + round(random() * 25)) :: integer) \
                         FROM generate_series(1, FLOOR(RANDOM()*(10-4)+4):: integer)), ''), "
                         "array_to_string(ARRAY(SELECT chr((150 + round(random() * 25)) :: integer) \
                         FROM generate_series(1, FLOOR(RANDOM()*(10-4)+4):: integer)), ''), "
                         "FLOOR(RANDOM()*(100000-1)+1),"
                         "(SELECT id FROM public.\"Showtime\" LIMIT 1 OFFSET "
                         "(round(random() *((SELECT COUNT(id) FROM public.\"Showtime\")-1)))), "
                         "FLOOR(RANDOM()*(100000-1)+1),"
                         "FLOOR(RANDOM()*(100000-1)+1);")

    def search_data_two_tables(self):
        return self.session.query(Showtime) \
            .join(Ticket) \
            .filter(and_(
                Showtime.timing <= 19,
                Ticket.price >= 130,
                Ticket.place <= 10,
            )) \
            .all()

    def search_data_three_tables(self):
        return self.session.query(Movie) \
            .join(Showtime).join(Ticket) \
            .filter(and_(
                Movie.title.ilike('Dune'),
                Showtime.id >= 4,
                Ticket.row == 5,
            )) \
            .all()

    def search_data_all_tables(self):
        return self.session.query(Cinema) \
            .join(Movie).join(Showtime).join(Ticket) \
            .filter(and_(
                Cinema.id <= 6,
                Movie.title.ilike('The Eternals'),
                Showtime.timing >= 10,
                Ticket.date.ilike('17.11'),
            )) \
            .all()
