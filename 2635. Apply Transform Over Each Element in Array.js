/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
const returned = [];
arr.forEach((item, index)=>{returned[index]=fn(item,index)})
return returned
};