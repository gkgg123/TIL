<template>
  <div>
    <input  type="text" v-model="inputData" @keypress.enter="onsearch"> 
    <button @click="onsearch">검색</button>
  </div>
</template>

<script>
export default {
  name : 'SeachBar',
  data(){
    return {
      inputData : '',
    }
  },
  methods : {
    onsearch(){
  
      this.$emit('search-list',this.inputData)
      this.inputData = ''

    }
  }
  
}
</script>

<style>

</style>