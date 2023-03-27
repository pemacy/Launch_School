// The function initGame below returns an object. Refactor it using arrow function syntax.

let initGame = function () {
  return {
    level: 1,
    score: 0
  };
};

let initGameArrow = () => ({
  level: 1,
  score: 0
});

let game = initGameArrow();

console.log('Level: ' + game.level);
console.log('Score: ' + game.score);
