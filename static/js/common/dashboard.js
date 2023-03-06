// Query Text color
const blueText = ['DROP','CREATE','TABLE','SEQUENCE','NOT','NULL','DEFAULT', 'CONSTRAINT', 'PRIMARY', 'KEY', 'UNIQUE',"SELECT","from"]
const yellowText = ['nextval', 'integer', '::regclass','timestamp','text', 'varchar']



// swiper 배너
$(document).ready(function () {

  var mySwifer = new Swiper('.swiper-container', {
      slidesPerView: 8,
      spaceBetween: 30,
      slidesPerGroup: 1,
      loopFillGroupWithBlank: true,
      loop: true,
      autoplay: {
          delay: 1000,
          disableOnInteraction: false,
        },
      breakpoints: {
          0: {
              slidesPerView: 1,
          },
          520: {
              slidesPerView: 2,
          },
          950: {
              slidesPerView: 3,
          },
          1000: {
              slidesPerView: 4,
          },
          1700: {
              slidesPerView: 6,
          },
          1920: {
            slidesPerView: 8,
          },
      },
  })
    $('.swiper-slide').hover(function(){
        mySwifer.autoplay.stop();
     }, function(){
        mySwifer.autoplay.start();
    });
});

// 메모리 CPU 디스크 버튼
$(document).ready(function () {
   
// X-factor DF
	 $(".btn-dataNavi").on('click',function(){
        const dataNavi = ['Teradata','Postgres','ETC']
        $(".btn-dataNavi").removeClass("active");
        $(this).addClass("active");
        let btnText = $(this).text()
        dataNavi.forEach(function(element){
         if(btnText === element){
            $('.Navi-DF').css("display","none");
            $('.Navi-DF-' + element +'-menu').css("display","block");
            }
        });
    });
    const textBoxHover = function(){
        $(".table-textBox").on({
            'mouseover':function(){
                $(this).addClass("textBox-scroll")
            },
            'mouseout':function(){
                $(this).removeClass("textBox-scroll")
            }
        });
    };

    $(".btn-tableProperties").on('click',function(){
//    Data Columns View Procedure DDL
        const tableProperties = ['Data', 'Column', 'View', 'Procedure', 'DDL']
        $(".btn-tableProperties").removeClass("active");
        $(this).addClass("active");
        let btnText = $(this).text()
        tableProperties.forEach(function(element){
             if(btnText === element){
                $('.properties').css("display","none");
                $(".properties-" + element).css("display","table");

                $(".TableProperties").css("display","table");
             }
         });
         textBoxHover()
    });

    $(".menu-list").on('click',function(){
        if($(this).is('.menu-list1')){
            var mother = $(this).closest('.Navi-DF-menu1')
            if($(this).is('.bi-caret-right-fill')){
                $(this).removeClass("bi-caret-right-fill")
                $(this).addClass("bi-caret-down-fill")
                mother.children(".Navi-DF-menu2").css("display",'block');
            } else if($(this).is('.bi-caret-down-fill')) {
                $(this).removeClass("bi-caret-down-fill")
                $(this).addClass("bi-caret-right-fill")
                mother.children(".Navi-DF-menu2").css("display",'none');
            }
        }
        


            });


    let qTab = $('.query-tabs').children().last()
    let cTab = $('.query-tabContent').children().last()
    let delBtn = qTab.children().children().last()
    let number = 1
    $("#addScript").on('click',function(){
        let qHasClass = 0;
        let cHasClass = 0;
        if (number < 10){
            if(cTab.hasClass("active") === true) {
                cTab.removeClass('active')
                cTab.removeClass('show')
                cTab.removeClass('active')
                cHasClass++
            }
            if(qTab.children().hasClass("active") === true) {
                qTab.children().last().removeClass('active')
                qHasClass++
            }
            delBtn = qTab.children().children().last().clone(true)
            qTab = $('.query-tabs').children().last().clone(true)
            cTab = $('.query-tabContent').children().last().clone(true)

            if(cHasClass === 1){
                cTab.addClass('active')
                cTab.addClass('show')
                cTab.addClass('active')
            }

            if(qHasClass === 1){
                qTab.children().last().addClass('active')

            }

            qTab.appendTo( $('.query-tabs') )
            cTab.appendTo( $('.query-tabContent') )

            number++;

            cTab.attr('id','Query'+ number)
            cTab.children().children().children().text("")
            qTab.children().last().text('Query')
            qTab.children().last().attr('href', '#Query' + number)
            delBtn.appendTo($('.query-tabs').children().last().children())

            }
        else{
              $('#alertQueryNot').modal('show')

            }
    });

    $(".delScript").on('click',function(){
    if (number > 1){
        let lastQtab = qTab.last()
        let lastCtab =cTab.last()
        lastQtab.remove()
        lastCtab.remove()
        qTab = $('.query-tabs').children().last()
        cTab = $('.query-tabContent').children().last()
        number--;
    }
    });


});




