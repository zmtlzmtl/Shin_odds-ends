function solution(numbers) {
    //console.log(numbers)
    let answer = numbers[0];
    
    for (i=1; i < numbers.length; i++) {
        answer += numbers[i];
    } return answer / numbers.length;
}