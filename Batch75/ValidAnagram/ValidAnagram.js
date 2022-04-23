const ValidAnagram = (s,t) => {
  let hashMapS = {}
  for (let i = 0; i < s.length; i++) {
      hashMapS[s[i]] ? hashMapS[s[i]] += 1 : hashMapS[s[i]]  = 1
  }
  for (let i = 0; i < t.length; i++) {
      if(!hashMapS[t[i]] || s.length !== t.length) {
          return false
      } else {
          hashMapS[t[i]] -= 1
      }
  }
  return true
};