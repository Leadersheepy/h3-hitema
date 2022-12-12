<template>
  <form @submit.prevent="submit($event)" class="signup-form">
    <h1 class="signup-title">Créer un nouveau profil</h1>

    <input type="text" id="username" class="signup-input" placeholder="pseudo" v-model="pseudo">

    <div class="espacement"></div>

    <input type="email" id="email" class="signup-input" placeholder="votre@email.fr" v-model="email">

    <div class="espacement"></div>

    <input type="password" id="password" class="signup-input" placeholder="confirmer password" v-model="password">

    <div class="espacement"></div>

    <input type="password" id="imageUrl" class="signup-input" placeholder="url de votre image - taille conseillée 1000x200px
    " v-model="urlImgProfil">

    <div class="espacement"></div>

    <button type="submit" class="signup-button">Créer un nouveau profil</button>
  </form>
</template>

<script setup lang="ts">

import {useUserStore} from "@/stores/userStore"
import router from "@/router";
import {ref} from "vue";

let userStore = ref(useUserStore());
let pseudo = ref('');
let email = ref('');
let password = ref('');
let urlImgProfil = ref('');

function submit() {
  const identifiants = {email: email.value, password: password.value, pseudo: pseudo.value, urlImgProfil: urlImgProfil.value}
  userStore.value.add(identifiants)
  router.push("/")
}

</script>