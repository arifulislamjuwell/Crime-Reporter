$('.chech').on('change', function() {
    value= this.value;
  
    if(value=='dhaka'){
      items=['Dhaka','Kishoreganj','Gopalganj','Jamalpur', 'Faridpur', 'Gazipur', 'Tangail','Narsingdi','Narayanganj','Netrakona','Faridpur','Mymensingh','Madaripur','Manikganj','Munshiganj','Rajbari','Shariatpur','Shariatpur']
      var str = ""
      for (var item of items) {
      str += "<option value="+ item.toLowerCase()+ '>' +  item + "</option>"

    }
    document.getElementById("check11").innerHTML = str;
    }
  
    else if(value=='chittagong'){
      items=['Chattogram','Bandarban','Brahmanbaria','Chandpur','Cumilla',"Cox's Bazar",'Feni','Khagrachhari','Lakshmipur','Noakhali','Rangamati']
      var str = ""
      for (var item of items) {
      str += "<option value="+item.toLowerCase()+'>'+  item + "</option>"
    }
    document.getElementById("check11").innerHTML = str;
    }
  
    else if(value=='barishal'){
      items=['Barishal','Barguna','Bhola','Jhalokati','Patuakhali','Pirojpur']
      var str = ""
      for (var item of items) {
      str += "<option value="+item.toLowerCase()+'>'+  item + "</option>"
    }
    document.getElementById("check11").innerHTML = str;
    }
  
    else if(value=='khulna'){
      items=['Khulna','Bagerhat','Chuadanga','Jashore','Jhenaidah','Kushtia','Magura','Meherpur','Narail','Satkhira']
      var str = ""
      for (var item of items) {
      str += "<option value="+item.toLowerCase()+'>'+  item + "</option>"
    }
    document.getElementById("check11").innerHTML = str;
    }
  
    else if(value=='rajshahi'){
      items=['Rajshahi','Bogura','Joypurhat','Naogaon','Natore','Chapainawabganj','Pabna','Sirajgonj']
      var str = ""
      for (var item of items) {
      str += "<option value="+item.toLowerCase()+'>'+  item + "</option>"
    }
    document.getElementById("check11").innerHTML = str;
    }
  
    else if(value=='rangpur'){
      items=['Rangpur','Dinajpur','Gaibandha','Kurigram','Lalmonirhat','Nilphamari','Panchagarh','Thakurgaon']
      var str = ""
      for (var item of items) {
      str += "<option value="+item.toLowerCase()+'>'+  item + "</option>"
    }
    document.getElementById("check11").innerHTML = str;
    }
  
    else if(value=='sylhet'){
      items=['Sylhet','Habiganj','Moulvibazar','Sunamganj']
      var str = ""
      for (var item of items) {
      str += "<option value="+item.toLowerCase()+'>'+  item + "</option>"
    }
    document.getElementById("check11").innerHTML = str;
    }
  
    else if(value=='mymensingh'){
      items=['Mymensingh','Jamalpur','Sherpur','Netrokona']
      var str = ""
      for (var item of items) {
      str += "<option value="+item.toLowerCase()+'>'+  item + "</option>"
    }
    document.getElementById("check11").innerHTML = str;
    }
  });
  