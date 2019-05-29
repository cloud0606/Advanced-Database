// q1
    $("#btn_q1").click(function(){  
    console.log('q1hhhh');
    var UserID =$("#UserID").val()
    $.ajax({
        type : "POST",
        url : "query1/",
        dataType : "html",
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            UserID: UserID,
        },
        async : true,
        success : function(data) {
            $("#UserID").val(UserID); 
            $("#result_q1").html(data); 
        },
        error : function() {
            alert('请求有误');
        }
    });
    });

    $("#btn_q2").click(function(){  
        console.log('q2hhhh');
        var KeyWord =$("#KeyWord").val()
        $.ajax({
            type : "POST",
            url : "query2/",
            dataType : "html",
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                KeyWord: KeyWord,
            },
            async : true,
            success : function(data) {
                $("#KeyWord").val(KeyWord); 
                $("#result_q2").html(data); 
            },
            error : function() {
                alert('请求有误');
            }
        });
        });

$("#btn_q3").click(function(){  
    console.log('q3hhhh');
    var Style =$("#Style").val()
    $.ajax({
        type : "POST",
        url : "query3/",
        dataType : "html",
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            Style: Style,
        },
        async : true,
        success : function(data) {
            $("#Style").val(Style); 
            $("#result_q3").html(data); 
        },
        error : function() {
            alert('请求有误');
        }
    });
    });