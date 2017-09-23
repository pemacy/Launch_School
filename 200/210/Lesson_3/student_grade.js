// student_grade.js

var grades = [];
for (i = 0; i < 3; i++) {
  grades[i] = prompt('Enter grade' + String(i + 1));
}

total = grades.reduce(function(sum, total) {
  return sum + parseInt(total, 10);
}, 0);

var ave = Math.round(total / 3);
var grade;

if (ave > 90) {
  grade = 'A';
} else if (ave >= 80) {
  grade = 'B';
} else if (ave >= 70) {
  grade = 'C';
} else if (ave >= 60) {
  grade = 'D';
} else {
  grade = 'F';
}

alert("Average is: " + String(ave) + ". Grade is a :" + grade);
