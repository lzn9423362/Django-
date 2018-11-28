$(function(){
	
	

	//banner轮播， 使用ajax获取后端接口数据
	$.get("/banner/",function(data){
           let banners = data.banners;

        for (let i=0; i<banners.length; i++) {
            // 图片
            let img = banners[i].img

            // 创建节点
            $("<li><img src="+ img +" ></li>").appendTo("#ul1");

            // 序号

        }

		//在这里写DOM操作
        		lunbo3();




		//调用轮播图效果
	});
	
	

	
	// 轮播图效果
	function lunbo3(){
		var ul1 = document.getElementById("ul1"); 
		var ali = ul1.getElementsByTagName("li");
		ul1.appendChild(ali[0].cloneNode(true));
		var ol1 = document.getElementById("ol1");
		var oli = ol1.getElementsByTagName("li");
		var size = ali.length;
		var liw = ali[0].offsetWidth;
		ul1.style.width=liw*size+"px"; 
	
		var index = 0;
		var timer =setInterval(function(){
			index++;
			move();
		},3000)
	
		function move(){ 
			if(index>=size){
				ul1.style.left=0;
				index=1;
			}
			if(index<0){
				ul1.style.left=-liw*(size-1)+"px";
				index =size-2;
			}
			animate(ul1,{left:-index*liw});
			for(var i=0;i<oli.length;i++){
				if(i==index){
					oli[i].className="active";
				}
				else{
					oli[i].className="";
				}
				if(index==size-1){
					oli[0].className="active";
				}
			}
		}
		for(var i=0;i<oli.length;i++){
			oli[i].index = i;
			oli[i].onmouseenter = function(){
				index = this.index;
				move();
				clearInterval(timer);
			}
		}
		
		
		box.onmouseenter = function(){
			clearInterval(timer);
		}
		box.onmouseleave=function(){
			clearInterval(timer);
			timer = setInterval(function(){
				index++;
				move();
			},3000)
		}
		
		
		left1.onclick = function(){  
			index--;
			move();
		}
		right1.onclick = function(){
			index++;
			move(); 
		};		
		
	}
	// <li>
	// 						<img src="img/images/150831323345_1571x2000.JPG">
	// 						<div class="parcel">
	// 							<p>Y PROJECT</p>
	// 							<p>￥4699</p>
	// 						</div>
	// 					</li>

	// 首页商品数据, 使用ajax获取后端接口数据

	$.get("/goods/",function(data){
		let goods = data.goods
        for (let i = 0; i<goods.length; i++){
            let name = goods[i].name
            let price = goods[i].price
            let headImg = goods[i].headImg
            $("<li><img src="+ headImg +" ><div class='parcel'>"+ "<p>"+ name +"</p> " + "<p>"+ "￥" +price +"</p> "  +"</div>></li>").appendTo("#mygoods");

        }
	});







	
	
/*
 **********************************************
 **********************************************
 *************  后面的代码不用看了     ***************
 *************  后面的代码不用看了     ***************
 **********************************************
 **********************************************
 * */
	

	
	var shopnum = $.cookie("totalSum")?$.cookie("totalSum"):0
	$(".sumnum").html(shopnum);


	$(".con1 ul").on("mouseenter","li",function(){
		
		$(this).find(".parcel").stop(true).animate({left:65},300);
		$(this).find("img").stop(true).animate({left:85},300);
		$(this).find("img").stop(true).animate({left:85},300);
	})
	$(".con1 ul").stop(true).on("mouseleave","li",function(){
		$(this).find(".parcel").stop(true).animate({left:80})
		$(this).find("img").stop(true).animate({left:70},300);
	})
		 
	$(".con1 ul").on("click","li",function(){
		var index = $(this).index();
	})
	//没写完上面的是详情页面
	
	//上面是轮播图
	$(".tbox").on({
		"mouseenter":function(){
			$(this).stop().animate({top:175},300) 
		},
		"mouseleave":function(){
			$(this).stop().animate({top:274},300) 
		}
	})
   	//划出效果  	
   	$("#first").on({
   		"mouseenter":function(){
  			 $("#first ul").css("display","block") 
  			 $("#first ul li").mouseenter(function(){
  			 	$(this).find(".menu").find("div").css({display:"block"});
  			 	$(this).siblings().find(".menu").find("div").css({display:"none"});
  			 })
  			 $("#first ul li").mouseleave(function(){
  			 	$(this).find(".menu").find("div").css({display:"none"});
  			 })
  			 
  			 
   		},
   		"mouseleave":function(){
   			 $("#first ul").css("display","none") 
   		}
   	})

	//我的第五大道

	$(".gouwu,.cart2").mouseenter(function(){
		$(".cart2").stop().slideDown();
	})
	$(".gouwu,.cart2").mouseleave(function(){
		$(".cart2").stop().slideUp(); 
	})
	
	//phone
	$(".phonexia").mouseenter(function(){
		$(".phone").stop().fadeIn();
	})
	$(".phonexia,.phone").mouseleave(function(){
		$(".phone").stop().fadeOut(); 
	})

	//下面是链接购物车
	$(".cart1").click(function(){
		//location.href=""  
	})
	
	
	$(".side li").eq(1).css("display","block").on({
		"mouseenter":function(){
			$(".side1").fadeIn()
		},
		"mouseleave":function(){ 
			$(".side1").fadeOut()
		}
	})
	$(".side li").eq(2).css("display","block").on({
		"mouseenter":function(){
			$(".side2").fadeIn()
		},
		"mouseleave":function(){ 
			$(".side2").fadeOut()
		}
	})
	$(".side li").eq(3).css("display","block").on({
		"mouseenter":function(){
			$(".side3").fadeIn()
		},
		"mouseleave":function(){ 
			$(".side3").fadeOut()
		}
	})
	
	//回到顶部
	$(".callback").click(function(){
		$("body,html").animate({scrollTop:0},200)
		
	})

	//手风琴效果
	$("#accordion li").on({
		"mouseenter":function(){
			$(this).stop(true).animate({width:160},500) 
		},
		"mouseleave":function(){
			$(this).stop(true).animate({width:30},500)
		}
	})


});

