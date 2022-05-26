
$(".button-minus").click(function(){
    let product_id = $(this).attr('data-id')
    $.ajax({
        type: "post",
        url: "/cart/ajax/minus/"+product_id+"/"
    }).done(function(){
        location.reload();
    });
})


$(".button-plus").click(function(){
    let product_id = $(this).attr('data-id')
    $.ajax({
        type:"post",
        url: "/cart/ajax/add/"+product_id+"/"
    }).done(function(){
        location.reload();
    })
})
