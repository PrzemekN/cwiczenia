users = [
    {"id": 0, "name": "Hero"}, {"id": 1, "name": "Dunn"}, {"id": 2, "name": "Sue"}, {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"}, {"id": 5, "name": "Clive"}, {"id": 6, "name": "Hicks"}, {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"}, {"id": 9, "name": "Klein"},
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
# przeglądanie takich danych jest czasochlonne, dlatego zrobimy z tego slownik gdzie
# kluczami beda id uzytkownikow a wartosciami lista id uzytkowników z ktorymi sie przyjazdni. np {0:[1,2], 1:[0,2,3],..}
# Aby to zrobic musimy raz przejsc powyzsze struktury danych users i frendship_pairs.
# zauwaz ze warto miec pewnosc (tutaj taka pewnosc istnieje) zeby id bylo niepowtarzalne w ramach listy users.

# inicjalizowanie slownika pustymi listami dla kazdego user id:
friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    print(i, " ", j)

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)


# funkcja pobiera slownik z listy users, zwraca dlugosc listy ze słownika friendships
def number_of_friends(user: dict) -> int:
    user_id = user["id"]
    f_ids = friendships[user_id]
    return len(f_ids)


# funkcja zwracająca dl listy ze slownika friendship
def number_of_friends1(key: int) -> int:
    return len(friendships[key])


# lista uzytkownikow z liczbą przyjacioł [(0,2), (1,3)]
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_by_id1 = [(k, number_of_friends1(k)) for k in friendships]


# posortujmy num_firends_by_id wedlug number_of_friends
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)
