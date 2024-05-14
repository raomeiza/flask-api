const strings = 'askdhfiaweiurp89w998ur8ouwe8u';
let high;
const highest = strings.split('').reduce((acc, cur) => {
  if((cur >= 'a' && cur <= 'z') || (cur >= 'A' && cur <= 'Z')) {
    acc[cur] = acc[cur] ? acc[cur] + 1 : 1;
    if(!high) {
      high = cur;
    } else if(acc[cur] > acc[high]) {
      high = cur;
    }
  }
  return acc;
}, {});

console.log(high);