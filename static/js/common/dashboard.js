// Query Text color
const blueText = ['DROP','CREATE','TABLE','SEQUENCE','NOT','NULL','DEFAULT', 'CONSTRAINT', 'PRIMARY', 'KEY', 'UNIQUE',"SELECT","from"]
const yellowText = ['nextval', 'integer', '::regclass','timestamp','text', 'varchar']


$(document).ready(function(){
//map chart display from setting.json
    if (mapUse.WorldUse == 'block'){
        $('#korea-map, #seoul-map, #seongnam-map').hide();
        $('#world-map').show();
        }
    else if (mapUse.KoreaUse == 'block'){
        $('#world-map, #seoul-map').hide();
        $('#korea-map').show();
        }
    else if (mapUse.AreaUse == 'block'){
        if (mapUse.AreaType == 'seoul-map'){
        $('#world-map, #korea-map, #seongnam-map').hide();
        $('#seoul-map').show();
        }
        else if (mapUse.AreaType == 'seongnam-map'){
        $('#world-map, #korea-map, #seoul-map').hide();
        $('#seongnam-map').show();
        }
    };


   $(".who_btn").click(function() {
       $(".who_btn").removeClass("active");
        $(this).addClass("active");
    });

//map chart 버튼
    $('#worldBtn').click(function() {
        $('#world-map').show();
        $('#korea-map, #seoul-map, #seongnam-map').hide();
        $('#world-map, #korea-map, #seongnam-map').removeClass("selectMap");
        $('#world-map').addClass("selectMap");
        zoomCount = 1;
        reset_xy()
        dragMap()
        $('.selectMap').css('transform','scale(1)');
    });

    $('#koreaBtn').click(function() {
        $('#korea-map').show();
        $('#world-map, #seoul-map, #seongnam-map').hide();
        $('#world-map, #korea-map, #seongnam-map').removeClass("selectMap");
        $('#korea-map').addClass("selectMap");
        zoomCount = 1;
        reset_xy()
        dragMap()
        $('.selectMap').css('transform','scale(1)');
    });

    $('#areaBtn').click(function() {
        if (mapUse.AreaType == 'seoul-map'){
        $('#world-map, #korea-map, #seongnam-map').hide();
        $('#seoul-map').show();
        }
        else if (mapUse.AreaType == 'seongnam-map'){
        $('#world-map, #korea-map, #seoul-map').hide();
        $('#world-map, #korea-map, #seongnam-map').removeClass("selectMap");
        $('#seongnam-map').show();
        $('#seongnam-map').addClass("selectMap");
        zoomCount = 1;
        reset_xy()
        dragMap()
        $('.selectMap').css('transform','scale(1)');

        }
    });

    let startDrag
    let endDrag
    let xLocation = 0;
    let yLocation = 0;
    let lastX = 0;
    let lastY = 0;

//map 줌인 줌아웃 버튼
    let zoomCount = 1;
    $('.map-zoomIn').on('click',function(){
        if(zoomCount < 10){
            zoomCount = zoomCount + 0.1;
        }
        $('.selectMap').css('transform',"scale("+ zoomCount + ") translate(" + lastX  + "px," + lastY +"px)")
 });

    $('.map-zoomOut').on('click',function(){
        if(zoomCount > 1){
            zoomCount = zoomCount - 0.1;
             }
        $('.selectMap').css('transform',"scale("+ zoomCount + ") translate(" + lastX  + "px," + lastY +"px)")
 });
    const reset_xy = function(){
        xLocation = 0;
        yLocation = 0;
        lastX = 0;
        lastY = 0;
    }

    $(".bi-fullscreen").click(function() {
        $('.selectMap').css('transform',"translate(0px,0px)")
        zoomCount = 1;
        reset_xy()
    });

    const dragMap = function(){
// 이미지 드래그 기능
    $('.selectMap').on({
    'mousedown':function(e){
        startDrag = [event.offsetX,event.offsetY];
        $('.selectMap').css('cursor','grabbing')
        $('.selectMap').on('mousemove', function(e){
            endDrag = [event.offsetX,event.offsetY];
            xLocation = endDrag[0] - startDrag[0];
            yLocation = endDrag[1] - startDrag[1];
            lastX = lastX + xLocation
            lastY = lastY + yLocation
            $('.selectMap').css('cursor','grabbing')
            $('.selectMap').css('transform',"scale("+ zoomCount + ") translate(" +  lastX  + "px," + lastY  +"px)")
        });
    },
    'mouseup':function(e){
       $('.selectMap').off('mousemove');
       $('.selectMap').css('cursor','grab')
    }

});
};
    dragMap()
});


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
    const $Memory = $('.MemoryCharts')
    const $CPU = $('.CPUCharts')
    const $Disk = $('.DiskCharts')

    $(".mcdBtn").on('click',function(){
        $(".mcdBtn").removeClass("active");
        $(this).addClass("active");

        if($(this).text() === '메모리'){
            $($Memory).css("display","block");
            $($CPU).css("display","none");
            $($Disk).css("display","none");
            return;
        }

        if($(this).text() === 'CPU'){
            $($Memory).css("display","none");
            $($CPU).css("display","block");
            $($Disk).css("display","none");
            return;
        }
        if($(this).text() === '디스크'){
            $($Memory).css("display","none");
            $($CPU).css("display","none");
            $($Disk).css("display","block");
            return;
        }
    });
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
        else if($(this).is('.menu-list2')){
            var mother = $(this).closest('.Navi-DF-menu2')
            if($(this).is('.bi-caret-right-fill')){
                $(this).removeClass("bi-caret-right-fill")
                $(this).addClass("bi-caret-down-fill")
                mother.children(".Navi-DF-menu3").css("display",'block');
            } else if($(this).is('.bi-caret-down-fill')) {
                $(this).removeClass("bi-caret-down-fill")
                $(this).addClass("bi-caret-right-fill")
                mother.children(".Navi-DF-menu3").css("display",'none');
            }
        }
        else if($(this).is('.menu-list3')){
            var mother = $(this).closest('.Navi-DF-menu3')
            if($(this).is('.bi-caret-right-fill')){
                $(this).removeClass("bi-caret-right-fill")
                $(this).addClass("bi-caret-down-fill")
                mother.children(".Navi-DF-menu4").css("display",'block');
            } else if($(this).is('.bi-caret-down-fill')) {
                $(this).removeClass("bi-caret-down-fill")
                $(this).addClass("bi-caret-right-fill")
                mother.children(".Navi-DF-menu4").css("display",'none');
            }
        }
        else if($(this).is('.menu-list4')){
            var mother = $(this).closest('.Navi-DF-menu4')
            if($(this).is('.bi-caret-right-fill')){
                $(this).removeClass("bi-caret-right-fill")
                $(this).addClass("bi-caret-down-fill")
                $(this).children(".bi").removeClass("bi-folder")
                $(this).children(".bi").addClass("bi-folder2-open")
                mother.children(".Navi-DF-menu5").css("display",'block');
            } else if($(this).is('.bi-caret-down-fill')) {
                $(this).removeClass("bi-caret-down-fill")
                $(this).addClass("bi-caret-right-fill")
                $(this).children(".bi").removeClass("bi-folder2-open")
                $(this).children(".bi").addClass("bi-folder")
                mother.children(".Navi-DF-menu5").css("display",'none');
            }
        }
        else if($(this).is('.menu-list5')){
            var mother = $(this).closest('.Navi-DF-menu5')
            if($(this).is('.bi-caret-right-fill')){
                $(this).removeClass("bi-caret-right-fill")
                $(this).addClass("bi-caret-down-fill")
                $(this).children(".bi").removeClass("bi-folder")
                $(this).children(".bi").addClass("bi-folder2-open")
                mother.children(".Navi-DF-menu6").css("display",'block');
            } else if($(this).is('.bi-caret-down-fill')) {
                $(this).removeClass("bi-caret-down-fill")
                $(this).addClass("bi-caret-right-fill")
                $(this).children(".bi").removeClass("bi-folder2-open")
                $(this).children(".bi").addClass("bi-folder")
                mother.children(".Navi-DF-menu6").css("display",'none');
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

   $('.query-input').on('input',function(event){
        let queryText = event.currentTarget.value
        let split_txt = queryText.split('\n');
        let textHere = $(this).next()
        let i = 0
        console.log(queryText)
        $(textHere).text("");
        split_txt.forEach(function(spText){
            let noComment = 0
            if (i >= 1){
                $(textHere).append('<br>')
            }
            let text = spText.trim();

//            숫자 구분 () 안에 들어간 숫자  0
            queryText = text.split(' ')
            if(text.startsWith('--')){
                $(textHere).append('<span class = "text-comment">' + text + '</span>')
                noComment++
            }
               queryText.forEach(function(qrText){
                  let defaultColor = 0
                  let tap = text.split('\t')
                  let uppText = qrText.toUpperCase();
                  blueText.forEach(function(bText){
                    if (uppText === bText.toUpperCase()){
                        $(textHere).append('<span class = "text-queryBlue">' + qrText + ' </span>')
                        defaultColor++
                    }
                  });
                  yellowText.forEach(function(yText){
                     if (uppText === yText.toUpperCase()){
                       $(textHere).append('<span class = "text-queryYellow">' + qrText + ' </span>')
                        defaultColor++
                    }
                  });
                  if(qrText == ''){
                    $(textHere).append('<span>​</span>')
                  }
                  if (defaultColor == 0 && noComment == 0){
                    $(textHere).append('<span>' + qrText + '</span>')
                  }

                });


            i++
        });
    });
});



