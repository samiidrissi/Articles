var articleOffset = 0;

var articleLoader = function() {
    $.ajax({
        url: '/ajax/articles/?offset=' + articleOffset,
        success: function(data) {
            if (data.length > 0) {
                for (var i = 0, total = data.length; i < total; i++) {
                    var compile_data;
                    compile_data = '<h3>' + data[i].titre + '</h3>\
                        <p>' + data[i].contenu '|truncatewords_html:80 + </p>';

                    $('#ArticlesDiv').append(compile_data);
                }

                /* update the offset */
                articleOffset += 2
            } else {
                $('#ArticlesDiv').append('No articles found');
            }
        }
    });
}

/* Infinite scrolling for fetching articles */
var $window = $(window);
function prodScrollPosition() {
    var distance = $window.scrollTop() + $window.height();
    if ($('body').height() <= distance && $('#ArticlesDiv')) {
        articleLoader();
    }
}

$window.scroll(prodScrollPosition).scroll();

/* Manually initiate the first ajax request */
articleLoader();