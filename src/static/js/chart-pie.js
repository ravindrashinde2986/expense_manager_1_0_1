// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var category = ctx.dataset.category
console.log(category)
var categoryArray = category.split(',');
var amount = ctx.dataset.amount
var amountArray = amount.split(',');

var myPieChart = new Chart(ctx, {
  type: 'horizontalBar',
  data: {
//    labels: ["Direct", "Referral", "Social"],
    labels: categoryArray,
    datasets: [{
//      data: [55, 30, 15],
      data: amountArray,
      backgroundColor: ['#4B0082','#0000FF','#00FF00', '#FFFF00', '#FF7F00', '#FF0000','#4e73df', '#1cc88a',
      '#36b9cc', '#ff0080', '#8000ff'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 20,
      yPadding: 20,
      displayColors: true,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});

//var chart = new Chart(ctx,
//	{
//
//		legend: {
//			maxWidth: 350,
//			itemWidth: 120
//		},
//		data: [
//		{
//			type: "pie",
//			showInLegend: true,
//			legendText: "{indexLabel}",
//			dataPoints: [
//				{ y: 4181563, indexLabel: "PlayStation 3" },
//				{ y: 2175498, indexLabel: "Wii" },
//				{ y: 3125844, indexLabel: "Xbox 360" },
//				{ y: 1176121, indexLabel: "Nintendo DS"},
//				{ y: 1727161, indexLabel: "PSP" },
//				{ y: 4303364, indexLabel: "Nintendo 3DS"},
//				{ y: 1717786, indexLabel: "PS Vita"}
//			]
//		}
//		]
//	});
//	chart.render();
