$(function () {

    //获取数据
    // $.ajax({
    //     type: 'GET',
    //     url: 'http://192.168.154.142:5000/banner/',
    //     success: function(data) {
    //     let banners = data.banners;
    //     for (let i = 0; i<banners.length; i++){
    //         let img = banners[i].img;
    //         $("<li><img src="+ img +"></li>").appendTo('#list1');
    //         let li = $("<li>"+(i+1)+"</li>").appendTo('#list2');
    //         if(i == 0){
    //             li.addClass('active')
    //         }
    //
    //
    //     }
    //
    //
    //
    //         //创建好节点后， 开始轮播
    //         lunbo();
    //     }
    // });

    $.ajax({
        type : 'GET',
        url : 'http://192.168.154.142:5000/banner/',
        success: function (data) {
            let banners = data.banners;
            for (let i = 0; i< banners.length; i++){
                let img = banners[i].img;
                $("<li><img src="+ img +" alt=''></li>").appendTo('#list1');
                let li =  $("<li>"+(i+1)+"</li>").appendTo('#list2');
                if(i == 0){
                    li.addClass('active')
                }

            }
            lunbo()
        }
    })


    //jq轮播图
    function lunbo() {

        let list1 = $("#list1");
        let list2 = $("#list2");
        let li1 = $("#list1 li");
        let li2 = $("#list2 li");

        //复制第一张图到最后
        li1.first().clone(true).appendTo(list1);

        //
        let size = $("#list1 li").size();
        list1.width(600 * size);

        //开启定时器
        let i = 0;
        let timer = setInterval(function () {
            i++;
            move();
        }, 2000);

        function move() {

            if (i < 0) {
                list1.css("left", -600 * (size - 1));
                i = size - 2;
            }

            if (i >= size) {
                list1.css("left", 0);
                i = 1;
            }

            list1.stop().animate({left: -i * 600}, 500);

            li2.eq(i).addClass("active").siblings().removeClass("active");
            if (i == size - 1) {
                li2.eq(0).addClass("active").siblings().removeClass("active");
            }
        }

        //上一页
        $("#prev").click(function () {
            i--;
            move();
        });

        //下一页
        $("#next").click(function () {
            i++;
            move();
        });

        li2.mouseenter(function () {
            i = $(this).index();
            move();
        });

        $("#box").hover(function () {
                console.log("mouseenter");
                clearInterval(timer);
            },
            function () {
                console.log("mouseleave");
                timer = setInterval(function () {
                    i++;
                    move();
                }, 2000);
            })
    }
});