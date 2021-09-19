var config = require('./db-config.js');
var mysql = require('mysql');

config.connectionLimit = 10;
var connection = mysql.createPool(config);

/* -------------------------------------------------- */
/* ------------------- Route Handlers --------------- */
/* -------------------------------------------------- */

/* ---- (Dashboard) ---- */
function getAllPeople(req, res) {
  var query = `
    SELECT login, name, birthyear
    FROM Person;
  `;
  connection.query(query, function(err, rows, fields) {
    if (err) console.log(err);
    else {
      res.json(rows);
    }
  });
};

/* ---- Part 2 (FindFriends) ---- */
function getFriends(req, res) {
  var inputLogin = req.params.login;
  
  // TODO: (3) - Edit query below
  var query = `
    select F.friend, P.name
    from Friends F 
    join Person P 
    on F.friend = P.login
    where F.login LIKE '${inputLogin}'
    ;
  `;
  connection.query(query, function(err, rows, fields) {
    if (err) console.log(err);
    else {
      console.log(rows);
      res.json(rows);
    }
  });
};

// The exported functions, which can be accessed in index.js.
module.exports = {
  getAllPeople: getAllPeople,
  getFriends: getFriends
}