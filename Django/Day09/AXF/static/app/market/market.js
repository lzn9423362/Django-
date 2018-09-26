$(document).ready(function () {

    var alltype = document.getElementById('all_type')
    var showsort = document.getElementById('sort_rule')
    var typediv = document.getElementById('typeid')
    var sortdiv = document.getElementById('sortdiv')

    typediv.style.display = 'none'
    sortdiv.style.display = 'none'


    alltype.addEventListener('click',function(){

        typediv.style.display = 'block'
        sortdiv.style.display = 'none'
    },false)
    showsort.addEventListener('click',function(){

        typediv.style.display = 'none'
        sortdiv.style.display = 'block'
    },false)
   typediv.addEventListener('click',function(){

        typediv.style.display = 'none'
    },false)
    sortdiv.addEventListener('click',function(){

        sortdiv.style.display = 'none'
    },false)

})


