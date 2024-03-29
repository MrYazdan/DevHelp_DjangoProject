// search form
$("label[for=search]").click(function () {
    $(this).parent().submit()
})

// timer
function timer(el, interval, hide_time = 300, dot_time = 0) {
    if (dot_time !== 0) {
        setInterval(function () {
            el.append(".")
        }, dot_time)
    }

    setTimeout(function () {
        el.fadeOut(hide_time)
    }, interval)

    setTimeout(function () {
        el.remove()
    }, interval + hide_time)
}

$('[timer]').each(function () {
    let Interval = Number($(this).attr("timer"))
    let dot_time = 0
    let hide_time = 300
    if ($(this)[0].hasAttribute("timer-dot")) {
        dot_time = $(this).attr("timer-dot")
    }
    if ($(this)[0].hasAttribute("timer-hide")) {
        hide_time = $(this).attr("timer-hide")
    }
    timer($(this), Interval, hide_time, dot_time)
})

// mostly views :
$('.mostly-views>a').mouseenter(function () {
    $('.mostly-views>a>img').not($(this).children("img")).addClass("filter grayscale")
}).mouseleave(function () {
    $('.mostly-views>a>img').removeClass("filter grayscale")
})

// blur effect :
$('.last-update-list>a').mouseenter(function () {
    $(this).children('div').removeClass("hidden")
    $(this).children('i,h3,p').addClass("filter blur-sm")
}).mouseleave(function () {
    $(this).children('div').addClass("hidden")
    $(this).children('i,h3,p').removeClass("filter blur-sm")
})

// random color selector
function arrayRemove(arr, value) {
    return arr.filter(function (ele) {
        return ele !== value
    })
}

$colors = ["#aab2be", "#fdbd30", "#28c840", "#62d3df", "#d483ef", "#f67171"]
$(".blinker").each(function () {
    let color = $colors[Math.floor(Math.random() * $colors.length)]
    $(this).children('h3, p').css('color', color)
    $(this).css('border-color', color)
    $colors = arrayRemove($colors, color)
});

// Hover
$('[hover-class]').each(function () {
    let el = $(this)
    let class_animate = el.attr('hover-class')
    if (el.attr("hover-child")) {
        el = el.children(el.attr("hover-child"))
        console.log(el)
    }
    $(this).mouseenter(function () {
        el.addClass(class_animate)
    }).mouseleave(function () {
        el.removeClass(class_animate)
    })
})