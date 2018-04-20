//Part I
// A function that responds 'Polo!' if it hears 'Marco'
function marcoPolo(heardWord){
  if(heardWord.toLowerCase() == "marco")
  {
    console.log("Polo!");
  }
  else
  {
    console.log("Try again!");
  }
};


//Part II
// 2 functions:
// 1. A function that takes a string and a callback function
function marcoPolo(heardWord){
  if(heardWord.toLowerCase() == "marco")
  {
    console.log("Polo!");
  }
  else
  {
    console.log("Try again!");
  }
};
// 2. A callback function that is called in response to the first function
function respond(heardWord, callBack) {
  return callBack(heardWord)
}
// and executes the same rules as Part I.
