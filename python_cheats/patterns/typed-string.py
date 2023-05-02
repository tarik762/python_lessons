from typing import TypedDict
from pydantic import BaseModel


class Movie(TypedDict):
    name: str
    year: int


# ex1
movie: Movie = {'name': 'Blade Runner',
                'year': '1982'}

print(movie)

# ex2


def record_movie(movie: Movie) -> None: ...


record_movie({'name': 'Blade Runner', 'year': 1982})

# ex 3
movie: Movie
...
...
...
movie = {'name': 'Blade Runner', 'year': 1982}
print(movie)
movie['dgjvsiojvno'] = 'redley'
print(movie)
