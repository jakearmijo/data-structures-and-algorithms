

function ClassPhoto(redShirtHeights, blueShirtHeights) {
// first things is sort both array in place
redShirtHeights.sort((a,b) => b - a)
blueShirtHeights.sort((a,b) => b - a)
// determine which shirt is in front and back
let shirtColorInFirstRow = redShirtHeights[0] < blueShirtHeights[0] ? 'RED' : 'BLUE'
// FOR - loop through array
for (let i = 0; i < redShirtHeights.length; i++) {
  // create redheight and blue height variable
  // assign them them to their array at index -> redShirtHeights[i]
  const redHeight = redShirtHeights[i]
  const blueHeight = blueShirtHeights[i]

  // if the front color is red and its height is greate then the blue height return false
  // if the front row is blue and its greater then the larget red return false
  if(shirtColorInFirstRow === 'RED') {
    if (redHeight >= blueHeight) return false
  } else if (blueHeight >=redHeight) return false
}
// if all goes well it returns true
  return true
}