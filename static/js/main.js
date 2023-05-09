$(document).ready(function(){
    $('#load').on('click',function(){
        ajax.Load();
    })
    $('#save').on('click',function(e){
         e.preventDefault();
        ajax.Save();
    });

});
var ajax ={ 
    Load(){
        $.ajax({
            type: 'POST',
            url: "load/",
            headers: {
                "X-CSRFToken" : csrf
            },
            success: function (e) {
//                let data = JSON.parse(e.data);
                let users = e.users; 
                let trips = e.trips;
                $('#loaded').text(users+" and TRIPS:"+trips); 
                // console.log(data)

            },
            error: function (e) {
                console.log("error:"+JSON.stringify(e));
            }
        });

    },

    Save(){
        console.log("save??");
        data = {
           data : JSON.stringify({
               first_name : $('#fname').val(),
               last_name : $('#lname').val(),
               date : $('#date').val(),
            })
        }
        $.ajax({
            type: 'POST',
            url: "save/",
            headers: {
                "X-CSRFToken" : csrf
            },
            data : data,
            success: function (e) {
                  console.log('settings save success:'+JSON.stringify(e).trim(0,200));

            },
            error: function (e) {
                console.log("setting save err: "+ JSON.stringify(e).trim(0,200));
//                $('html').html(JSON.stringify(e));
            }
        });

    },
}
