const jsonString = `{
  "vendas": [
    {
      "data": "2023-07-01",
      "quantidade_vendida": {
        "A": 18,
        "B": 12,
        "C": 6
      }
    },
    {
      "data": "2023-07-02",
      "quantidade_vendida": {
        "A": 9,
        "B": 15,
        "C": 8
      }
    },
    {
      "data": "2023-07-03",
      "quantidade_vendida": {
        "A": 12,
        "B": 3,
        "C": 7
      }
    },
    {
      "data": "2023-07-04",
      "quantidade_vendida": {
        "A": 6,
        "B": 4,
        "C": 3
      }
    },
    {
      "data": "2023-07-05",
      "quantidade_vendida": {
        "A": 9,
        "B": 8,
        "C": 9
      }
    },
    {
      "data": "2023-07-06",
      "quantidade_vendida": {
        "A": 14,
        "B": 10,
        "C": 11
      }
    },
    {
      "data": "2023-07-07",
      "quantidade_vendida": {
        "A": 11,
        "B": 9,
        "C": 5
      }
    }
  ]
}`;

const dataJSON = JSON.parse(jsonString);

const dates = dataJSON.vendas.map(item => item.data);

const quantidade_vendida_A = dataJSON.vendas.map(item => item.quantidade_vendida.A);
const quantidade_vendida_B = dataJSON.vendas.map(item => item.quantidade_vendida.B);
const quantidade_vendida_C = dataJSON.vendas.map(item => item.quantidade_vendida.C);

const convertedDates = dates.map(date => {
  return new Date(
    parseInt(date.slice(0, 4)),   // Year
    parseInt(date.slice(5, 7)) - 1, // Month (0-indexed)
    parseInt(date.slice(8, 10)),  // Day
  );
});

const data = {
  labels: dates,
  datasets: [
    {
      label: 'Produto A',
      data: quantidade_vendida_A,
      backgroundColor: [
        'rgba(255, 0, 0, 0.2)',
      ],
      borderColor: [
        'rgba(255, 0, 0, 1)',
      ],
      borderWidth: 1
    },
    {
      label: 'Produto B',
      data: quantidade_vendida_B,
      backgroundColor: [
        'rgba(0, 0, 255, 0.2)',
      ],
      borderColor: [
        'rgba(0, 0, 255, 1)',
      ],
      borderWidth: 1
    },
    {
      label: 'Produto C',
      data: quantidade_vendida_C,
      backgroundColor: [
        'rgba(0, 128, 0, 0.2)',
      ],
      borderColor: [
        'rgba(0, 128, 0, 1)',
      ],
      borderWidth: 1
    }
  ]
};

const config = {
  type: 'bar',
  data,
  options: {
    scales: {
      x: {
        type: 'time',
        time: {
          unit: 'day'
        },
        stacked: true
      },
      y: {
        beginAtZero: true,
        stacked: true
      }
    }
  }
};

const myChart = new Chart(
  document.getElementById('chart'),
  config
);

function convertStringToDate(date){
  new_date = new Date(
    parseInt(date.slice(0, 4)),
    parseInt(date.slice(5, 7)) - 1,
    parseInt(date.slice(8, 10)),
  );

  return new_date
}

function filterData(start, end, datapoints, size){
  const dtpoints = [... datapoints];
  dtpoints.splice(end + 1, size);
  dtpoints.splice(0, start);

  return dtpoints
}

function filterDate() {
  const startValue = document.getElementById('start').value;
  const endValue = document.getElementById('end').value;

  const start = convertStringToDate(startValue)
  const end = convertStringToDate(endValue)

  const start_date = start.getTime()
  const end_date = end.getTime()

  const filterDates = convertedDates.filter(date => date >= start_date && date <= end_date)

  myChart.config.data.labels = filterDates;

  const startArray = convertedDates.indexOf(filterDates[0]);
  const endArray = convertedDates.indexOf(filterDates[filterDates.length - 1]);

  const data_1 = filterData(startArray, endArray, quantidade_vendida_A, filterDates.length)
  myChart.config.data.datasets[0].data = data_1;

  const data_2 = filterData(startArray, endArray, quantidade_vendida_B, filterDates.length)
  myChart.config.data.datasets[1].data = data_2;

  const data_3 = filterData(startArray, endArray, quantidade_vendida_C, filterDates.length)
  myChart.config.data.datasets[2].data = data_3;

  myChart.update();
}

function resetDate() {
  myChart.config.data.labels = convertedDates;
  myChart.config.data.datasets[0].data = quantidade_vendida_A;
  myChart.config.data.datasets[1].data = quantidade_vendida_B;
  myChart.config.data.datasets[2].data = quantidade_vendida_C;

  myChart.update()
}