<template>
    
    <form @submit.prevent="submit($event)" class="login-form">
        <h1 class="login-title">Se connecter</h1>

        <input v-model="email" placeholder="votre@emailfr" type="text" id="username" class="login-input">

        <div class="espacement"></div>

        <input type="password"  v-model="password" placeholder="password" id="password" class="login-input">

        <div class="espacement"></div>

        <button type="submit"  value="Se connecter" class="login-button">connexion</button>
    </form>
  
  </template>
  
  <script lang="ts">
  import {useUserStore} from "@/stores/userStore"
  import router from "@/router";
  
  export default {
    methods: {
      submit: function () {
        const identifiants = {email: this.email, password: this.password}
        this.userStore.login(identifiants);
        router.push("/")
      }
    },
    data : () => {
      return {
        email : "",
        password : "",
        userStore : useUserStore()
      }
    }
  }
  </script>


 