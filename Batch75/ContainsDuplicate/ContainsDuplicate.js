


const ContainsDuplicates = (nums) => {
  let hashMap = {}
  for (let i = 0; i < nums.length; i++){
      hashMap[nums[i]] ? hashMap[nums[i]] += 1 : hashMap[nums[i]]  = 1
      if (hashMap[nums[i]] === 2) {
          return true
      }
  }
  return false
};