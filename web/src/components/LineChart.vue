<template>
  <div style="height: 500px;">
    <Line :data="data" :options="options" />
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
import * as chartConfig from './chartConfig.js'

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
    return chartConfig
  }
}
</script>

<style scoped>
.chart-container {
  height: 500px;
}
</style>