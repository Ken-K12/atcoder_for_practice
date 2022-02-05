// 問題文
// シカのAtCoDeerくんは二つの正整数 a,b を見つけました。 
// a と b の積が偶数か奇数か判定してください。

// 制約
// 1 ≤ a,b ≤ 10000
// a,b は整数

//
function Main(input) {
    input = input.split(" ");
    let a = parseInt(input[0], 10);
    let b = parseInt(input[1], 10);
    let c = a * b;
    if(c % 2 == 0){
        console.log("Even");
    }else{
        console.log("Odd");
    }
}
  
Main(require("fs").readFileSync("/dev/stdin", "utf8"));