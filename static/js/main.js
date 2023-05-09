$(document).ready(function(){
    $('#load').on('click',function(){
        alert('load:');
        ajax.Load();
    })
    $('#save').on('click',function(e){
         e.preventDefault();
        alert('save:');
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
                console.log('settings load returned:');
                let data = JSON.parse(e.data);
                console.log(data)

            },
            error: function (e) {
                console.log("Load settings error:"+JSON.stringify(e));
            }
        });
        $('html').on(Input.end, function(){
            if (Menu.settingsShown){
                Settings.SaveSettings();
            }
        });

    },

    Save(){
        console.log("save??");
        data = {
           settings : JSON.stringify({
               name : $('#fname').val(),
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
