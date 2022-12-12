<template>
  <div class="alignementNavBar">
    <header>
      <h1 class="title">MyNetWork <img class="petitLogo" src="../assets/logo.png"></h1>
      <nav>
        <router-link to="/">Fils d'actualité</router-link>
        <router-link to="/creation">Créer un profil</router-link>
        <router-link to="/identification" v-if="!userStore.user.isLogged">Se connecter</router-link>
        <router-link to="/" v-else @click="deconnection()">Se déconnecter</router-link>
      </nav>
    </header>
  </div>
</template>

<script setup lang="ts">

import {ref, onMounted} from "vue"
import router from "@/router";
import {useUserStore} from "@/stores/userStore"

let userStore = ref(useUserStore());

let isLogged = ref(false);

function deconnection() {
  userStore.value.logout();
  router.push('/');
}

onMounted(() => {
  userStore.value.get_cookies();

  isLogged.value = userStore.value.user.isLogged
})

</script>