<template>
  <div>
    <button @click="fetchData">Fetch Data</button>
    <pre>{{ data }}</pre>
  </div>
</template>

<script lang="ts">
import { ref, defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'FetchDataComponent',
  setup() {
    const data = ref<any>(null);

    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/users/1');
        data.value = response.data;
      } catch (error) {
        console.error('An error occurred:', error);
        data.value = 'An error occurred';
      }
    };

    return {
      data,
      fetchData
    };
  }
});
</script>
