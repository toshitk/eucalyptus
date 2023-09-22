<template>
  <div style="height: 500px;">
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<script lang="ts">
import {
CategoryScale,
Chart as ChartJS,
Legend,
LineElement,
LinearScale,
PointElement,
Title,
Tooltip
} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

export default {
  components: {
    Line
  },
  data() {
    return {
      chartData: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [40, 39, 10, 40, 39, 100, 40]
          },
          {
            label: 'Data',
            backgroundColor: '#f87979',
            data: [10, 20, 30, 40, 50, 100, 40]
          },
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  }
}
</script>