function doClick2() {
   var ie7 = chart.get('ie7');
    ie7.y = 1;
    ie7.update(ie7,false);
    chart.isDirty = true;
    chart.redraw();
}
function doClick() {
   var ie7 = chart.get('ie7');
    ie7.y = 50;
    ie7.update(ie7,false);
    chart.isDirty = true;
    chart.redraw();
}

$(function () {
    
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'container',
            type: 'pie',
            events: {
                redraw: function(){
                    console.log(this.series[0].data);
                    $(this.series[0].data).each(function(i,e){
                        if(e.setVisible && e.percentage>5){
                            e.setVisible(true);
                        }
                    });
                    
                }
            }
        },
        
        plotOptions: {
            pie: {
                showInLegend: false,
                dataLabels: {
                    formatter: function(){
                        console.log(this);
                        if (this.percentage > 5) {
                            this.point.visible = true;
                            return this.key;
                        }
                       else {
                            this.point.visible = false;
                            return '';
                       }
                    }
                }
            
            }
        },
        
        series: [{
            data: [
                {name:'Firefox',   y:44.2, id:'firefox'},
                {name:'IE7 long',  y:2.6, id:'ie7'},
                {name: 'IE6 long', y:20, id:'ie6'}
            ]
        }]
    });
});