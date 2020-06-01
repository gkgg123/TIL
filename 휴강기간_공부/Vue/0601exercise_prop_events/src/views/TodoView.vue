<template>
  <div>
    <h1>TodoView</h1>
    <TodoInput @create-todo="createTodo"/>
    <TodoList v-bind:todos="todos" />
  </div>
</template>

<script>
import TodoInput from '@/components/TodoInput.vue'
import TodoList from '@/components/TodoList.vue'
export default {
  name : 'TodoView',
  components :{
    TodoInput,
    TodoList,
  },
  data() {
    return {
      todos : [
        {
          id : 1,
          content : 'django복습',
          isCompleted : true,
        },
        {
          id : 2,
          content : 'vue복습',
          isCompleted : false,
        }
      ]
    }
  },
  methods:{
    createTodo(newTodo){
      this.todos.push(newTodo)
    }
  } 
}
</script>

<style>

</style>