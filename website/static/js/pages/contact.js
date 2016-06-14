var Contact = function () {

    return {

        //Map
        initMap: function () {
            var map;
            $(document).ready(function(){
                map = new GMaps({
                    div: '#map',
                    lat: 30.258888,
                    lng: 120.122611
                });
                var marker = map.addMarker({
                    lat: 30.258888,
                    lng: 120.122611,
                    title: '曹光彪东楼414室',
                    infoWindow: {
                        content: '<div class="container"><div class="row"> <div class="col-md-12"> <ul class="list-unstyled who"> <li><a href="#"><i class="fa fa-home"></i>浙江杭州市浙大路38号浙江大学玉泉校区曹光彪东楼414室</a></li> <li><a href="#"><i class="fa fa-envelope"></i>chenwz[at]zju.edu.cn</a></li> <li><a href="#"><i class="fa fa-phone"></i>0571-87952433</a></li> <li><a href="http://arc.zju.edu.cn"><i class="fa fa-globe"></i>http://arc.zju.edu.cn</a></li> </ul> </div> </div> </div>'
                    }
                });
                var infoW1 = new google.maps.InfoWindow({
                    content: '<div class="container"><div class="row"> <div class="col-md-12"> <ul class="list-unstyled who"> <li><a href="#"><i class="fa fa-home"></i>浙江杭州市浙大路38号浙江大学玉泉校区曹光彪西楼401室</a></li> <li><a href="#"><i class="fa fa-envelope"></i>chenwz[at]zju.edu.cn</a></li> <li><a href="#"><i class="fa fa-phone"></i>0571-87952433</a></li> <li><a href="http://arc.zju.edu.cn"><i class="fa fa-globe"></i>http://arc.zju.edu.cn</a></li> </ul> </div> </div> </div>'
                });
                var marker1 = map.addMarker({
                    lat: 30.259601,
                    lng: 120.120894,
                    title: '曹光彪西楼401室',
                    infoWindow: infoW1
                });
                infoW1.open(map,marker1)
            });
        }

    };
}();
