import { createApp } from 'vue'
import App from './App.vue'
//import HelloWorld from './components/HelloWorld.vue' basically you will import the component you want to use
import router from './router'

//createApp(App).mount('#app')

createApp(App).use(router).mount('#app')