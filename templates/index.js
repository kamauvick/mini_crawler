// Our labels along the x-axis
var years = [1500, 1600, 1700, 1750, 1800, 1850, 1900, 1950, 1999, 2050];
// For drawing the lines
var africa = [86, 114, 106, 106, 107, 111, 133, 221, 783, 2478];
var asia = [282, 350, 411, 502, 635, 809, 947, 1402, 3700, 5267];
var europe = [168, 170, 178, 190, 203, 276, 408, 547, 675, 734];
var latinAmerica = [40, 20, 10, 16, 24, 38, 74, 167, 508, 784];
var northAmerica = [6, 3, 2, 2, 7, 26, 82, 172, 312, 433];
// var prices = [{% for data in %}];

var ctx = document.getElementById("myChart");
var pie = document.getElementById("mypie");
var polar = document.getElementById("myPolar");

var myChart = new Chart(ctx, {
    type: 'radar',
    data: {
        labels: years,
        datasets: [
            {
                data: northAmerica,
                label: 'northAmerica',
                borderColor: "#3e95cd",
                fill: false
            },
            {
                data: africa,
                label: 'Africa',
                borderColor: "#8e5ea2",
                fill: false
            },
            {
                data: asia,
                label: 'Asia',
                borderColor: "#3cba9f",
                fill: false
            },
            {
                data: europe,
                label: 'Europe',
                borderColor: "#e8c3b9",
                fill: false
            },
            {
                data: latinAmerica,
                label: 'LatinAmerica',
                borderColor: "#c45850",
                fill: false
            }
        ]
    }
});

var mypie = new Chart(pie, {
    type: 'doughnut',
    data: {
        labels: years,
        datasets: [
            {
                data: northAmerica,
                label: 'northAmerica',
                borderColor: "#3e95cd",
                fill: false,
                borderWidth: 2,
            },
            {
                data: africa,
                label: 'Africa',
                borderColor: "#8e5ea2",
                fill: false,
                borderWidth: 2,
            },
            {
                data: asia,
                label: 'Asia',
                borderColor: "#3cba9f",
                fill: false,
                borderWidth: 2,
            },
            {
                data: europe,
                label: 'Europe',
                borderColor: "#e8c3b9",
                fill: false,
                borderWidth: 2,
            },
            {
                data: latinAmerica,
                label: 'LatinAmerica',
                borderColor: "#c45850",
                fill: false,
                borderWidth: 2,
            }
        ]
    }
});

var myPolar = new Chart(polar, {
    type: 'bar',
    data: {
        labels: years,
        datasets: [
            {
                data: northAmerica,
                label: 'northAmerica',
                backgroundColor: "#3e95cd",
                fill: false
            },
            {
                data: africa,
                label: 'Africa',
                backgroundColor: "#8e5ea2",
                fill: false
            },
            {
                data: asia,
                label: 'Asia',
                backgroundColor: "#3cba9f",
                fill: false
            },
            {
                data: europe,
                label: 'Europe',
                backgroundColor: "#e8c3b9",
                fill: false
            },
            {   
                data: latinAmerica,
                label: 'LatinAmerica',
                backgroundColor: "#c45850",
                fill: false
            }
        ]
    }
});