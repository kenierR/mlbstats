
const labels = ['Enero', 'Febrero', 'Marzo', 'Abril']


console.log(x)

const dataset1 = {
    label: "BTC",
    data: x,
    borderColor: 'rgba(248, 37, 37, 0.8)',
    fill: false,
    tension: 0.1
};


const graph = document.querySelector("#graph");

const data = {
    labels: labels,
    datasets: [dataset1]
};

const config = {
    type: 'line',
    data: data,
};

new Chart(graph, config);