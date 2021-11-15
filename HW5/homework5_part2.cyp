
//////////////////////////     Part 2: Neo4J     ///////////////////////////////
/////////// IMPORTANT: DO NOT ADD/REMOVE ANY COMMENTS TO THIS FILE /////////////

// Question 8
CREATE (n15:City{name:"Paris", country:"United States of America"}) 



// Question 9
MATCH (c1:City)-[:HAS_FLIGHT]->(f:Flight)-[:FLYING_TO]->(c2:City {name: "London"}) RETURN c1, f, c2



// Question 10
MATCH (f:Flight) WHERE f.source_airport_code =~ "A.*" OR f.source_airport_code =~ "L.*" RETURN f.source_airport_code as airport_code UNION MATCH(f:Flight) WHERE f.destination_airport_code =~ "A.*" OR f.destination_airport_code =~ "L.*" RETURN f.destination_airport_code as airport_code



// Question 11
MATCH (c1:City)-[:HAS_FLIGHT]->(f:Flight)-[:FLYING_TO]->(c2:City) WITH c1, collect(distinct c2.name) as destinations RETURN c1.name, destinations ORDER BY c1.name



// Question 12
MATCH (c1:City)-[:HAS_FLIGHT]->(f:Flight)-[:FLYING_TO]->(c2:City)  WHERE c1.country <> c2.country  with collect(distinct c1.name) as jcity MATCH (c3:City) WHERE NOT c3.name IN jcity RETURN distinct c3.name

