<template>
  <div>
    <p>List입니다.</p>
    <li v-for="todo in todos" v-bind:key="todo.id" :class="{completed :todo.isCompleted}">
      <input type="checkbox" v-model ="todo.isCompleted">{{todo.content}}
      {{todo.isCompleted}}

    </li>
  </div>
</template>

<script>
export default {
  name : 'TodoList',
  props : {
    todos : {
      type : Array,
      required : true,
    }
  }

}
</script>

<style>
  .completed {
    text-decoration: line-through;
  }
</style>