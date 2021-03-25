/// /////////////////////////
// LIKES
/// /////////////////////////

const JS_CSRFTOKEN = document.querySelector('[name=csrfmiddlewaretoken]').value
const JS_ICON_HEART_GRAY = "{% static 'img/heart-icon.png' %}"
const JS_ICON_HEART_BLUE = "{% static 'img/heart-icon-red.png' %}"

const likes = () => {
  // Global valuable
  // Clicked like icon
  likes('.js-like').click(function () {
    const tweetId = likes(this).data('tweet-id')
    const likeCountObj = likes(this).parent().find('.js-like-count')
    const likeCount = Number(likeCountObj.html())
    const heartIconObj = likes(this).find('img')
    const heartIconUrl = heartIconObj.attr('src')

    if (heartIconUrl === JS_ICON_HEART_GRAY) {
      // It has not been liked
      // Increase the count of likes
      likes.ajax({
        url: '/tweetLikeAdd/' + tweetId + '/',
        type: 'POST',
        data: {},
        headers: { 'X-CSRFToken': JS_CSRFTOKEN }
      })
      // Successful
        .done((data) => {
          // Increase
          const newLikeCount = likeCount + 1
          likeCountObj.html(newLikeCount)

          // Change the icon
          heartIconObj.attr('src', JS_ICON_HEART_BLUE)
        })
      // Failure
        .fail((data) => {
          console.log('Error')
          console.log(data)
        })
    } else {
      // It has been liked
      // Decrease the count of likes
      likes.ajax({
        url: '/tweetLikeSubtract/' + tweetId + '/',
        type: 'POST',
        data: {},
        headers: { 'X-CSRFToken': JS_CSRFTOKEN }
      })
      // Successful
        .done((data) => {
          // Decrease
          const newLikeCount = likeCount - 1
          likeCountObj.html(newLikeCount)

          // Change the button to blue
          heartIconObj.attr('src', JS_ICON_HEART_GRAY)
        })
      // Failure
        .fail((data) => {
          console.log('Error')
          console.log(data)
        })
    }
  })
}
