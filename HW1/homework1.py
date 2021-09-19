"""
DO NOT MODIFY ANY VARIABLE NAMES. YOU MAY COMMENT YOUR CODE IF NEEDED. 
"""

# You must fill in your Pennkey and your 8 digit Penn ID below:

pennkey = "cheng24"
penn_id = "57477468"


# ORACLE QUERIES
 
answer1 = """
select name
from movie_cast
where name like '__p_s%'
and name not like 'Sop%'
and name not like '%laud'
order by name;
"""

answer2 = """
select distinct mg.genre_name
from movie m
join movie_genre mg
on m.movie_id = mg.movie_id
and m.release_year = 2017
order by mg.genre_name;
"""

answer3 = """
select distinct mc.name
from movie m
join cast_in ci
on m.release_year = 2015
and m.title = 'Cinderella'
and m.movie_id = ci.movie_id
and ci.charac like '%(uncredited)%'
join movie_cast mc
on ci.cast_id = mc.id
order by mc.name;
"""

answer4 = """
select m.title, m.rating, count(kwd_name) as num_kw
from movie m
join movie_genre mg
on m.movie_id = mg.movie_id
and mg.genre_name = 'Adventure'
and m.rating >= 7
and m.release_year = 2001
join movie_keyword mk
on m.movie_id = mk.movie_id
group by m.title, m.rating
order by num_kw desc;
"""

answer5 = """
select mk.kwd_name as keyword, count(distinct mk.movie_id) as num
from movie m
join movie_genre mg
on m.release_year > 2010
and m.movie_id = mg.movie_id
and mg.genre_name = 'Comedy'
join movie_keyword mk
on m.movie_id = mk.movie_id
group by mk.kwd_name
having count(distinct mk.movie_id) > 50
order by num desc
fetch first 10 rows only;
"""

answer6 = """
with a as (
    select mc.id, count(ci.movie_id) as num_movies
    from movie_cast mc
    left join cast_in ci
    on mc.id = ci.cast_id
    where mc.gender = 1
    group by mc.id
)
select num_movies, count(id) as num_actors
from a
group by num_movies
order by num_movies asc;
"""

answer7 = """
with a as (
    select distinct ci.movie_id
    from movie_cast mc
    join cast_in ci
    on ci.cast_id = mc.id
    and mc.name = 'Inuko Inuyama'
), b as (
    select ci.cast_id
    from cast_in ci
    join a
    on ci.movie_id = a.movie_id
    group by ci.cast_id
    having count(ci.movie_id) = (select count(*) from a)
)
select mc.id, mc.name
from b
join movie_cast mc
on mc.id = b.cast_id
and mc.name <> 'Inuko Inuyama';
"""

answer8 = """
with a0 as (
    select id from movie_cast where name = 'Brian Evers'
), b0 as (
    select movie_id from cast_in where cast_id = (select * from a0)
), a1 as (
    select distinct c1.cast_id, 1 as n from cast_in c1 join b0 on b0.movie_id = c1.movie_id
), b1 as (
    select distinct c2.movie_id from cast_in c2 join a1 on a1.cast_id = c2.cast_id
), a2 as (
    select distinct c3.cast_id, 2 as n from cast_in c3 join b1 on b1.movie_id = c3.movie_id
), b2 as (
    select distinct c4.movie_id from cast_in c4 join a2 on a2.cast_id = c4.cast_id
), a3 as (
    select distinct c5.cast_id, 3 as n from cast_in c5 join b2 on b2.movie_id = c5.movie_id
), a as (
    select cast_id, n from a1
    union all select cast_id, n from a2
    union all select cast_id, n from a3
)
select mc2.id, mc2.name, min(n) as n
from a
join movie_cast mc2
on a.cast_id = mc2.id
and mc2.id not in (select id from a0)
group by mc2.id, mc2.name;
"""



# MYSQL QUERIES

# The database you set up on RDS - SPECIFICALLY FOR SUBMISSION

db_config = {
    "username" : "admin",
    "host": "database-2.cl03devemfhy.us-east-2.rds.amazonaws.com",
    "port": "3306",
    "password": "88888888"
}


# Fill in DDL statements in the order of execution. A deduction might be applied for an incorrect order.
# Create query for Airlines
answer9a = """
CREATE TABLE Airlines(
    id int(11),
    name varchar(20),
    alias varchar(20),
    iata char(2),
    icao char(3),
    callsign varchar(20),
    country varchar(20),
    active char(1),
    PRIMARY KEY (id));
"""

# Create query for Airports
answer9b = """
CREATE TABLE Airports(
    id int(11),
    name varchar(20),
    city varchar(20),
    country varchar(20),
    iata char(3),
    icao char(4),
    lat decimal(8,6),
    lon decimal(9,6),
    alt int(11),
    timezone decimal(3,1),
    dst char(1),
    tz varchar(20),
    PRIMARY KEY (id));
"""

# Create query for Routes
answer9c = """
CREATE TABLE Routes(  
    airline_iata char(3),
    airline_id int(11),
    src_iata_icao char(4),
    source_id int(11),
    target_iata_icao char(4),
    target_id int(11),
    code_shar char(1),
    equipment char(20),
    CHECK (code_shar in ('Y', ' ')),
    FOREIGN KEY (airline_id) REFERENCES Airlines(id),
    FOREIGN KEY (source_id) REFERENCES Airports(id),
    FOREIGN KEY (target_id) REFERENCES Airports(id));
"""

answer10 = """
SELECT name
FROM Airlines
WHERE country = 'France'
AND active = 'Y';
"""

answer11 = """
SELECT city, COUNT(*) AS NumAirports
FROM Airports
WHERE country = 'United States'
GROUP BY city
HAVING COUNT(*) > 3;
"""

answer12 = """
WITH a AS (
    SELECT airline_id, COUNT(*) AS num
    FROM Routes
    GROUP BY airline_id
)
SELECT
    (SELECT MIN(num) FROM a
     WHERE num <= ALL (SELECT num FROM a)) as MinRoutes,
    (SELECT MAX(num) FROM a
     WHERE num >= ALL (SELECT num FROM a)) as MaxRoutes,
    (SELECT AVG(num) FROM a) AS AvgRoutes;
"""

answer13 = """
with a as (
    select r.source_id, a.name as source_name, r.target_id, a2.name as target_name
    from Routes r
    join Airports a
    on r.source_id = a.id
    join Airports a2
    on r.target_id = a2.id
)
select distinct source_name as name
from a
where source_name not in (select target_name from a)
order by name asc;
"""

answer14 = """
with a as (
    select name, id, city
    from Airports
    where country = 'United States'
    and city in ('Los Angeles', 'San Francisco')
)
select ap.name as airport_name,
       sum(case a.city when 'San Francisco' then 1 else 0 end) as num_SF,
       sum(case a.city when 'Los Angeles' then 1 else 0 end) as num_LA
from Routes r
join a
on r.target_id = a.id
join Airports ap
on r.source_id = ap.id
and ap.country = 'United States'
and ap.city not in ('Los Angeles', 'San Francisco')
group by ap.name
having sum(case a.city when 'San Francisco' then 1 else 0 end) > 0
and sum(case a.city when 'Los Angeles' then 1 else 0 end) > 0;
"""
