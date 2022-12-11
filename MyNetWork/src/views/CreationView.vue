<template>
<form class="signup-form">
    <h1 class="signup-title">Créer un nouveau profil</h1>

    <input type="text" id="username" class="signup-input"  placeholder="pseudo">

    <div class="espacement"></div>
    
    <input type="email" id="email" class="signup-input"  placeholder="votre@email.fr">

    <div class="espacement"></div>

    <input type="password" id="password" class="signup-input"  placeholder="confirmer password">

    <div class="espacement"></div>

    <input type="password" id="imageUrl"  class="signup-input"  placeholder="url de votre image - taille conseillée 1000x200px
    ">

    <div class="espacement"></div>

    <button type="submit" class="signup-button">Créer un nouveau profil</button>
  </form>
</template>
  <style>
    /* Style the sign up form using CSS */
    .signup-form {
      max-width: 500px;
      margin: 50px auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  
    .signup-title {
      text-align: center;
      margin-bottom: 20px;
    }
  
    .signup-label {
      display: block;
      margin-bottom: 10px;
    }
  
    .signup-input {
      width: 100%;
      padding: 10px;
      border-radius: 4px;
      border: 1px solid #ccc;
    }
  
    .signup-button {
      display: block;
      margin: 0 auto;
      background-color: #337ab7;
      border-color: #2e6da4;
      color: #fff;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
    }
  
    .signup-button:hover {
      background-color: #286090;
      border-color: #204d74;
    }
  </style>