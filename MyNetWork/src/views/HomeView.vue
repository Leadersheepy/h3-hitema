
<template>

    <div id="wrapper" v-for="article in articles">
        
        <header class="headerPost">
                <h1 class="name">{{ article.pseudo }}</h1>
                <img class='profile-pic' :src="utilisateurs.filter(function(val) {
        return val.pseudo === article.pseudo
      })[0].urlImgProfil">
                <p class="date">posté le 28/03/2021 à 05h54</p>
        </header>
        
        <p class="status">{{ article.contenu }}</p>
        <img class="img-content" :src="article.urlImgArticle" />
        
        <div class="action headerPost">

            <div class="commentary">
                <a href="#">
                    <img src="../assets/comment.png" />
                    <p>Counter</p>
                </a>
            </div>

            <div class="like">
                <a href="#">
                    <img src="https://1.bp.blogspot.com/-qns_lZPjg0I/VWY2dO1HN-I/AAAAAAAACVA/akLTMY7RJSk/s1600/Thumbs-up-facebook-icon-small.png" alt="thumbs up" />
                    <p>Counter</p> 
                </a>
            </div>
            
        </div>

        <h3 class="commentaire"> Commentaires : </h3>
        
        <div class="comment">
            <div class="comment-author">
                <h3 class="comment-name">John Doe</h3>
                <p class="comment-date">December 11, 2022</p>
            </div>
            <p class="comment-content">This is a comment on the post.</p>
        </div>
    </div>
    
    </template>

<script setup lang="ts">

import {ref, onMounted} from "vue"
import {useUserStore} from "../stores/userStore"

let userStore = useUserStore();

let articles = ref([]);
let utilisateurs = ref([]);

onMounted(() => {
  const userEmail = userStore.user.email

  fetch("http://localhost:3000/articles")
      .then(response => response.json())
      .then(data => articles.value = data)

  fetch("http://localhost:3000/utilisateurs")
      .then(response => response.json())
      .then(data => utilisateurs.value = data)
      .then(data => {
        console.log(data.filter(function (val) {
          return val.pseudo === "Alain"
        })[0])
      })
})
</script>

<style>
  /* Style the comment using CSS */
  .comment {
    margin-top: 20px;
    border: 1px solid rgb(207, 204, 204);
    border-radius: 10px;
  }

  .comment-author {
    display: flex;
    align-items: center;
  }

  .comment-avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
  }

  .comment-name {
    font-size: 18px;
    margin-left: 10px;
  }

  .comment-date {
    font-size: 14px;
    color: #999;
    margin-left: 10px;
  }

  .comment-content {
    font-size: 16px;
    line-height: 1.5;
    margin-top: 10px;
  }
</style>
