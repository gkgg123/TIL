<template>
  <div>
    <input type="text" v-model="todo" @keypress.enter="createTodo">
    <button @click="createTodo">제출</button>
  </div>
</template>

<script>
export default {
  name : 'TodoInput',
  data(){
    return {
      todo : ''
    }
  },
  methods :{
    createTodo(){
      const newTodo ={
        id : Date.now(),
        content : this.todo,
        isCompleted : false,
      }
      this.$emit('create-todo',newTodo)
      this.todo = ""
    },

  }

}
</script>

<style>

</style>