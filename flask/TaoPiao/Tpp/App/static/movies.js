$(function () {

    get();
    function get(flag=1){



    $.ajax({
        type: 'GET',
        // url: '/movies/?flag='+flag,
        url: '/movies/',
        data: {flag: flag},
        success:function (data) {
            console.log(data);
           let movies = data.movies;
           $('#list').empty();
           for (let i = 0; i<movies.length; i++){
               let movie = movies[i];
               imgsrc = 'http://img.alicdn.com/bao/uploaded/' + movie.backgroundpicture

               $("<li><img src="+ imgsrc +"></li>").appendTo('#list')

           }
        },
        error:function (e) {
            console.log(e)
        }
    })
    }

    $('#btn1').click(function () {
        get()
    })
    $('#btn2').click(function () {
        get(2)
    })
});