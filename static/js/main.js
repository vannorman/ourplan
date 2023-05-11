$(document).ready(function(){
    $('#load').on('click',function(){
        ajax.Load();
    })
    $('#save').on('click',function(e){
         e.preventDefault();
        ajax.Save();
    });


    // Add city
    $city = $('#cities').html(); // copy the existing city
    $('#addCity').on('click',function(){
       $('#cities').append($city);
       var newCity= Object.assign({}, city)
       trip.cities.push(newCity);
       console.log("cities len:"+trip.cities.length);
    });

    $(document).on('click', '.deleteCity', function() {
        $(this).closest('tr').remove();
      //code here ....
    });

    $(document).on('keyup change', 'input', function() {
        if ($(this).attr('id') === "startDate") {
            let date = $(this).val();
            trip.startDate = parseInt(date);
            UpdateCalendar()
        }

        if ($(this).attr('class') === "city"){
            let row = $(this).closest('tr').index();
            trip.cities[row].name = $(this).val();             
            console.log("updating row :"+row);
            UpdateCalendar();
        }
        if ($(this).attr('class') === "numDays"){
            let row = $(this).closest('tr').index();
            trip.cities[row].days = parseInt($(this).val());   
            UpdateCalendar();
        }
    //    console.log('ch:'+$(this).val());
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


// Add rows of boxes for the calendar
document.addEventListener("DOMContentLoaded", function() {

  for (var i = 1; i < 30; i++) {
    $('.container').append($('<div class="box" id="box'+i+'"><div class="num">'+i+'</div><div class="city"></div></div>'));
  }
});


var city = {
    name : "new city",
    days : 1
}

var trip = {
    startDate : 1,
    cities : [
        {
            name : "empty",
            days : 1,
        },
    ],
    getColorForCity(i) {
        return "hsl("+i*40+",20%,50%)";
    }
}

function UpdateCalendar(){
    $('.box').css('background','#e0e0e0');
    $('#box'+trip.startDate).css('background','#abc');
    $('.box').each(function(){
        $(this).find('.city').text('');
    })
    var days = 0;
    for(let i=0;i<trip.cities.length;i++){
        //console.log("trip startdate:"+trip.startDate+", days:"+days+", sum:"+trip.startDate+days);
        let day = days + trip.startDate;
        let cityName = trip.cities[i].name;
//        console.log("updating "+day+" with "+cityName);
        $('#box'+day).find('.city').text(cityName);

        let cityStartDate = trip.startDate + days;
        // color the boxes
        
        for (let j=cityStartDate;j<cityStartDate+trip.cities[i].days;j++){
            let color = trip.getColorForCity(i);
            $('#box'+j).css('background',color);
        }
        days += trip.cities[i].days;
    }

}
