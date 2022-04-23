// R - takes array and target - return 2 indices of the #'s that sum to target
// E - input: [2,7,11,15], 9 -> output: [0,1]
// A - FOR - loop through nums. find difference b/w target and current value. create hashMap tracker and add each current value on iteration when found.
// return the INDEX of value not the value itself
// C - see below
// T - TIME: O(n) where n is the length of the nums array. Object search/inser = O(1)
// S - SPACE: O(n) -> hashMap cost memory which could possibly take every element in array
// O - NA


const twoSumArrow = (nums,target) => {
  let hashMap = {}
  for (let i = 0; i < nums.length; i ++) {
      let difference = target - nums[i]
      if (hashMap.hasOwnProperty(difference)) {
          return [hashMap[difference], i]
      } else {
          hashMap[nums[i]] = i
      }
  }
}