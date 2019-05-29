// q1
function query1() {
    console.log('hhhh');
    $.ajax({
        type : "POST",
        url : "query",
        dataType : "html",
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            UserID: $("#UserID").val(),
        },
        async : true,
        success : function(data) {
            //$("#UserID").val(userID); 
            $("#result_q1").html(data); 
        },
        error : function() {
            alert('请求有误');
        }
    });
}
// $(document).ready(function(){
//     $("#btn_q1").click(function(){  
//         console.log("点击成功"); 
//         var userID = $("#UserID").val();   
//         $.post(
//             "/search/",
//             {'UserID':userID},  // 参数传递
//             function(data,status)
//             {               
//                $("#UserID").val(userID);  
//                $("#result_q1").html(data);         
//            }
//        );
//    });
//    });
