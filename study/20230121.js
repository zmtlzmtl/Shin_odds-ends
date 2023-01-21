// let userName = 'John';

// function showMessage() {
//   userName = "Bob"; // (1) 외부 변수를 수정함

//   let message = 'Hello, ' + userName;
//   console.log(message);
// }

// console.log( userName ); // 함수 호출 전이므로 John 이 출력됨

// showMessage();

// console.log( userName ); // 함수에 의해 Bob 으로 값이 바뀜

// QQQQQ!
// 위는 외부변수가 내부변수로 인해 수정되는데 밑은 조금 다른데 수정이
// 안됨, 다른건 알듯한데 뭔지 모르겠음.


// let userName = 'John';

// function showMessage() {
//   userName = "Bob"; // (1) 외부 변수를 수정함

//   let message = 'Hello, ' + userName;
//   console.log(message);
// }

// console.log( userName ); // 함수 호출 전이므로 John 이 출력됨

// showMessage();

// console.log( userName ); // 함수에 의해 Bob 으로 값이 바뀜
//                         // ^
//                         // |
//                         // |
//                         // |
//                         // |

// let from = "Ann";

// function showMessage(from, text) {

//     from = '*' + from + '*'; // "from"을 좀 더 멋지게 꾸며줍니다.
//     //외부변수 from이 아니라 매개변수 from을 꾸며주는건가?
  
//     console.log( from + ': ' + text );
//   }
  
  
//   showMessage(from, "Hello"); // *Ann*: Hello
  
//   // 함수는 복사된 값을 사용하기 때문에 바깥의 "from"은 값이 변경되지 않습니다.
//   console.log( from ); // Ann


//   function minn(a,b) {
//     return a > b ? b : a;
//   }
//   console.log(minn(3,4));

function pow(a,b) {
    return a**b
}
console.log(pow(3,4));