/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let filteredArr = [];
      arr.forEach((item, index) => {
        if(fn(item, index)){filteredArr.push(item)}});
      return filteredArr;
  };