<template>
  <div>
    <h1>API Response:</h1>
    <p>{{ response }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      response: null,
    };
  },
  async created() {
    try {
      const res = await axios.get('http://localhost:8000/users/1');
      this.response = res.data;
    } catch (error) {
      console.error(error);
    }
  },
};
</script>
