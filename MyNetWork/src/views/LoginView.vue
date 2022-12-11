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


  <style>
    /* Style the login form using CSS */
    .login-form {
      max-width: 500px;
      margin: 50px auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  
    .login-title {
      text-align: center;
      margin-bottom: 20px;
    }
  
    .espacement{
      margin-bottom: 20px;
    }
  
    .login-input {
      width: 100%;
      padding: 10px;
      border-radius: 4px;
      border: 1px solid #ccc;
    }
  
    .login-button {
      display: block;
      margin: 0 auto;
      background-color: #337ab7;
      border-color: #2e6da4;
      color: #fff;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
    }
  
    .login-button:hover {
      background-color: #286090;
      border-color: #204d74;
    }
  </style>

  