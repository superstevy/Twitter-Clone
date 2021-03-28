/// /////////////////////////
// LIKES
/// /////////////////////////

const JS_ICON_HEART = "{% static 'img/heart-icon.png' %}"
const JS_ICON_HEART_RED = "{% static 'img/heart-icon-red.png' %}"

const likes = () => {
  const likeCountObj = this.parent().find('.js-like-count')
  const likeCount = Number(likeCountObj.html())
  const heartIconObj = this.find('img')
  const heartIconUrl = heartIconObj.attr('src')

  if (heartIconUrl === JS_ICON_HEART) {
    // It has not been liked
    // Increase the count of likes
    const newLikeCount = likeCount + 1
    likeCountObj.html(newLikeCount)

    // Change the icon
    heartIconObj.attr('src', JS_ICON_HEART_RED)
  } else {
    // It has been liked
    // Decrease the count of likes
    // Decrease
    const newLikeCount = likeCount - 1
    likeCountObj.html(newLikeCount)

    // Change the button to blue
    heartIconObj.attr('src', JS_ICON_HEART)
  }
}
