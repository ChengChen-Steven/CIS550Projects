/*******************************************************************************
********************************************************************************

                              CIS 550
                              Homework 5

Note: This assignment will be autograded, therefore, you must follow these
  instructions in order for your submission to be processed successfully.
  Violating any of these instructions will cause the autograder to deduct
  your grade, and you might receive a ZERO.

  General:
    - Do not modify the comments that are included in the skeleton file.
    - Do not write any comments that look similar to the ones we wrote
    - Read the writeup carefully for instructions on how to place your
        answers.


********************************************************************************
*******************************************************************************/

/**************************     Part 1: MongoDB     ***************************/

// Question 1
var answer_1 = db.laureates.find({$or: [{"bornCity": "Philadelphia, PA"}, {"prizes.affiliations.name": "University of Pennsylvania"}]}).count();

// Question 2
var answer_2 = db.laureates.find({$and: [{"gender": "male"}, {"prizes.category": {$in: ["economics", "peace"]}}]}, {"firstname":1, "surname":1, "_id":0});

// Question 3
var answer_3 = db.laureates.aggregate({$project: {affiliationName:"$prizes.affiliations.name"}}, {$unwind:"$affiliationName"}, {$unwind:"$affiliationName"}, {$group: {_id:"$affiliationName", num: {$sum: 1}}}, {$sort: {num: -1}});
// Question 4
var answer_4 = db.laureates.aggregate({$match: {$and: [{"prizes.motivation": {$regex: /discovery/}}, {$or: [{"born": {$regex: /^19/}}, {"born": {$regex: /^20/}}]}]}}, {$group: {_id: "$bornCountry", number: {$sum: 1}}}, {$sort: {number: -1}}, {$limit: 1});

// Question 5
var answer_5 = db.Prizes.aggregate({$match: {$and: [{category: "physics"}, {year: {$in: ["2016", "2017", "2018", "2019", "2020", "2021"]}}]}}, {$unwind: "$laureates"}, {$project: {year:1, id:"$laureates.id", firstname: "$laureates.firstname", surname:"$laureates.surname", _id:0}});

// Question 6
var mapFunction = function() {emit(this.year, this.laureates.length);};
var reduceFunction = function(yearAwarded, arrayLaureates) {return Array.sum(arrayLaureates);};
var answer_6 = db.Prizes.mapReduce(mapFunction, reduceFunction, {out:{inline: 1}});

// Question 7
var answer_7 = db.Prizes.aggregate({$unwind: "$laureates"}, {$group: {_id:"$year", value:{$sum:1}}});