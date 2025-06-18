<template>
  <div class="container">
    <h1>Todo List</h1>

    <form @submit.prevent="addTodo">
      <input v-model="newTodo" placeholder="Enter a task" required />
      <button>Add</button>
    </form>

    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <label>
          <input type="checkbox" v-model="todo.completed" @change="toggleTodo(todo)" />
          <span :style="{ textDecoration: todo.completed ? 'line-through' : 'none' }">
            {{ todo.title }}
          </span>
        </label>
        <button @click="deleteTodo(todo.id)">❌</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      todos: [],
      newTodo: '',
    }
  },
  methods: {
    async fetchTodos() {
      const res = await axios.get('http://localhost:8000/todos')
      this.todos = res.data
    },
    async addTodo() {
      const res = await axios.post('http://localhost:8000/todos', {
        title: this.newTodo,
        completed: false,
      })
      this.todos.push(res.data)
      this.newTodo = ''
    },
    async deleteTodo(id) {
      await axios.delete(`http://localhost:8000/todos/${id}`)
      this.todos = this.todos.filter((todo) => todo.id !== id)
    },
    async toggleTodo(todo) {
      await axios.put(`http://localhost:8000/todos/${todo.id}`, {
        ...todo,
        completed: !todo.completed,
      })
      this.fetchTodos()
    },
  },
  mounted() {
    this.fetchTodos()
  },
}
</script>

<style>
.container {
  max-width: 500px;
  margin: auto;
  padding: 1rem;
  font-family: sans-serif;
}
button {
  margin-left: 1rem;
}
</style>
