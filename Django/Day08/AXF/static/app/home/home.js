$(document).ready(function () {

        swiper1()
    swiper2()
})



function swiper1() {

    var mySwiper = new Swiper ('#topSwiper', {
        direction: 'horizontal',
    loop: true,// 循环模式选项
    pagination: '.swiper-pagination',// 如果需要分页器
    autoplay: 1500, //轮播图
    autoplayDisableOnInteraction: false, //默认为true ,当设为false的时候触碰,拖动操作时会停止自动轮播,并且重新启动一个autoplay
    })

}

function swiper2() {

    var mySwiper = new Swiper ('#swiperMenu', {
    loop: true,// 循环模式选项
    // pagination: '.swiper-pagination',// 如果需要分页器
        slidesPerView:3, //显示3个
        paginationClickable: true, //可以点击
        spaceBetween:2, //间距为2



    })

}

