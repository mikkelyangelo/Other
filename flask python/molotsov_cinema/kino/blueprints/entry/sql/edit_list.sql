SELECT session_id,date_time,session_hall, country,film.year,director,studio
FROM session join film
on session_film = film_id