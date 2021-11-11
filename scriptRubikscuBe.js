/*
 ** JS Script https://rubikscu.be/
 ** Copy paste this script in your devTools and use the shuffle function
 ** with an array of string representing movements  e.g. ("L'","R'","F2"]...)
 */

const movMap = {
  L: "rotateL",
  "L'": "rotateLi",
  R: "rotateR",
  "R'": "rotateRi",
  U: "rotateU",
  "U'": "rotateUi",
  D: "rotateD",
  "D'": "rotateDi",
  F: "rotateF",
  "F'": "rotateFi",
  B: "rotateB",
  "B'": "rotateBi",
};

/**
 *
 * @description Takes an array of string or a string representing rubik movement sequence.
 * @param {string[] | string} seq rubik movement sequence
 * @returns {void}
 */
function shuffle(seq) {
  const finalSequence = Array.isArray(seq) ? seq.join(" ") : seq;

  finalSequence.split(" ").forEach((mov) => {
    if (mov.includes("2")) {
      document.getElementById(movMap[mov[0]]).click();
      document.getElementById(movMap[mov[0]]).click();
    } else {
      document.getElementById(movMap[mov]).click();
    }
  });
}
